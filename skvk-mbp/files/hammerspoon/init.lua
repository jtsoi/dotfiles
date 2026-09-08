-- Managed by skvk-mbp/mise.toml ([dotfiles]).
--
-- Drawing surface for AeroSpace's `new` binding mode (Caps+N): shows a centred
-- overlay while the mode is active, hidden the instant it exits. AeroSpace
-- owns the keys and the mode; this file owns pixels only, reached over
-- `hs.ipc` from `on-mode-changed` in aerospace.toml. It never binds a key and
-- never manages a window — those are AeroSpace's domain, and reaching into
-- either would put the two tools in a fight over the same keys and windows.

require("hs.ipc") -- the only thing that makes `hs -c` reachable from outside

-- hs.execute inherits whatever environment happened to launch Hammerspoon,
-- which is not guaranteed to have `aerospace` on PATH. Pinned for the same
-- reason VS Code's CLI is invoked by its in-bundle path rather than `code`.
local AEROSPACE = "/opt/homebrew/bin/aerospace"

-- Colours live in colors.sh, not here, so a re-theme touches one file. Read
-- once at load: colors.sh doesn't change while Hammerspoon is running, and a
-- config reload (which re-runs this file) is what picks up an edit to it.
local function palette(path)
  local t = {}
  for line in io.lines(path) do
    -- Lua's %w excludes underscores, and every role name here has one
    -- (BAR_BG, CHIP_BORDER, ...), so [%w_] is required or nothing matches.
    local k, hex = line:match("^export%s+([%w_]+)=0x(%x%x%x%x%x%x%x%x)")
    if k then
      t[k] = { alpha = tonumber(hex:sub(1, 2), 16) / 255,
               red   = tonumber(hex:sub(3, 4), 16) / 255,
               green = tonumber(hex:sub(5, 6), 16) / 255,
               blue  = tonumber(hex:sub(7, 8), 16) / 255 }
    end
  end
  return t
end

-- A missing colors.sh must not stop this file loading. io.lines raises, and an
-- unloaded config means modeChanged is undefined -- so Caps+N would capture the
-- keyboard with nothing on screen to say so, which is the worst failure this
-- design has. Degrade to greyscale: visibly wrong, but never invisible.
local ok, PALETTE = pcall(palette, os.getenv("HOME") .. "/.config/sketchybar/colors.sh")
if not ok or not PALETTE.OVERLAY_BG then
  PALETTE = { OVERLAY_BG = { white = 0.15, alpha = 0.9 },
              TOAST_BG   = { white = 0.15, alpha = 0.8 },
              OVERLAY_FG = { white = 1.00, alpha = 1 },
              FG         = { white = 0.95, alpha = 1 },
              ACTIVE_BG  = { white = 1.00, alpha = 1 } }
end

-- Row order mirrors [mode.new.binding] in aerospace.toml: a dim title, then
-- one row per key that mode defines.
local ROWS = {
  { key = nil,   label = "NEW WINDOW" },
  { key = "g",   label = "Google Chrome" },
  { key = "f",   label = "Firefox" },
  { key = "c",   label = "Code" },
  { key = "esc", label = "cancel" },
}

local FONT = "JetBrainsMono Nerd Font" -- matches sketchybarrc's $FONT
local W, ROW_H, PAD = 250, 30, 14
local H = #ROWS * ROW_H + PAD * 2

local overlay = nil

function overlayShow()
  if overlay then overlay:delete() end

  -- Read the screen fresh on every show, not once at load, so the overlay
  -- self-corrects when the built-in and the BenQ swap which one is main.
  local ff = hs.screen.mainScreen():fullFrame()
  local x = ff.x + (ff.w - W) / 2
  local y = ff.y + (ff.h - H) / 2

  local elements = {
    -- Inset by half the stroke width: hs.canvas centres a stroke on its path, so
    -- a rect flush to the canvas edge loses the outer half of its border to
    -- clipping. White on a light window is inherently low contrast -- 3px is
    -- what makes it read there without looking heavy over dark ones.
    { type = "rectangle", action = "strokeAndFill",
      fillColor = PALETTE.OVERLAY_BG, strokeColor = PALETTE.OVERLAY_FG, strokeWidth = 3,
      roundedRectRadii = { xRadius = 12, yRadius = 12 },
      frame = { x = 1.5, y = 1.5, w = W - 3, h = H - 3 } },
  }

  for i, row in ipairs(ROWS) do
    local ty = PAD + (i - 1) * ROW_H + 3
    local isTitle = row.key == nil
    if not isTitle then
      table.insert(elements, {
        type = "text", text = row.key,
        textFont = FONT, textSize = 14, textColor = PALETTE.ACTIVE_BG,
        textAlignment = "right", frame = { x = 8, y = ty, w = 40, h = 22 },
      })
    end
    -- The title is centred across the whole panel and the rows are not, so it
    -- gets its own frame rather than sharing the label column's.
    table.insert(elements, {
      type = "text", text = row.label,
      textFont = FONT, textSize = isTitle and 12 or 14,
      textColor = isTitle and PALETTE.OVERLAY_FG or PALETTE.FG,
      textAlignment = isTitle and "center" or "left",
      frame = isTitle and { x = 0, y = ty, w = W, h = 22 }
                       or { x = 58, y = ty, w = W - 66, h = 22 },
    })
  end

  overlay = hs.canvas.new({ x = x, y = y, w = W, h = H })
  overlay:appendElements(elements)
  -- screenSaver sits above everything, and AeroSpace does not treat a canvas
  -- at this level as a tileable window.
  overlay:level(hs.canvas.windowLevels.screenSaver)
  overlay:behavior(hs.canvas.windowBehaviors.canJoinAllSpaces)
  overlay:show()

  -- Centring is arithmetic, not calibration (see the design doc), and this
  -- return value is how that arithmetic gets checked from `hs -c`: the panel
  -- mid should equal the screen mid exactly, on whichever display is main.
  return string.format("mid=%d,%d screenMid=%d,%d",
    math.floor(x + W / 2), math.floor(y + H / 2),
    math.floor(ff.x + ff.w / 2), math.floor(ff.y + ff.h / 2))
end

function overlayHide()
  if overlay then
    overlay:delete()
    overlay = nil
  end
  return "hidden"
end

function modeChanged()
  local out = hs.execute(AEROSPACE .. " list-modes --current")
  -- Trim before comparing: the output carries a trailing newline.
  if (out or ""):gsub("%s+$", "") == "new" then
    overlayShow()
  else
    overlayHide()
  end
end

-- The layout toast Caps+M and Caps+/ raise. Those are `layout` commands, not
-- modes, so on-mode-changed never fires for them: each binding chains its own
-- trigger instead. A layout toggle also has no "exit" event, which is why this
-- one carries a timer where the Caps+N overlay does not.
-- The axis glyph is inverted from AeroSpace's own naming, which trips people up:
-- h_tiles means a HORIZONTAL arrangement, which on screen is windows side by
-- side, i.e. vertical divisions. So h gets the vertical bars.
local AXIS = {
  h = utf8.char(0x2016),  -- U+2016 DOUBLE VERTICAL LINE: side by side
  v = utf8.char(0x2630),  -- U+2630 TRIGRAM FOR HEAVEN: stacked
}

local LAYOUT_NAMES = {
  h_tiles     = "Tiles "     .. AXIS.h,
  v_tiles     = "Tiles "     .. AXIS.v,
  h_accordion = "Accordion " .. AXIS.h,
  v_accordion = "Accordion " .. AXIS.v,
}

local TOAST_W, TOAST_H, TOAST_SECS = 170, 34, 1.4
local toast, toastTimer = nil, nil

local function clearToast()
  if toastTimer then toastTimer:stop(); toastTimer = nil end
  if toast then toast:delete(); toast = nil end
end

function layoutToast()
  -- --workspace focused rather than --focused: the latter exits 2 on an empty
  -- workspace. All three layout placeholders agree while the tree stays flat,
  -- and nothing here binds join-with, so the root is the one Caps+M moves.
  local out = hs.execute(AEROSPACE ..
    " list-windows --workspace focused --format '%{workspace-root-container-layout}'")
  local layout = (out or ""):match("^%s*(%S+)")
  if not layout then return "no windows" end          -- nothing to report
  local text = LAYOUT_NAMES[layout] or layout

  clearToast()
  local ff = hs.screen.mainScreen():fullFrame()
  -- Bottom right, clear of the bar: 32px of bar plus its 2px margin, plus air.
  local x = ff.x + ff.w - TOAST_W - 12
  local y = ff.y + ff.h - TOAST_H - 46

  toast = hs.canvas.new({ x = x, y = y, w = TOAST_W, h = TOAST_H })
  toast:appendElements(
    { type = "rectangle", action = "strokeAndFill",
      fillColor = PALETTE.TOAST_BG, strokeColor = PALETTE.OVERLAY_FG, strokeWidth = 3,
      roundedRectRadii = { xRadius = 10, yRadius = 10 },
      frame = { x = 1.5, y = 1.5, w = TOAST_W - 3, h = TOAST_H - 3 } },
    { type = "text", text = text,
      textFont = FONT, textSize = 13, textColor = PALETTE.OVERLAY_FG,
      textAlignment = "center",
      frame = { x = 0, y = 8, w = TOAST_W, h = 20 } })
  toast:level(hs.canvas.windowLevels.screenSaver)
  toast:behavior(hs.canvas.windowBehaviors.canJoinAllSpaces)
  toast:show()

  toastTimer = hs.timer.doAfter(TOAST_SECS, clearToast)
  return string.format("%s at %d,%d", text, math.floor(x), math.floor(y))
end

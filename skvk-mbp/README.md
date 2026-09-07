# skvk-mbp

Personal macOS shell setup, applied with `mise bootstrap`. There are no install
scripts: `mise.toml` declares everything, and `tasks.toml` holds the one
procedural piece, the `verify` harness.

## Apply

```sh
mise trust .          # once; ~/repos/jtsoi is not in trusted_config_paths
mise bootstrap --dry-run
mise bootstrap
```

`mise run verify` applies the module into a throwaway `HOME` and asserts the
result, so it is safe to run at any time. The throwaway `HOME` isolates
writes, not reads: mise still reads the real `~/.config/mise/config.toml`,
which is why every run prints a `trusted_config_paths ... ignored for
security reasons` warning.

## The boundary

This machine is also provisioned by `~/repos/skvk/developer-machine`, which owns
`~/.zprofile` and the numbered fragments in `~/.sko/`. **This module never writes
to a path that repo owns:** `~/.zprofile`, `~/.sko/*`, `~/.config/direnv/*`,
`~/.config/git/ignore`, `~/.config/mise/config.toml`, `~/.config/mise/tasks/*`.

It owns `~/.zshrc`, `~/.zshrc.d/*`, `~/.config/starship.toml`, and
`~/.config/mise/conf.d/*.toml`.

The two layers need no coordination for *files*, because shell startup order
separates them: `.zprofile` → `.sko/*` runs first, `.zshrc` second.

**macOS defaults have no such ordering rule**, and one key is written by both
layers: `com.apple.dock autohide-delay`, which
`developer-machine/aerospace-macos-tweaks.sh` sets to `0` and this module sets
to `1000` so the Dock stays hidden instead of springing up when the cursor
reaches the bottom edge. Last writer wins, so re-running that script reverts it.
`mise bootstrap --dry-run` lists the key as pending whenever that has happened,
which is the only signal that the two disagree.

Personal mise tools go in `conf.d/`, not `config.toml`, because a fragment in
`~/.sko/` (`062-mise.sh` on this machine; newer provisioning ships it as
`998-mise.sh`) runs `mise settings jobs 1` on every shell start, rewriting
`config.toml`. `conf.d` takes `[tools]` only — `config.toml` wins on `[settings]`.

## Design

[docs/superpowers/specs/2026-09-06-skvk-mbp-dotfiles-design.md](../docs/superpowers/specs/2026-09-06-skvk-mbp-dotfiles-design.md)

## Window management

Caps Lock is remapped by Karabiner to `Ctrl+Opt+Cmd` — three modifiers, not the
usual four-modifier Hyper. That is deliberate: Hyper includes Shift, which would
make `Caps+Shift+Left` indistinguishable from `Caps+Left` and cost every
move-window binding.

Karabiner also swaps `fn` and Left Control, putting Control in the bottom-left
corner where Linux keeps it. macOS cannot do this itself — its Modifier Keys
panel has no row for `fn`.

Everything `fn` does moves one key to the right, onto the old Control position:
brightness and volume (`com.apple.keyboard.fnState` is 1, so F1-F12 are plain
function keys), forward delete, and Home/End/PgUp/PgDn. Karabiner performs the
F-row translation itself rather than leaving it to the keyboard firmware, which
is why a synthesised `fn` still reaches them. The `AppleFnUsageType` default in
`mise.toml` belongs to this swap rather than being a separate preference.

**Karabiner needs two manual steps before any of this works.** Its cask ships a
pkg that requires an interactive `sudo` password, so `mise bootstrap` cannot
install it unattended; run `brew install --cask karabiner-elements` from a
terminal. It then needs Input Monitoring granted in System Settings → Privacy &
Security. Until both are done Caps Lock stays an ordinary Caps Lock and none of
the bindings below reach AeroSpace.

Left and Right leave the workspace; everything else acts inside it.

The terminal is Alacritty, chosen because it ships no tabs and no splits:
AeroSpace already tiles, so a terminal that tiles too would be two window
managers fighting. `Caps+Enter` opens a window, mirroring `$mod+Return` in the
i3 config.

| keys | action |
|---|---|
| `Caps+Enter` | open an Alacritty window |
| `Caps+Left` / `Right` | previous / next workspace, wrapping at the ends |
| `Caps+Shift+Left` / `Right` | throw the window to the previous / next workspace |
| `Caps+Up` / `Down` | previous / next window in the accordion stack |
| `Caps+Shift+Up` / `Down` | move the window up / down the stack |
| `Caps+,` / `Caps+.` | previous / next window, under any layout |
| `Caps+Shift+,` / `.` | move the window left / right along a tiling row |
| `Caps+1..9`, `Caps+0/-/=` | switch to workspace 1-9, M, L, S |
| `Caps+Shift+<same>` | move the focused window to that workspace |
| `Caps+Tab` | jump back to the previously focused window |
| `Caps+Q` | close window |
| `Caps+F` | fullscreen |
| `Caps+M` | flip the workspace between side-by-side tiles and a full-width stack |
| `Caps+/` | flip that layout's axis: horizontal to vertical and back |
| `Caps+Space` | toggle the focused window between floating and tiled |

`Caps+,` / `Caps+.` are `focus dfs-prev` / `dfs-next` rather than
`focus left` / `right`, so one pair of keys means "previous and next window"
whatever the layout — along the tiling row on workspaces 1-3, and up and down
the accordion stack everywhere else.

Workspace next/prev walks all twelve persistent workspaces, empty ones
included. Skipping the empties needs an `eval` pipeline over
`list-workspaces --empty no`; jumping straight to a workspace by name is what
`Caps+1..9` is for.

Workspaces 1-3 are horizontal tiles, for terminals side by side; the rest are a
**vertical** accordion, so every window gets full width. Each workspace names
its layout explicitly (`h_tiles`, `v_accordion`), which keeps this independent
of `default-root-container-orientation`.

Those layouts are applied by `after-startup-command`, which runs only at
startup; `Caps+M` and `Caps+/` are how a workspace changes layout after that.
`Caps+M` names `h_tiles` and `v_accordion` outright, since those are the two
states this config declares, and `Caps+/` flips the axis of whichever is
current — so two unshifted keys reach all four layouts. Neither uses Shift,
because `ctrl-alt-cmd-shift-slash` never reached AeroSpace. Note that the
workspace named M is reached with `Caps+0`, not `Caps+M`.

AeroSpace's own `layout tiles horizontal vertical` cannot cover this in one
key: it applies the first layout in the list that differs from the current one,
so a list of three collapses into a two-cycle.

`aerospace list-workspaces --all --format '%{workspace} %{workspace-root-container-layout}'`
prints the live layout per workspace, which is worth knowing because a
workspace holding one window looks identical under all four.

AeroSpace installs from the `bootstrap` task rather than `[bootstrap.packages]`,
because it ships from `nikitabobko/tap`, which publishes no `api/cask` metadata
for mise's brew-cask backend to read.

## Rollback

`mise bootstrap` records what it applied, so the module removes cleanly:

```sh
mise bootstrap dotfiles unapply
```

This removes `~/.zshrc`, `~/.zshrc.d/*`, `~/.config/starship.toml`,
`~/.config/mise/conf.d/10-personal.toml`, `~/.aerospace.toml` and
`~/.config/karabiner/karabiner.json`, returning the machine to a bare shell
driven entirely by `~/.zprofile`. Brew packages and macOS defaults are not
reverted; remove them with `brew uninstall` and `defaults delete` if wanted.

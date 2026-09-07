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

The two layers need no coordination, because shell startup order separates them:
`.zprofile` → `.sko/*` runs first, `.zshrc` second.

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

**Karabiner needs two manual steps before any of this works.** Its cask ships a
pkg that requires an interactive `sudo` password, so `mise bootstrap` cannot
install it unattended; run `brew install --cask karabiner-elements` from a
terminal. It then needs Input Monitoring granted in System Settings → Privacy &
Security. Until both are done Caps Lock stays an ordinary Caps Lock and none of
the bindings below reach AeroSpace.

| keys | action |
|---|---|
| `Caps+1..9`, `Caps+0/-/=` | switch to workspace 1-9, M, L, S |
| `Caps+Shift+<same>` | move the focused window to that workspace |
| `Caps+arrows` | focus directionally; on accordion workspaces Up/Down walks the window stack |
| `Caps+Shift+arrows` | move the window |
| `Caps+Tab` | jump back to the previously focused window |
| `Caps+Q` | close window |
| `Caps+F` | fullscreen |

Workspaces 1-3 tile, for terminals side by side. The rest use a **vertical**
accordion, so every window gets full width and `Caps+Up`/`Caps+Down` walks the
stack. The vertical orientation is load-bearing — a horizontal accordion would
put stack-walking on Left/Right, where the tiling workspaces need those keys.

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

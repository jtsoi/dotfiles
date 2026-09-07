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

## Rollback

`mise bootstrap` records what it applied, so the module removes cleanly:

```sh
mise bootstrap dotfiles unapply
```

This removes `~/.zshrc`, `~/.zshrc.d/*`, `~/.config/starship.toml` and
`~/.config/mise/conf.d/10-personal.toml`, returning the machine to a bare shell
driven entirely by `~/.zprofile`. Brew packages and macOS defaults are not
reverted; remove them with `brew uninstall` and `defaults delete` if wanted.

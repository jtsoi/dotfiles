# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Personal dotfiles for Linux (Debian/Ubuntu/Pop!_OS) and macOS (MBP) environments.

The two platforms use **different architectures**, and which one applies depends
entirely on where you are working:

| path | platform | style |
|---|---|---|
| `modules/` | Linux | imperative shell modules |
| `skvk-mbp/` | macOS | declarative, one `mise.toml` |

Do not carry conventions from one into the other.

## macOS — `skvk-mbp/`

One `mise.toml` consumed by `mise bootstrap`. There are no install scripts, no
`lib/` helpers and no directory numbering: `[dotfiles]` symlinks config into
`$HOME`, `[bootstrap.packages]` installs brew formulae, and
`[bootstrap.macos.defaults]` replaces `defaults write` calls. `tasks.toml` holds
the one procedural piece, the `verify` harness.

```sh
cd skvk-mbp
mise trust .              # once — ~/repos/jtsoi is not in trusted_config_paths
mise bootstrap --dry-run
mise bootstrap            # note: no `apply` subcommand at the top level
mise run verify           # applies into a throwaway HOME and asserts the result
```

`mise bootstrap` converges, so re-running is safe, and
`mise bootstrap dotfiles unapply` backs the whole module out.

### The ownership boundary — read before editing anything here

This Mac is **also** provisioned by `~/repos/skvk/developer-machine` (work),
which owns `~/.zprofile` and the numbered shell fragments in `~/.sko/`. That
layer installs brew, mise, direnv and fnox, and runs `compinit`.

**`skvk-mbp/` must never write to a path that repo owns:** `~/.zprofile`,
`~/.sko/*`, `~/.config/direnv/*`, `~/.config/git/ignore`,
`~/.config/mise/config.toml`, `~/.config/mise/tasks/*`.

It owns `~/.zshrc`, `~/.zshrc.d/*`, `~/.config/starship.toml` and
`~/.config/mise/conf.d/*.toml`.

The two layers need no coordination because shell startup order separates them:
`.zprofile` → `.sko/*` runs first, `.zshrc` second. Personal settings win on
overlap without editing a work-owned file.

Two consequences that are easy to get wrong:

- **Personal global mise tools go in `conf.d/`, never `config.toml`.** A `~/.sko/`
  fragment runs `mise settings jobs 1` on every shell start, rewriting
  `config.toml`. `conf.d` merges `[tools]` but **loses** to `config.toml` on
  `[settings]`, so a settings key there is silently ignored.
- **Never add `[bootstrap.mise_shell_activate]`.** Work already activates mise,
  and that phase writes into zsh *profile* files, which are work-owned.

`skvk-mbp/README.md` covers the same ground for a human reader.

## Linux — `modules/`

Modules live in `modules/`, numbered by execution order (e.g. `01-system-tools`,
`13-zsh`). Each is a self-contained directory with an `install.sh` that:

1. Sources `../../lib/dot.sh` to get shared path variables and load `.env`
2. Uses `dot_symlink` / `dot_curl_download` helpers from `lib/files.sh`
3. Manages its own configuration files, usually stored in `files/` and symlinked to `$HOME`

**Key variables set by `lib/dot.sh`:**
- `DOT_DIR` — repo root (resolved by splitting path on `dotfiles`)
- `DOT_MODULE_FILES_DIR` — `files/` subdirectory of the running module
- `ZSHRC_D_DIR` — `~/.zshrc.d/` where shell hook files are dropped

Each module's `install.sh` is run directly; there is no central install script:

```sh
cd modules/13-zsh && sh install.sh
```

### Configuration files convention

- Files prefixed with `dot_` in `modules/*/files/` get symlinked to `~` (e.g. `dot_zshrc` → `~/.zshrc`)
- Shell hook files (e.g. `13-direnv-hook.zsh`, `31-pyenv-hook.zsh`) are placed in `~/.zshrc.d/` and sourced by `~/.zshrc`

`lib/` and `modules/` are Linux-only. `skvk-mbp/` does not use them.

### Adding a Linux module

1. Create `modules/<NN>-name/` (pick a number that reflects priority/order)
2. Write `install.sh` starting with `. ../../lib/dot.sh`
3. Place config files in `modules/<NN>-name/files/` with `dot_` prefix if they symlink to `$HOME`

## Environment Variables

Linux modules expect a `.env` file at the repo root (gitignored). Commonly used
variables include `GIT_USER_NAME` and `GIT_USER_EMAIL`. `lib/dot.sh` loads this
file automatically via `eval`.

## Git Commits

Do not add Claude attribution (`Co-Authored-By`) to commits.

Planning and design documents under `docs/` are deliberately gitignored — they
are working notes, not repository content.

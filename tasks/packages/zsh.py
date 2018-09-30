
from tasks import dotfiles, files
from tasks.packages import apt


HOME = files.resolve_path('~/')
BASH_ALIASES = files.resolve_path('~/.bash_aliases')

PREZTO_DIR = files.resolve_path('~/.zprezto')
PREZTO_CONFIG = files.resolve_path('~/.zpreztorc')
PREZTO_SYMLINKS = [
    'zlogin',
    'zlogout',
    'zpreztorc',
    'zprofile',
    'zshenv',
    'zshrc'
]


def build(c):
    apt.install(c, 'zsh')
    if not files.exists(c, PREZTO_DIR):
        c.run(f'git clone --recursive https://github.com/sorin-ionescu/prezto.git {PREZTO_DIR}')
    with c.cd(str(PREZTO_DIR)):
        c.run('git pull && git submodule update --init --recursive')
    configure(c)


def configure(c):
    for link in PREZTO_SYMLINKS:
        target_path = HOME / f'.{link}'
        files.remove(c, target_path)
        files.symlink(c, PREZTO_DIR / 'runcoms' / link, target_path)

    dotfiles.link(c, 'files/zsh/zpreztorc', PREZTO_CONFIG)
    dotfiles.link(c, 'files/zsh/bash_aliases', BASH_ALIASES)

    c.run('chsh -s /usr/bin/zsh')


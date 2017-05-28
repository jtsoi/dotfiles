from os import path
from fabric.api import env, run, cd
from tasks import dotfiles, util
from tasks.packages import yaourt
from fabtools import files, require

HOME = util.full_path('~/')
PREZTO_DIR = util.full_path('~/.zprezto')
PREZTO_CONFIG = util.full_path('~/.zpreztorc')
PREZTO_SYMLINKS = [
    'zlogin',
    'zlogout',
    'zpreztorc',
    'zprofile',
    'zshenv',
    'zshrc'
]


def install():
    yaourt.install('zsh fasd')
    configure()


def configure():
    if not files.exists(PREZTO_DIR):
        run('git clone --recursive https://github.com/sorin-ionescu/prezto.git {}'.format(PREZTO_DIR))
    with cd(PREZTO_DIR):
        run('git pull && git submodule update --init --recursive')
    for link in PREZTO_SYMLINKS:
        target_path = path.join(HOME, '.{}'.format(link))
        files.remove(target_path)
        files.symlink(path.join(PREZTO_DIR, 'runcoms', link), target_path)
    dotfiles.link('files/zsh/zpreztorc', PREZTO_CONFIG)
    run('chsh -s /usr/bin/zsh')

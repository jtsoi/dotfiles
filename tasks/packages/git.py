from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files


GIT_CONFIG = '~/.gitconfig'
GIT_PACKAGES = [
    'tk',
    'git',
    'tig',
    'aspell-en'
]


def install():
    yaourt.install(' '.join(GIT_PACKAGES))
    configure()


def configure():
    dotfiles.link('files/git/gitconfig', GIT_CONFIG)

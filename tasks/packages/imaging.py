from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files


PACKAGES = [
    'pinta',
    'inkscape',
    'maim',
    'feh'
]


def install():
    #yaourt.remove('gimp')
    yaourt.install(' '.join(PACKAGES))
    configure()


def configure():
    pass

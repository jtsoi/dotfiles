from os import path
from fabric.api import env, run, cd
from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files, require

XRESOURCES_CONFIG = path.abspath(path.expanduser('~/.extend.Xresources'))
XINITRC_CONFIG = path.abspath(path.expanduser('~/.extend.xinitrc'))
XMODMAP_CONFIG = path.abspath(path.expanduser('~/.Xmodmap'))
I3_CONFIG = path.abspath(path.expanduser('~/.i3/config'))
MORC_MENU_CONFIG = path.abspath(path.expanduser('~/.config/morc_menu/morc_menu_v1.conf'))

PACKAGES = [
    'rofi',
    'ttf-font-awesome',
    #'i3blocks',
]


def install():
    yaourt.install(' '.join(PACKAGES))
    configure()


def configure():
    dotfiles.link('files/i3wm/extend.Xresources', XRESOURCES_CONFIG)
    dotfiles.link('files/i3wm/extend.xinitrc', XINITRC_CONFIG)
    dotfiles.link('files/i3wm/Xmodmap', XINITRC_CONFIG)
    dotfiles.link('files/i3wm/config', I3_CONFIG)
    dotfiles.link('files/i3wm/morc_menu_v1.conf', MORC_MENU_CONFIG)

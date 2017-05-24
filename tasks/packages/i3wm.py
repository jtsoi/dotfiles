from os import path
from fabric.api import env, run, cd
from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files, require

XRESOURCES_CONFIG = path.abspath(path.expanduser('~/.extend.Xresources'))
XINITRC_CONFIG = path.abspath(path.expanduser('~/.extend.xinitrc'))
I3_CONFIG = path.abspath(path.expanduser('~/.i3/config'))
MORC_MENU_CONFIG = path.abspath(path.expanduser('~/.config/morc_menu/morc_menu_v1.conf'))


def install():
    #yaourt.install('rofi ttf-font-awesome')
    configure()


def configure():
    dotfiles.link('files/i3wm/extend.Xresources', XRESOURCES_CONFIG)
    dotfiles.link('files/i3wm/extend.xinitrc', XINITRC_CONFIG)
    dotfiles.link('files/i3wm/config', I3_CONFIG)
    dotfiles.link('files/i3wm/morc_menu_v1.conf', MORC_MENU_CONFIG)

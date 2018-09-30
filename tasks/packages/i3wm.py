# from os import path
# from fabric.api import env, run, cd
# from tasks import dotfiles, util
# from tasks.packages import yaourt
# from fabtools import files, require

# XRESOURCES_CONFIG = util.full_path('~/.extend.Xresources')
# XINITRC_CONFIG = util.full_path('~/.extend.xinitrc')
# XMODMAP_CONFIG = util.full_path('~/.Xmodmap')
# I3_CONFIG = util.full_path('~/.i3/i3config.gaps.old')
# PY3STATUS_CONFIG = util.full_path('~/.i3/py3status.conf')
# MORC_MENU_CONFIG = util.full_path('~/.i3config.gaps.old/morc_menu/morc_menu_v1.conf')
# COMPTON_CONFIG = util.full_path('~/.i3config.gaps.old/compton.conf')
from tasks import apt

PACKAGES = [
    'rofi',
    'ttf-font-awesome',
    'py3status',
]


def build(c):
    apt.install(c, 'i3')



# def configure():
#     dotfiles.link('files/i3wm/extend.Xresources', XRESOURCES_CONFIG)
#     dotfiles.link('files/i3wm/extend.xinitrc', XINITRC_CONFIG)
#     dotfiles.link('files/i3wm/Xmodmap', XINITRC_CONFIG)
#     dotfiles.link('files/i3wm/i3config.gaps.old', I3_CONFIG)
#     dotfiles.link('files/i3wm/py3status.conf', PY3STATUS_CONFIG)
#     dotfiles.link('files/i3wm/morc_menu_v1.conf', MORC_MENU_CONFIG)
#     dotfiles.link('files/i3wm/compton.conf', COMPTON_CONFIG)

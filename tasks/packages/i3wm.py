from tasks import dotfiles, apt, files


# XRESOURCES_CONFIG = util.full_path('~/.extend.Xresources')
# XINITRC_CONFIG = util.full_path('~/.extend.xinitrc')
# XMODMAP_CONFIG = util.full_path('~/.Xmodmap')
# I3_CONFIG = util.full_path('~/.i3/i3config.gaps.old')
# PY3STATUS_CONFIG = util.full_path('~/.i3/py3status.conf')
# MORC_MENU_CONFIG = util.full_path('~/.i3config.gaps.old/morc_menu/morc_menu_v1.conf')
# COMPTON_CONFIG = util.full_path('~/.i3config.gaps.old/compton.conf')

PACKAGES = [
    'rofi',
    'ttf-font-awesome',
    'py3status',
]


def build(c):
    i3(c)
    #themes(c)
    #fonts(c)


def i3(c):
    apt.install(c, 'i3 i3blocks')
    dotfiles.link(c, 'files/i3wm/i3config', files.resolve_path('~/.config/i3/config'), c.config.dot.i3wm)
    dotfiles.link(c, 'files/i3wm/i3blocks', files.resolve_path('~/.config/i3blocks/config'), c.config.dot.i3wm)


def themes(c):
    apt.add_ppa(c, 'ppa:noobslab/themes')
    apt.add_ppa(c, 'ppa:noobslab/icons')

    #apt.install(c, 'arc-theme arc-icons')
    apt.install(c, 'matcha-theme matcha-icons')
    #apt.install(c, 'plane-theme plane-icons') < this for now


def fonts(c):
    apt.install(c, 'ttf-mscorefonts-installer')



# def configure():
#     dotfiles.link('files/i3wm/extend.Xresources', XRESOURCES_CONFIG)
#     dotfiles.link('files/i3wm/extend.xinitrc', XINITRC_CONFIG)
#     dotfiles.link('files/i3wm/Xmodmap', XINITRC_CONFIG)
#     dotfiles.link('files/i3wm/i3config.gaps.old', I3_CONFIG)
#     dotfiles.link('files/i3wm/py3status.conf', PY3STATUS_CONFIG)
#     dotfiles.link('files/i3wm/morc_menu_v1.conf', MORC_MENU_CONFIG)
#     dotfiles.link('files/i3wm/compton.conf', COMPTON_CONFIG)

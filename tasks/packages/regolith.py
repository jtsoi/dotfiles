"""
See how to config Regolith:
https://regolith-linux.org/configure.html
"""
from patchwork.files import directory

from tasks import dotfiles


def build(c):
    i3conf(c)


def i3conf(c):
    directory(c, '~/.config/regolith/i3')
    dotfiles.link(c, 'files/regolith/i3config', '~/.config/regolith/i3/config', context=c.config.dot)

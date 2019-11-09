"""
See how to config Regolith:
https://regolith-linux.org/configure.html
"""
from patchwork.files import directory

from tasks import dotfiles
from tasks import apt


def build(c):
    #base(c)
    # fonts(c)
    polybar(c)
    i3conf(c)


def base(c):
    apt.add_ppa(c, 'ppa:kgilmer/speed-ricer')


def fonts(c):
    # enable bitmap fonts

    c.sudo('mv -f /etc/fonts/conf.d/70-no-bitmaps.conf /etc/fonts/conf.d/70-no-bitmaps.conf.old', pty=True, warn=True)

    # Polybar siji font
    c.run('cd /tmp/ && rm -rf siji && git clone https://github.com/stark/siji && cd siji && ./install.sh',  pty=True)

    # Polybar unifont
    apt.install(c, 'xfonts-unifont')


def i3conf(c):
    directory(c, '~/.config/regolith/i3')
    dotfiles.link(c, 'files/regolith/i3config', '~/.config/regolith/i3/config', context=c.config.dot)
    dotfiles.link(c, 'files/regolith/i3xrocks', '~/.config/regolith/i3/i3xrocks', context=c.config.dot)


def polybar(c):
    # Manual step
    # Download and install font-awesome pro files.
    # Open the otf files in th GUI and click install.

    #apt.install(c, 'polybar yad xdotool')
    dotfiles.link(c, 'files/regolith/polybar/config', '~/.config/regolith/polybar/config', context=c.config.dot)
    dotfiles.link(c, 'files/regolith/polybar/launch-polybar.sh', '~/.config/regolith/polybar/launch-polybar.sh', context=c.config.dot)
    dotfiles.link(c, 'files/regolith/polybar/popup-calendar.sh', '~/.config/regolith/polybar/popup-calendar.sh', context=c.config.dot)
    c.run('chmod +x ~/.config/regolith/polybar/*.sh', pty=True)


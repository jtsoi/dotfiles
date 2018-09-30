from tasks import dotfiles
from tasks.packages import apt


def build(c):
    lxterminal(c)
    sublime_merge(c)


def lxterminal(c):
    # LXTerminal
    dotfiles.link(c, 'files/lxterminal/lxterminal.conf', '~/.config/lxterminal/lxterminal.conf')


def sublime_merge(c):
    c.sudo('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -', pty=True)
    c.sudo('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list', pty=True)
    apt.update(c)
    apt.install(c, 'sublime-merge')
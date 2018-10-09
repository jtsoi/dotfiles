from tasks import dotfiles, apt, files, snap


def build(c):
    print('Building desktop')
    bitwarden(c)
    spotify(c)
    slack(c)

#    lxterminal(c)
#    chrome(c)
#    mc(c)


def lxterminal(c):
    # LXTerminal
    dotfiles.link(c, 'files/lxterminal/lxterminal.conf', '~/.config/lxterminal/lxterminal.conf')


def chrome(c):
    c.sudo('wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -', pty=True)
    c.sudo('echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list', pty=True)
    apt.update(c)
    apt.install(c, 'google-chrome-stable')


def mc(c):
    apt.install(c, 'mc')
    dotfiles.link(c, files.resolve_path('files/mc/solarized.ini'), files.resolve_path('~/.mc/solarized.ini'))
    dotfiles.link(c, files.resolve_path('files/mc/100_zshrc_mc.zsh'), files.resolve_path('~/.zshrc.d/100_zshrc_mc.zsh'))


def bitwarden(c):
    snap.install(c, 'bitwarden')


def spotify(c):
    snap.install(c, 'spotify')


def slack(c):
    snap.install(c, 'slack', classic=True)
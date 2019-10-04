from tasks import dotfiles, apt, files, snap


def build(c):
    print('Building desktop')
    #bitwarden(c)
    #spotify(c)
    chrome(c)

    # slack(c)
    #lxterminal(c)
    # mc(c)


def lxterminal(c):
    # LXTerminal
    apt.install(c, 'lxterminal')
    dotfiles.link(c, 'files/lxterminal/lxterminal.conf', '~/.config/lxterminal/lxterminal.conf')


def chrome(c):
    #c.sudo('bash -c "cd /tmp && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && dpkg -i google-chrome-stable_current_amd64.deb"', pty=True)
    dotfiles.link(c, files.resolve_path('files/chrome/chrome-nulltales.desktop'), files.resolve_path('~/.local/share/applications/chrome-nulltales.desktop'))
    dotfiles.link(c, files.resolve_path('files/chrome/chrome-private.desktop'), files.resolve_path('~/.local/share/applications/chrome-private.desktop'))


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

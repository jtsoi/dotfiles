from invoke import task

from tasks import dotfiles, apt, files, snap


@task
def lxterminal(c):
    # LXTerminal
    apt.install(c, 'lxterminal')


@task
def lxterminal_conf(c):
    dotfiles.link(c, 'files/lxterminal/lxterminal.conf', '~/.config/lxterminal/lxterminal.conf')


@task
def mc(c):
    apt.install(c, 'mc')
    dotfiles.link(c, files.resolve_path('files/mc/solarized.ini'), files.resolve_path('~/.mc/solarized.ini'))
    dotfiles.link(c, files.resolve_path('files/mc/100_zshrc_mc.zsh'), files.resolve_path('~/.zshrc.d/100_zshrc_mc.zsh'))


@task
def bitwarden(c):
    snap.install(c, 'bitwarden')


@task
def pinta(c):
    # Runs Mono, do you really need pinta?
    apt.install(c, 'pinta')


@task
def keybase(c):
    files.curl_download(c, 'https://prerelease.keybase.io/keybase_amd64.deb', '/tmp/keybase_amd64.deb')
    apt.install(c, '/tmp/keybase_amd64.deb')
    c.run('run_keybase -g')

from invoke import task

from tasks import dotfiles, apt, files, snap, machine


@task
def chrome(c):
    c.sudo('bash -c "cd /tmp && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && dpkg -i google-chrome-stable_current_amd64.deb"', pty=True)


@task
def chrome_conf(c):
    dotfiles.link(c, files.resolve_path('files/chrome/chrome-nulltales.desktop'), files.resolve_path('~/.local/share/applications/chrome-nulltales.desktop'))
    dotfiles.link(c, files.resolve_path('files/chrome/chrome-private.desktop'), files.resolve_path('~/.local/share/applications/chrome-private.desktop'))
    dotfiles.link(c, files.resolve_path('files/chrome/chrome-horizon.desktop'), files.resolve_path('~/.local/share/applications/chrome-horizon.desktop'))
    dotfiles.link(c, files.resolve_path('files/chrome/chrome-skovik.desktop'), files.resolve_path('~/.local/share/applications/chrome-skovik.desktop'))

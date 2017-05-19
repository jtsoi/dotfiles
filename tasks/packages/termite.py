from os import path

from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files, require

TERMITE_CONFIG = '~/.config/termite/config'


def install():
    yaourt.install('termite')
    configure()


def configure():
    files.remove('/usr/bin/terminal', use_sudo=True)
    files.upload_template(
        'files/termite/terminal',
        '/usr/bin/terminal',
        use_sudo=True,
        mode='0755',
        chown=True,
        user='root'
    )
    dotfiles.link('files/termite/config', TERMITE_CONFIG)

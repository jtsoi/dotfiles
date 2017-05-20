from os import path
from fabric.api import env
from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files, require

SSH_CONFIG = path.abspath(path.expanduser('~/.ssh/config'))


def install():
    yaourt.install('keychain')
    configure()


def configure():
    require.files.directory(path.dirname(SSH_CONFIG), mode=755)
    dotfiles.link('files/ssh/config', SSH_CONFIG)
    require.files.file(SSH_CONFIG, mode=600)

    for name, key in env.vars.ssh.key_files.items():
        private_key_path = path.abspath(path.expanduser('~/.ssh/{}'.format(name)))
        public_key_path = path.abspath(path.expanduser('~/.ssh/{}.pub'.format(name)))
        require.files.file(private_key_path, contents=key.private, mode=600)
        require.files.file(public_key_path, contents=key.public, mode=644)

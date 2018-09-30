
from tasks import dotfiles, files, local
from tasks.packages import apt

SSH_CONFIG = files.resolve_path('~/.ssh/config')


def build(c):
    apt.install(c, 'keychain ssh-askpass')
    configure(c)


def configure(c):
    files.directory(c, SSH_CONFIG.parent, mode=755)
    dotfiles.link(c, 'files/ssh/config', SSH_CONFIG)
    files.chmod(c, 600, SSH_CONFIG)

    for name, key in c.config.dot.ssh.key_files.items():
        private_key_path = files.resolve_path(f'~/.ssh/{name}')
        public_key_path = files.resolve_path(f'~/.ssh/{name}.pub')

        local.content(c, key['private'], private_key_path)
        files.chmod(c, 600, private_key_path)
        local.content(c, key['public'], public_key_path)
        files.chmod(c, 644, public_key_path)

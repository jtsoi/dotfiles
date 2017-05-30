from tasks import dotfiles
from tasks.packages import yaourt
from fabtools import files
from fabric.api import sudo, env


PACKAGES = [
    'docker',
    'docker-compose',
]


def install():
    yaourt.install(' '.join(PACKAGES))
    configure()


def configure():
    # Add user to docker group
    sudo('systemctl enable docker')
    sudo('groupadd -f docker')
    sudo('usermod -aG docker {}'.format(env.vars.user))

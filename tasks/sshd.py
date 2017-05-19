from contextlib import contextmanager

from fabric.api import sudo, run, local


def start_sshd():
    local('sudo systemctl start sshd')


def stop_sshd():
    local('sudo systemctl stop sshd')
    local('sudo systemctl disable sshd')


@contextmanager
def sshd():
    try:
        start_sshd()
        yield
    finally:
        stop_sshd()

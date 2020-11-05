from pathlib import Path
from patchwork.files import (
    exists,
    directory
)


def resolve_path(path):
    return Path(path).expanduser().absolute()


def remove(c, target):
    return c.run(f'rm -rf {target}')


def copy(c, source_path, target_path, chmod=None):
    result = c.run(f'cp {source_path} {target_path}')
    if chmod:
        c.run(f'chmod {chmod} {target_path}')
    return result


def symlink(c, source_path, target_path):
    return c.run(f'ln -s {source_path} {target_path}')


def chmod(c, mode, path):
    return c.run(f'chmod {mode} {Path(path)}')


def curl_download(c, from_url, to_path, sudo=True):
    cmd = f'curl --location {from_url} --output {to_path}'
    if sudo:
        return c.sudo(cmd, pty=True)
    return c.run(cmd, pty=True)


def wget_download(c, from_url, to_path, sudo=True):
    cmd = 'wget ' \
        '--quiet ' \
        f'--output-document={to_path} ' \
        f'{from_url}'
    if sudo:
        return c.sudo(cmd, pty=True)
    return c.run(cmd, pty=True)
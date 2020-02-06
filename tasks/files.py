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
    if sudo:
        return c.sudo(f'curl -L {from_url} -o {to_path}', pty=True)
    return c.run(f'curl -L {from_url} -o {to_path}', pty=True)


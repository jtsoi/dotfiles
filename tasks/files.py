from pathlib import Path
from patchwork.files import (
    exists,
    directory
)


def resolve_path(path):
    return Path(path).expanduser().absolute()


def remove(c, target):
    return c.run(f'rm -rf {target}')


def symlink(c, source_path, target_path):
    return c.run(f'ln -s {source_path} {target_path}')


def chmod(c, mode, path):
    return c.run(f'chmod {mode} {Path(path)}')
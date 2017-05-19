from fabric.api import env
from fabric.contrib.files import upload_template
from fabtools import files, require
from os import path

DOTFILES_TEMPLATES_DIR = path.abspath('files')
DOTFILES_STORAGE_DIR = path.abspath(path.expanduser('~/.dotfiles/'))


def link(source, target):
    """
    Copy the dotfile to ~/.dotfiles/
    Create a dotfile link from ~/.dotfiles/
    Ensure dir exists and rm any existing file before linking.
    :param source: 
    :param target: 
    :param use_sudo: 
    :return: 
    """

    source_rel = path.relpath(path.abspath(source), DOTFILES_TEMPLATES_DIR)
    storage = path.abspath(path.join(DOTFILES_STORAGE_DIR, source_rel))
    target = path.abspath(path.expanduser(target))
    target_dir = path.dirname(target)
    storage_dir = path.dirname(storage)

    require.files.directory(storage_dir)
    require.files.directory(target_dir)
    upload_template(
        source,
        storage,
        context=env.vars,
        use_jinja=True,
        keep_trailing_newline=True
    )
    if files.exists(target):
        files.remove(target)
    files.symlink(storage, target)

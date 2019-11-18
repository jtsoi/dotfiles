from tasks import files, local

DOTFILES_TEMPLATES_DIR = files.resolve_path('files')
DOTFILES_STORAGE_DIR = files.resolve_path('~/.dotfiles/')


def link(c, source, target, context=None):
    """
    Copy the dotfile to ~/.dotfiles/
    Create a dotfile link from ~/.dotfiles/
    Ensure dir exists and rm any existing file before linking.
    :param source: 
    :param target:
    :return: 
    """

    source_rel = files.resolve_path(source).relative_to(DOTFILES_TEMPLATES_DIR)
    storage = DOTFILES_STORAGE_DIR / source_rel
    target = files.resolve_path(target)
    target_dir = target.parent
    storage_dir = storage.parent

    files.directory(c, storage_dir)
    files.directory(c, target_dir)

    local.template(c, source, storage, context=context or {})

    if files.exists(c, target):
        files.remove(c, target)
    files.symlink(c, storage, target)


def copy(c, source, target, context=None):
    """
    Copy the dotfile to target

    Ensure dir exists and rm any existing file before copying.
    :param source:
    :param target:
    :return:
    """
    target = files.resolve_path(target)
    target_dir = target.parent

    files.directory(c, target_dir)

    if files.exists(c, target):
        files.remove(c, target)

    local.template(c, source, target, context=context or {})

from pathlib import Path

from invoke import task

from tasks import apt, snap, files, dotfiles


@task
def git(c):
    apt.install(c, 'git aspell-en')


@task
def git_conf(c):
    for directory, dir_settings in c.config.dot.code_dirs.items():
        dir_path = Path('~/Code/') / directory
        files.directory(c, dir_path)
        print(f"Created {dir_path}")
        dotfiles.copy(c, 'files/git/gitconfig_project_template', dir_path / '.gitconfig', context=dir_settings)

    dotfiles.link(c, 'files/git/gitconfig', '~/.gitconfig', context=c.config.dot)


@task
def autosrc(c):

    dotfiles.link(c, 'files/code/zshrcd/autosrc.zsh', files.resolve_path('~/.zshrc.d/autosrc.zsh'))

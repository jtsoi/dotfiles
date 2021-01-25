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
    dotfiles.link(c, 'files/git/global-gitignore', '~/.gitignore', context=c.config.dot)


# Autoenv seems quite broken.
# Should really use direnv or similar
# @task
# def autoenv(c):
#     files.curl_download(c, 'https://github.com/inishchith/autoenv/archive/master.`1zip', '/tmp/autoenv.zip')
#     c.run('mkdir -p ~/.autoenv')
#     c.run('unzip -o -j /tmp/autoenv.zip autoenv-master/activate.sh -d ~/.autoenv/')
#
#
# @task
# def autoenv_conf(c):
#     dotfiles.link(c, 'files/code/zshrcd/32-autoenv.zsh', files.resolve_path('~/.zshrc.d/32-autoenv.zsh'), jinja=False)


# Use autosrc so far until I can debug direnv
# Direnv has issues with invoke cmd line complete
@task
def autosrc(c):

    dotfiles.link(c, 'files/code/zshrcd/31-autosrc.zsh', files.resolve_path('~/.zshrc.d/31-autosrc.zsh'), jinja=False)


@task
def direnv(c):
    apt.install(c, 'direnv')

@task
def direnv_conf(c):
    dotfiles.link(c, 'files/code/zshrcd/30-direnv-hook.zsh', files.resolve_path('~/.zshrc.d/30-direnv-hook.zsh'), jinja=False)
    dotfiles.link(c, 'files/code/direnvrc', files.resolve_path('~/.direnvrc'), jinja=False)


from tasks import dotfiles
from tasks.packages import apt

GIT_CONFIG = '~/.gitconfig'


def build(c):
    apt.install('git aspell-en')
    configure(c)


def configure(c):
    dotfiles.link(c, 'files/git/gitconfig', GIT_CONFIG, context=c.config.dot)

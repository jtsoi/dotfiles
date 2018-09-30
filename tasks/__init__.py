from invoke import task

from tasks import files
from tasks.packages import (
    snap,
    apt,
    editors,
    i3wm,
    desktop,
    zsh,
    ssh,
    git)


@task
def build(c):
    print("Building!")
    #apt.update(c)
    #snap.build(c)
    #editors.build(c)
    #i3wm.build(c)

    desktop.build(c)
    #zsh.build(c)
    #ssh.build(c)
    #git.build(c)

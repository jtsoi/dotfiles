from invoke import task

from tasks import files, apt, snap
from tasks.packages import (
    system,
    editors,
    i3wm,
    desktop,
    sdk)


@task
def build(c):
    print("Building!")
    #system.build(c)

    #desktop.build(c)
    editors.build(c)
    #sdk.build(c)


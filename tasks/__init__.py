from invoke import task

from tasks import files, apt, snap
from tasks.packages import (
    system,
    editors,
    i3wm,
    desktop,
    sdk,
    media,
    thinkpad,
    utils,
    regolith)


@task
def build(c):
    print("Building!")
    #system.build(c)
    regolith.build(c)
    #utils.build(c)
    desktop.build(c)
    media.build(c)
    #editors.build(c)
    #sdk.build(c)
    #thinkpad.build(c)


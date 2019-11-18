from os import environ

from invoke import Collection

from tasks import files, apt, snap, machine
from tasks.packages import (
    system,
    editors,
    desktop,
    browsers,
    messaging,
    sdk,
    code,
    media,
    thinkpad,
    utils,
    regolith)


ns = Collection(
    system,
    regolith,
    browsers,
    messaging,
    editors,
    desktop,
    sdk,
    media,
    thinkpad,
    utils,
    code
)
ns.configure(dict(machine=dict(is_thinkpad=machine.is_thinkpad())))

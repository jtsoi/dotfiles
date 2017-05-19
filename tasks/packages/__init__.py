from fabric.api import run, sudo

from tasks.packages import termite, fonts, thinkpad
from tasks.packages import git


def install():
    #fonts.install()
    #termite.install()
    #git.install()
    thinkpad.install()

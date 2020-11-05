import addict
from invoke import task

from tasks import snap, dotfiles, apt, files, local

SLICER_VERSION = '2_3_0'


@task
def slicer(c):
    files.directory(c, '~/Prusa/Gcode')
    files.curl_download(c,
                        f'https://cdn.prusa3d.com/downloads/drivers/prusa3d_linux_{SLICER_VERSION}.zip',
                        '~/Prusa/prusa3d_slicer.zip')
    with c.cd('~/Prusa/'):
        c.run('unzip -o prusa3d_slicer.zip')
        c.run('mv PrusaSlicer* prusa3d_slicer.AppImage')
        c.run('chmod +x prusa3d_slicer.AppImage')

    dotfiles.link(c, files.resolve_path('files/prusa/prusa-slicer.desktop'), files.resolve_path('~/.local/share/applications/prusa-slicer.desktop'))


@task
def openscad(c):
    apt.install(c, 'openscad')\


@task
def freecad(c):
    apt.add_ppa(c, 'ppa:freecad-maintainers/freecad-stable')
    apt.install(c, 'freecad')

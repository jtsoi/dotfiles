import addict
from invoke import task

from tasks import snap, dotfiles, apt, files, local


@task
def wireguard(c):
    apt.install(c, 'wireguard resolvconf net-tools')


@task
def wireguard_conf(c):

    WG_TMP_PATH = files.resolve_path('/tmp/wireguard/')
    WG_CONF_PATH = files.resolve_path('/etc/wireguard/')

    files.directory(c, WG_TMP_PATH)

    for iface in c.config.dot.wireguard.interfaces:
        iface = addict.Dict(iface)
        iface_tmp_file_path = WG_TMP_PATH / f'{iface.name}.conf'
        iface_conf_file_path = WG_CONF_PATH / f'{iface.name}.conf'

        iface.client_private_key = c.config.dot.wireguard.client_private_key
        local.template(c, 'files/wireguard/iface-template.conf.j2', iface_tmp_file_path, context=iface)

        c.sudo(f'mv {iface_tmp_file_path} {iface_conf_file_path}')
        c.sudo(f'chmod 600 {iface_conf_file_path}')
        c.sudo(f'chown root:root {iface_conf_file_path}')

    # Run: 'sudo wg-quick up skovik-develop'
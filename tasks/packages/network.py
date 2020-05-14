import addict
from invoke import task

from tasks import snap, dotfiles, apt, files, local

@task
def dnsmasq_conf(c):
    """
    Custom dev domains, i.e. skovik.dev
    /etc/resolv.conf should be a link to /run/NetworkManager/resolv.conf
    We will enable dnsmasq supplied with NetworkManager.
    It listens on address 127.0.1.1
    Regular systemd-resolved listens on 127.0.0.53
    """
    c.sudo("sed -i.bak 's/^#DNSStubListener=.*/DNSStubListener=no/g' /etc/systemd/resolved.conf")
    c.sudo('cp files/network/dnsmasq_conf/nm_confd/00-enable-dnsmasq.conf /etc/NetworkManager/conf.d/00-enable-dnsmasq.conf')
    c.sudo('cp files/network/dnsmasq_conf/dnsmasqd/skovik.conf /etc/NetworkManager/dnsmasq.d/skovik.conf')

    c.sudo('systemctl restart systemd-resolved')
    c.sudo('systemctl restart NetworkManager')


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

        c.sudo('rm -rf /etc/wireguard/*')
        c.sudo(f'mv {iface_tmp_file_path} {iface_conf_file_path}')
        c.sudo(f'chmod 600 {iface_conf_file_path}')
        c.sudo(f'chown root:root {iface_conf_file_path}')

    # Run: 'sudo wg-quick up skovik-develop'
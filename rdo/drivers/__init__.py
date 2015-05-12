from rdo.drivers import vagrant
from rdo.drivers import ssh

drivers = {
    'ssh': ssh.SSHDriver,
    'vagrant': vagrant.VagrantDriver
}


def find_driver(config):
    return drivers[config['driver']](config)

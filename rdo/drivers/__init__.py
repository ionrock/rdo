from rdo.drivers import vagrant
from rdo.drivers import ssh
from rdo.drivers import docker

drivers = {
    'ssh': ssh.SSHDriver,
    'vagrant': vagrant.VagrantDriver,
    'docker': docker.DockerDriver,
}


def find_driver(config):
    return drivers[config['driver']](config)

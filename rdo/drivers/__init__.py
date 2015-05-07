from rdo.drivers import vagrant

drivers = {
    'ssh': None,
    'vagrant': vagrant.VagrantDriver
}


def find_driver(config):
    return drivers[config['driver']](config)

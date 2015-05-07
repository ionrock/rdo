import os
import functools

from ConfigParser import ConfigParser


def get_config(config_file='.rdo.conf'):
    config = ConfigParser()
    config.read(config_file)
    env = os.environ.get('RDO_ENV') or 'default'
    return dict(config.items(env))


if __name__ == '__main__':
    c = Config('example.conf')
    c.parse()
    print(c.get('driver'))

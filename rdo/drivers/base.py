from subprocess import call


def truthy(val):
    if isinstance(val, basestring):
        if val.lower() == 'true':
            return True
        return False
    return val


class BaseDriver(object):

    def __init__(self, config):
        self.config = config

    def use_sudo(self, cmd):
        use_sudo = truthy(self.config.get('use_sudo'))
        if use_sudo:
            return ['sudo'] + cmd
        return cmd

    def working_dir(self, cmd):
        working_dir = self.config.get('directory')
        if working_dir:
            cmd = ['cd', working_dir, '&&'] + cmd
        return cmd

    def do(self, cmd):
        cmd = self.command(cmd)
        call(cmd)

    def command(self):
        raise NotImplementedError()

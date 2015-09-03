from subprocess import call


class BaseDriver(object):

    def __init__(self, config):
        self.config = config

    def working_dir(self, cmd):
        command = ' '.join(cmd)
        working_dir = self.config.get('directory')
        if working_dir:
            command = 'cd %s && %s' % (working_dir, command)
        return command

    def do(self, cmd):
        cmd = self.command(cmd)
        print(cmd)
        call(cmd)

    def command(self):
        raise NotImplementedError()

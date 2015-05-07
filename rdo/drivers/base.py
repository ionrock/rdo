from subprocess import call


class BaseDriver(object):

    def __init__(self, config):
        self.config = config

    def do(self, cmd):
        cmd = self.command(cmd)
        print(cmd)
        call(cmd)

    def command(self):
        raise NotImplementedError()

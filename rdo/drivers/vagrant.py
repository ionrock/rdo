from rdo.drivers.base import BaseDriver


class VagrantDriver(BaseDriver):

    def command(self, cmd):
        cmd = self.use_sudo(cmd)
        cmd = self.working_dir(cmd)

        # We need the command to be a single arg when passing it to
        # vagrant ssh -c
        return ['vagrant', 'ssh', '-c', ' '.join(cmd)]

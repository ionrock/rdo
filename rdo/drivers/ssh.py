import os
import itertools

from rdo.drivers.base import BaseDriver


class SSHDriver(BaseDriver):

    def credentials(self):
        if 'ident' in self.config:
            ident = os.path.abspath(self.config['ident'])
            yield '-i'
            yield ident

    def user_host(self):
        host_target = []
        if 'user' in self.config:
            host_target.append(self.config['user'] + '@')
        host_target.append(self.config['host'])
        yield ''.join(host_target)

    def extra_flags(self):
        if 'flags' in self.config:
            flags = self.config['flags'].split()
            for flag in flags:
                yield flag

    def command(self, cmd):
        ssh_command = ['ssh']

        flags = itertools.chain(
            self.extra_flags(),
            self.credentials(),
            self.user_host()
        )

        for flag in flags:
            ssh_command.append(flag)

        ssh_command.append(self.working_dir(cmd))
        return ssh_command

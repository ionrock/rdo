=========
 Drivers
=========

Drivers for `rdo` define the different ways to connect and run a
command on a remote machine.


The Vagrant Driver
==================

The Vagrant driver tries to re-use the `vagrant` command line to run
commands. For example `rdo ls -la` is the same as:

.. code-block:: bash

   $ vagrant ssh -c "cd /vagrant && ls -la"

The vagrant driver currently supports changing directories before
running commands.


The SSH Driver
==============

The SSH driver allows connecting to any machine via the `ssh`
command. Here is an annotated example config to show the currently
supported options.

.. code-block:: config

   [default]
   driver = ssh
   ssh = putty
   user = eric
   host = example.com
   directory = /opt/myapp
   ident = ~/.ssh/mycloud.pem
   flags = -p 2222


Running `rdo ls -la` then would result in the following command:

.. code-block:: bash

   $ putty -i /home/eric/.ssh/mycloud.pem -p 2222 eric@example.com "cd /opt/myapp && ls -la"


The Docker Driver
=================

The `Docker <https://docker.io>`_ driver tries to use a docker
container to run a command. The config can specify whether to use an
or running container.

.. code-block:: config

   [default]
   driver = docker
   name = ubuntu

Running a `rdo ls -la` then results in the following command:

.. code-block:: bash

   $ docker run -it ubuntu ls -la

You can use `exec = true` in the `.rdo.conf` in order to use `exec`
rather than `run`, the only caveat is that you need to be sure the
name is a running container.


A Note About Escaping
=====================

Currently drivers don't do anything terribly special about escaping
the command. At the moment, I'm assuing `YAGNI
<https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it>`_, but if
I'm wrong, please open an `issue
<https://github.com/ionrock/rdo/issues/>`_.

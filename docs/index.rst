.. rdo documentation master file, created by
   sphinx-quickstart on Tue Jul  9 22:26:36 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to rdo's documentation!
======================================

`rdo` stands for "Remote DO"

If you work on a project via a virtual machine or on a remote server,
`rdo` lets you run commands locally as if they were on the remote
machine.


Why `rdo`?
==========

Like many programmers, I work on code that was intended to run on a
specific platform. Tools such as docker and Vagrant are helpful in
this regard, but it never feels like you're developing locally. The
result is that the local tools you have on your machine go unused as
you struggle to work on a project through a terminal.

The goal of `rdo` is to allow an easy to way to run your commands as
if it were local, while running it on the necessary platform.


Usage
=====

The first step is to create a `.rdo.conf` file. This file is read by
the `rdo` command and describes the machine you'll be peforming
command on.

Here is an example using `rdo` with `Vagrant
<https://www.vagrantup.com/>`_.

.. code-block:: config

   [default]
   driver = vagrant
   directory = /vagrant

By default Vagrant will mount the directory of your `Vagrantfile` at
`/vagrant`. If you have your `Vagrantfile` at the root of your
project, this will make `rdo` act like it is running in the same
directory.

With your `.rdo.conf` in place you can try running a command.

.. code-block:: bash

   $ rdo ls -la

This should provide a list of your project files from the host
machine.


Contents:

.. toctree::
   :maxdepth: 2

   drivers
   contributing
   authors
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

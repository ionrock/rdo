===
rdo
===

.. image:: https://pypip.in/d/rdo/badge.png
        :target: https://pypi.python.org/pypi/rdo


`rdo` stands for "RemoteDO" and is to help facilitate running commands
on "remote" machines. Specifically is meant to help you run and
develop code on a virtual machine, while avoiding having to shell into
the VM.

=====
Usage
=====

The first step is to create a `.rdo.conf` file. Here is an example
using `rdo` with `Vagrant <https://www.vagrantup.com/>`_.

.. code-block:: config

   [default]
   driver = vagrant
   directory = /vagrant


Lets assume you have a `Vagrantfile` in the root of your code base and
are mounting your code to `/vagrant`. Lets also assume you have a
`Makefile` you use to run different tasks for your project.

Here is how you to run the `build` task using `rdo`:

.. code-block::

   $ rdo make build

`rdo` will compose the correct command to run it on your
Vagrant VM. For example, the above would end up running:

.. code-block::

   $ vagrant ssh -c "cd /vagrant && make build"



* Free software: BSD license
* Documentation: https://rdo.readthedocs.org.

Features
--------

* TODO implement a generic ssh driver.

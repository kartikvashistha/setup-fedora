Role Name
=========

Ansible role to configure a new Linux distro with my desired software packages and configurations respectively.

Requirements
------------

Install the requirements in your virtualenv or system as:
```
pip install -r requirements.txt
```

Role Variables
--------------

- **nvidia**: true, default value is null or empty \
    This variable is set to install nvidia drivers. By default, it skips the `nvidia.yml` task.

- **version**: (int), default value is 33 \
    This variable sets the version number of the Fedora distribution. It is of type `int`.

Example Playbook
----------------

The repo contains `playbook.yml` as a sample playbook to run the role. When running this playbook, it'll ask for your `sudo` password.

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

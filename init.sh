#/bin/sh

# Bootstrap script that installs the initial ansible dependencies, few base packages, the Oh My ZSH framework and runs the playbook.yml in this repo.

sudo dnf install ansible ansible-core curl git -y

ansible-galaxy collection install community.general

# Run the omz framework setup script
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

ansible-playbook --ask-become-pass  playbook.yml
#/bin/sh

# This script installs the initial ansible dependencies, few base packages and the Oh My ZSH framework

sudo dnf install ansible ansible-core curl git -y

ansible-galaxy collection install community.general

# Run the omz framework setup script
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


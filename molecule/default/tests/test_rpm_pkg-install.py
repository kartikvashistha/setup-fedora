import pytest

@pytest.mark.parametrize("name", [
    ("neofetch"),
    ("htop"),
    ("glances"),
    ("steam"),
    ("geary"),
    ("pavucontrol"),
    ("vim-enhanced"),
    ("samba"),
    ("gnome-tweaks"),
    ("code"),
    ("1password"),
    ("google-chrome-beta"),
    ("flatpak"),
    ("discord"),
])
def test_rpm_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed
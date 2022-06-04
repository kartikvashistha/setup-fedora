import pytest

@pytest.mark.parametrize("name", [
    ("us.zoom.Zoom"),
    ("com.microsoft.Teams"),
    ("org.telegram.desktop"),
])

def test_rpm_packages(host, name):
    flatpak = "/var/lib/flatpak/app/"+ name
    assert host.file(flatpak).exists
    assert host.file(flatpak).is_directory
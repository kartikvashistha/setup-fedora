import pytest

@pytest.mark.parametrize("repo", [
    ("rpmfusion-free.repo"),
    ("rpmfusion-free-updates.repo"),
    ("rpmfusion-nonfree.repo"),
    ("rpmfusion-nonfree-updates.repo"),
    ("1Password.repo"),
    ("google-chrome.repo"),
    ("google-chrome-beta.repo"),
    ("vscode.repo"),
])
def test_rpm_fusion_repos(host, repo):
    assert host.file("/etc/yum.repos.d/" + repo).exists
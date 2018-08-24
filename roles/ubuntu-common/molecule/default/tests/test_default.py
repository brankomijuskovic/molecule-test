import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_htop_is_installed(host):
	assert host.package("htop").is_installed

def test_vim_is_there(host):
	assert host.package("vim-common").is_installed

def test_nginx_is_running(host):
	assert host.service("nginx").is_running
	assert host.service("nginx").is_enabled


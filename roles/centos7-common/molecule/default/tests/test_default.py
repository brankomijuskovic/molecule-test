import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_htop_is_installed(host):
	assert host.package("epel-release").is_installed
	assert host.package("htop").is_installed

def test_vim_is_there(host):
	assert host.package("vim-enhanced").is_installed

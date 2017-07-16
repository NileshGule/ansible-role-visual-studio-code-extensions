import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('extension', [
    'donjayamanne.python',
    'wholroyd.jinja'
])
def test_visual_studio_code(Command, extension):
    output = Command.check_output('sudo --user test_usr -H code %s %s',
                                  '--install-extension', extension)
    assert 'already installed' in output


def test_visual_studio_code_extensions(Command):
    output = Command.check_output('sudo --user test_usr -H code %s',
                                  '--list-extensions')
    assert 'donjayamanne.python' in output


@pytest.mark.parametrize('extension', [
    'donjayamanne.python',
    'wholroyd.jinja'
])
def test_visual_studio_code_uninstall_extensions(Command, extension):
    output = Command.check_output('sudo --user test_usr -H code %s %s',
                                  '--uninstall-extension', extension)
    assert 'successfully uninstalled' in output

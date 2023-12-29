# coding: utf-8

import pytest
from adbutils import adb, AdbDevice
import subprocess
import pathlib


@pytest.fixture(scope="session")
def device():
    print("Fixture device")
    return adb.device()


@pytest.fixture
def device_tmp_path(device: AdbDevice):
    tmp_path = "/data/local/tmp/Hi-世界.txt"
    yield tmp_path
    device.remove(tmp_path)

@pytest.fixture
def device_tmp_dir_path(device: AdbDevice):
    tmp_dir_path = "/sdcard/test_d"
    yield tmp_dir_path
    device.remove_dir(tmp_dir_path)

@pytest.fixture
def local_src_in_dir(tmpdir):

    tmpdir.join('1.txt').write('1\n')
    tmpdir.join('2.txt').write('2\n')
    tmpdir.join('3.txt').write('3\n')

    a = tmpdir.mkdir('a')
    a.join('a1.txt').write('a1\n')

    aa = a.mkdir('aa')
    aa.join('aa1.txt').write('aa1\n')

    ab = a.mkdir('ab')
    ab.join('ab1.txt').write('ab1\n')
    ab.join('ab2.txt').write('ab2\n')

    b = tmpdir.mkdir('b')
    b.join('b1.txt').write('b1\n')

    c = tmpdir.mkdir('c')
    ca = c.mkdir('ca')
    ca.join('ca1.txt').write('ca1\n')

    caa = ca.mkdir('caa')
    caa.join('caa1.txt').write('caa1\n')

    cb = c.mkdir('cb')

    yield tmpdir

# @pytest.fixture
# def local_src_out_dir1(tmpdir):
#     local_src_out_dir1 = pathlib.Path('tests/test-assets/test_d1')
#     yield local_src_out_dir1
#     subprocess.check_output(['rm', '-r', local_src_out_dir1])

# @pytest.fixture
# def local_src_out_dir2(tmpdir):
#     local_src_out_dir2 = pathlib.Path('tests/test-assets/test_d2')
#     yield local_src_out_dir2
#     subprocess.check_output(['rm', '-r', local_src_out_dir2])
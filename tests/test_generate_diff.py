from pathlib import Path

from gendiff.gen_diff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff():
    result = read_file('result_file1_file2.txt')
    actual = generate_diff('/home/ttehasi/python-project-50/'
                           'tests/test_data/file1.json',
                           '/home/ttehasi/python-project-50/'
                           'tests/test_data/file2.json')
    assert actual == result
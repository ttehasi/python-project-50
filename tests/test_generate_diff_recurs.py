from gendiff.gen_diff import generate_diff
from tests.test_generate_diff import get_test_data_path, read_file


def test_generate_diff():
    result = read_file('result_file11_file22.txt')
    actual = generate_diff(str(get_test_data_path('file11.json')),
                           str(get_test_data_path('file22.json')))
    yam_act = generate_diff(str(get_test_data_path('file11.yml')),
                            str(get_test_data_path('file22.yml')))
    assert actual == result
    assert yam_act == result

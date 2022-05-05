import os
from hw7.task_05 import merge_sorted_files
import pytest


@pytest.fixture()
def file_list():
    for i in range(1, 4):
        with open(f'5_{i}.txt', 'w+') as f:
            f.writelines([f'{1*i}\n', f'{100*i}\n', f'{10*i}\n'])
    yield ['5_1.txt', '5_2.txt', '5_3.txt']
    for j in range(1, 4):
        os.remove(f"5_{j}.txt")


def test_merge_sorted_files(file_list):
    assert list(merge_sorted_files(file_list)) == [1, 2, 3, 10, 20, 30, 100, 200, 300]


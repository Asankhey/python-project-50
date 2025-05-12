from gendiff.generate_diff import generate_diff
from pathlib import Path

def test_flat_yaml_diff():
    result = generate_diff(
        'tests/test_data/file1.yml',
        'tests/test_data/file2.yml',
    )

    expected = Path('tests/test_data/flat_expected.txt').read_text().strip()
    assert result == expected

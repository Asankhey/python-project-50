from gendiff.generate_diff import generate_diff
from pathlib import Path


def test_plain_yaml_diff():
    result = generate_diff(
        'tests/test_data/nested1.yml',
        'tests/test_data/nested2.yml',
        formatter='plain'
    )

    expected = Path('tests/test_data/plain_expected.txt').read_text().strip()

    assert result == expected

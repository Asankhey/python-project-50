import json
from gendiff.generate_diff import generate_diff


def test_json_format():
    result = generate_diff(
        'tests/test_data/nested1.yml',
        'tests/test_data/nested2.yml',
        formatter='json'
    )
    parsed = json.loads(result)

    assert isinstance(parsed, dict)
    assert 'common' in parsed

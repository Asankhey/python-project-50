from gendiff.generate_diff import generate_diff
import json

def test_json_format():
    result = generate_diff(
        'tests/test_data/plain1.yml',
        'tests/test_data/plain2.yml',
        formatter='json'
    )
    parsed = json.loads(result)
    assert isinstance(parsed, dict)
    assert 'common' in parsed or 'group4' in parsed
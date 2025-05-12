from gendiff.generate_diff import generate_diff


def test_json_diff():
    with open('tests/test_data/json_expected.txt') as file:
        expected = file.read()

    result = generate_diff(
        'tests/test_data/nested1.yml',
        'tests/test_data/nested2.yml',
        formatter='json'
    )

    assert result == expected

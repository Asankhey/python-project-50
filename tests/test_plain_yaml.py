from gendiff.generate_diff import generate_diff


def test_plain_yaml_diff():
    result = generate_diff(
        'tests/test_data/nested1.yml',
        'tests/test_data/nested2.yml',
        formatter='plain'
    )

    expected = (
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. "
        "From [1, 2, 3] to 'so much'\n"
        "Property 'setting4' was removed\n"
        "Property 'setting5' was removed"
    )

    assert result == expected
from gendiff.generate_diff import generate_diff


def test_plain_yaml_diff():
    result = generate_diff(
        'tests/test_data/nested1.yml',
        'tests/test_data/nested2.yml',
        formatter='plain'
    )

    expected = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From [1, 2, 3] to 'so much'\n"
        "Property 'common.setting6.ops' was added with value: 'vops'\n"
        "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
        "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]"
    )

    assert result == expected
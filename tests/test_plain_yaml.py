from gendiff.generate_diff import generate_diff


def test_plain_yaml_diff():
    result = generate_diff(
        'tests/test_data/plain1.yml',
        'tests/test_data/plain2.yml',
        formatter='plain'
    )

    expected = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From true to [complex value]\n"
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From 'too much' to 'so much'\n"
        "Property 'common.setting6.ops' was added with value: 'vops'\n"
        "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
        "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]\n"
        "Property 'group4.default' was updated. From null to ''\n"
        "Property 'group4.foo' was updated. From 0 to null\n"
        "Property 'group4.isNested' was updated. From false to 'none'\n"
        "Property 'group4.key' was added with value: false\n"
        "Property 'group4.nest.bar' was updated. From '' to 0\n"
        "Property 'group4.nest.isNested' was removed\n"
        "Property 'group4.someKey' was added with value: true\n"
        "Property 'group4.type' was updated. From 'bas' to 'bar'"
    )

    assert result == expected
from gendiff.generate_diff import generate_diff

def test_nested_yaml_diff():
    result = generate_diff('tests/test_data/nested1.yml', 'tests/test_data/nested2.yml')
    expected = """{
    common: {
        setting1: Value 1
      - setting2: 200
        setting3: true
      + setting4: blah blah
      + setting5: {
        key5: value5
    }
        setting6: {
            doge: {
              - wow: [1, 2, 3]
              + wow: so much
            }
            key: value
        }
    }
  - setting4: blah blah
  - setting5: {
    key5: value5
}
}"""
    assert result == expected
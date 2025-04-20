from gendiff.generate_diff import generate_diff


def test_nested_yaml_diff():
    result = generate_diff(
        'tests/test_data/nested1.yml',
        'tests/test_data/nested2.yml'
    )
    expected = """{
    common: {
      + follow: false
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
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""
    assert result == expected
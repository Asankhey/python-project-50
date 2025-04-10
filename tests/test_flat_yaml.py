from gendiff.generate_diff import generate_diff


def test_flat_yaml_diff():
    result = generate_diff('tests/test_data/file1.yml', 'tests/test_data/file2.yml')
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert result == expected
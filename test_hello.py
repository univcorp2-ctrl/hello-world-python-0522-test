from hello import hello


def test_hello_returns_expected_message():
    assert hello() == "Hello, world!"

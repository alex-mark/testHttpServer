from scratch.headers import Headers


def test_can_add_headers():
    # Given that I have an empty object
    headers = Headers()

    # When I add a header
    headers.add("x-a-header", "a value")

    # Then I should be able to get the value of that header back
    assert headers.get("x-a-header") == "a value"


def test_headers_are_case_insesitive():
    headers = Headers()

    headers.add("X-A-HEADER", "a value")

    assert headers.get("x-a-header") == "a value"


def test_getting_a_missing_header_returns_none():
    headers = Headers()

    assert headers.get("x-a-header") is None


def test_can_get_headers_with_fallback():
    headers = Headers()

    # When I get that some header with a fallback value
    # Then I should get back that fallback value
    assert headers.get("x-a-header", "fallback") == "fallback"


def test_can_get_headers_as_ints():
    headers = Headers()

    headers.add("content-length", "1024")

    assert headers.get_int("content-length") == 1024


def test_can_get_headers_as_ints_with_fallback():
    headers = Headers()

    assert headers.get_int("content-length") is None


def test_getting_a_header_returns_its_last_value():
    headers = Headers()

    headers.add("x-a-header", "1")
    headers.add("x-a-header", "2")

    assert headers.get("x-a-header") == "2"


def test_can_get_all_of_a_headers_values():
    headers = Headers()

    headers.add("x-a-header", "1")
    headers.add("x-a-header", "2")

    assert headers.get_all("x-a-header") == ["1", "2"]


def test_headers_is_iterable():
    headers = Headers()

    headers.add("content-type", "application/javascript")
    headers.add("content-length", "1024")
    headers.add("x-some-header", "1")
    headers.add("x-some-header", "2")

    assert sorted(list(headers)) == sorted(
        [
            ("content-type", "application/javascript"),
            ("content-length", "1024"),
            ("x-some-header", "1"),
            ("x-some-header", "2"),
        ]
    )

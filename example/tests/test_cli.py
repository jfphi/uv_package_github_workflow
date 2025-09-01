from uv_example.cli import greet


def test_greet() -> None:
    assert greet("UV") == "Hello, UV!"




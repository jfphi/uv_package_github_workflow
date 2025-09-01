from __future__ import annotations

import argparse


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="uv-example CLI")
    parser.add_argument("--name", "-n", default="World", help="Name to greet")
    args = parser.parse_args(argv)

    message = greet(args.name)
    print(message)


if __name__ == "__main__":  # pragma: no cover
    main()




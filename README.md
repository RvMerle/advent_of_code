# Advent of Code

Python solutions for Advent of Code.

## Where the code lives

All 2025 solutions are in the 2025 folder (for example [`2025/day01/code.py`](2025/day01/code.py)). Each day is a small package containing:

- [`code.py`](2025/day01/code.py) - solution code
- [`input.txt`](2025/day01/input.txt) - puzzle input
- [`test.py`](2025/day01/test.py) - tests

## Setup

This repo uses `uv`. Install the required dependencies with

```bash
uv sync
```

## Run tests

`pytest` is included in dependencies (see [`pyproject.toml`](pyproject.toml)).

```bash
uv run pytest
```

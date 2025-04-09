install:
	uv pip install --upgrade pip && uv pip install --editable .[dev]

test:
	uv run pytest

lint:
	uv run flake8

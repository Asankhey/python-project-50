install:
	uv pip install --upgrade pip && uv pip install -r requirements.txt

test:
	pytest

lint:
	uv run flake8

lint:
	uv run ruff check

install:
	uv sync

build:
	uv build

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

package-install:
	uv tool install dist/*.whl

test:
	uv run pytest

check: test lint

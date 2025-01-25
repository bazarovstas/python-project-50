install:
	uv sync

build:
	uv build

help:
	uv run gendiff -h

package-install:
	python -m pip install --user dist/*.whl

package-reinstall:
	pip install --upgrade --force-reinstall dist/*.whl

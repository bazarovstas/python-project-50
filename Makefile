install:
	uv sync

build:
	uv build

help:
	uv run gendiff -h

diff:
	uv run gendiff gendiff/input_data/file1.json gendiff/input_data/file2.json

package-install:
	python -m pip install --user dist/*.whl

package-reinstall:
	pip install --upgrade --force-reinstall dist/*.whl

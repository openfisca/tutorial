all: test

install:
	pip install --upgrade pip pipenv
	pipenv install --keep-outdated

test: clean
	pipenv run python test_notebooks.py .

clean:
	rm -f executed_*

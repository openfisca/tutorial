all: test

install:
	pip install --upgrade pip pipenv
	pipenv install --dev --keep-outdated

run:
	pipenv run jupyter notebook

test: clean
	pipenv run python test_notebooks.py .

clean:
	rm -f executed_*

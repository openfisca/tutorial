all: test

install:
	pip install --upgrade pip pipenv
	# $PIPENV_OPTION is used to skip Pipfile.lock on edge CircleCI build
	pipenv install --dev --keep-outdated ${PIPENV_OPTION}

run:
	pipenv run jupyter notebook

test: clean
	pipenv run python test_notebooks.py .

clean:
	rm -f executed_*

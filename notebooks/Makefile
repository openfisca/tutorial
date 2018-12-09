all: test

run:
	jupyter notebook

test: clean
	python test_notebooks.py .

clean:
	rm -f executed_*

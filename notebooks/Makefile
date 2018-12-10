all: test

run:
	@# To run Jupyter locally (without Binder)
	jupyter notebook

test: clean
	@# To test that notebooks are compatible with the installed libraries.
	python test_notebooks.py .

clean:
	rm -f executed_*

all: test

uninstall:
	@# Uninstall all installed libraries of your current Python workspace.
	@# Handy when testing the instructions described in the README.md file.
	pip freeze | grep -v "^-e" | xargs pip uninstall -y

install:
	@# Install libraries as described in the requirements.txt file.
	pip install --upgrade pip
	pip install -r requirements.txt

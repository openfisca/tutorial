# -*- coding: utf-8 -*-

import sys
import os
from io import open

from nbformat import read, write
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

import logging
import traceback


'''
Checks notebooks by trying to convert each one of them into a notebook that
includes the execution results.

This script is similar to running this command:
    jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=60 \
                      --ExecutePreprocessor.kernel_name=python3 \
                      --output demo.ipynb demo.ipynb

on a group of notebooks. Whenever an error occurs, this script will give the user
pretty printed output in order to fix it.
'''


log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)


def is_notebook(file_path):
    return file_path[-6:] == ".ipynb"


def run(notebook_path):
    '''
    Execute a notebook and update it with its execution result.
    '''
    notebook_directory = os.path.dirname(notebook_path)
    notebook_filename = os.path.basename(notebook_path)

    with open(notebook_path) as f:
        notebook = read(f, as_version = 4)

    try:
        # Execute all the cells in the notebook
        ep = ExecutePreprocessor(timeout = 600, kernel_name = "python3")
        ep.preprocess(
            notebook,
            {"metadata": {"path": notebook_directory}}
            )

    except CellExecutionError:
        msg = 'Error executing the notebook "%s".\n' % notebook_filename
        msg += 'Take a look at the stack trace for more information.\n'
        log.error(msg)
        raise

    finally:
	    with open(notebook_path, mode = "wt") as f:
	        write(notebook, f)


# Check script target (file or directory) and test all notebooks
if __name__ == "__main__":
    try:
        target = sys.argv[1]

        if os.path.isdir(target):
            for file in os.listdir(target):
                if is_notebook(file):
                    log.debug(u"> " + file)
                    run(os.path.join(target, file))
        else:
            if not is_notebook(target):
                raise Exception(u"Expected an .ipynb file. Got: {}".format(target))
            run(target)

        log.info(u"OK. No error detected in tested notebook(s).")
    except BaseException as e:
        if len(sys.argv) == 1:
            log.error(u"Missing notebook or directory containing notebooks to test.")
            log.warn(u"USAGE: python test_notebooks.py target")
            log.warn(u"where 'target' is directory containing notebooks, or a .ipynb notebook file.")

        else:
            log.debug(str(e.__class__.__name__) + ": ")
            if e.__class__ is CellExecutionError and e.from_cell_and_msg:
                log.debug(e.from_cell_and_msg)
            elif e.message:
                log.debug(e.message)
            log.error(traceback.format_exc())
            sys.exit(1)

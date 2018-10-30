# -*- coding: utf-8 -*-

import sys
import os
from io import open

from nbformat import read, write
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
# Other dependencies: jupyter-client, ipykernel

import logging
import traceback


'''
Checks notebooks by trying to convert each one into a notebook
that includes its execution results.

This script is similar to this command:
jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=60
                  --output executed_notebook.ipynotebook demo.ipynb
'''


log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)


def is_notebook(file_path):
    return file_path[-6:] == ".ipynb"


def run(notebook_path):
    '''
    Test given notebook execution.
    If an error occurs, save execution result in a new notebook 
    of same name with 'executed_' prefix.
    '''
    notebook_directory = os.path.dirname(notebook_path)
    notebook_filename = os.path.basename(notebook_path)
    notebook_filename_out = os.path.join(
        notebook_directory,
        'executed_' + notebook_filename
        )

    with open(notebook_path) as f:
        notebook = read(f, as_version=4)

    try:
        # Execute all the cells in the notebook
        ep = ExecutePreprocessor(timeout=600, kernel_name='python')
        executed_notebook = ep.preprocess(notebook,
                {'metadata': {'path': notebook_directory}}
                )

    except CellExecutionError:
        executed_notebook = None
        msg = 'Error executing the notebook "%s".\n\n' % notebook_filename
        msg += 'See notebook "%s" for traceback.' % notebook_filename_out
        log.error(msg)
        raise

    finally:
        with open(notebook_filename_out, mode='wt') as f:
            write(notebook, f)
        if executed_notebook is not None:
            os.remove(notebook_filename_out)


# Check script target (file or directory) and test all notebooks
if __name__ == "__main__":
    try:
        target = sys.argv[1]

        if os.path.isdir(target):
            for file in os.listdir(target):
                if is_notebook(file):
                    log.debug("> " + file)
                    run(os.path.join(target, file))
        else:
            if not is_notebook(target):
                raise Exception(u"Expected an .ipynb file. Got: {}".format(target))
            run(target)

    except BaseException as e:
        if len(sys.argv) == 1:
            log.error(u"Missing a notebook directory or a notebook to test.")
            log.warn(u"USAGE: python test_notebooks.py target")
            log.warn(u"where 'target' is a notebooks directory OR an .ipynb notebook file to test.")

        else:
            log.debug(str(e.__class__.__name__) + ': ')
            if e.__class__ is CellExecutionError and e.from_cell_and_msg:
                log.debug(e.from_cell_and_msg)
            elif e.message:
                log.debug(e.message)
            log.error(traceback.format_exc())

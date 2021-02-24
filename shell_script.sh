#!/bin/bash
set -eu

if python -m unittest discover .; then
    git add .
    git commit -m "Test suite updated. All tests ran successfully."
    echo "All tests passed. Files have been committed to Git."
else
    echo "1 or more tests have failed. Could not commit files to Git."
fi
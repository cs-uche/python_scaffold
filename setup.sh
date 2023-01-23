#!/bin/bash
# Author : Sopuruchi Chisom


touch requirements.txt Makefile test.py 

chmod +x test.py

echo -e 'black
pylint
pytest
pytest-cov' > requirements.txt
prg = './crowsnest.py'

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint: 
	pylint $(prg)

format:
	black *.py

.PHONY: test
test:
	python -m pytest -xvv --cov=crowsnest test.py
	
all: install lint test

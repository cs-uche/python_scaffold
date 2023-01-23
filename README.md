[![Python application that runs tests with Github Actions](https://github.com/cs-uche/python_scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/cs-uche/python_scaffold/actions/workflows/main.yml)
# python_scaffold
**The goal: Implement a Continuous Integration Pipeline** 

<br/>In construction, a scaffold is a temporary structure that aids builders in transporting their tools and accessing heights.

The scaffold in this repo has a similar concept- it helps people write code. The steps below get you started in writing nearly any program.

### Steps
1. Use a cloud environment: This program uses Github Codespaces

2. Create a setup script
<br/>The script contains commands which are nearly always needed in any program I write. It creates a requirements file(populating it), a test file, and a Makefile.
```bash
touch setup.sh
chmod +x setup.sh
./setup.sh
```

3. Create the program
<br/>The program, crowsnest.py, prints a response with an appropriate article(a or an) based on the user's provided input. It simulates a warning call on a ship.

4. Create the tests for the program
<br/> Implementing test-driven development- write the test cases, fail them, then modify the code to pass the tests.

5. Modify the program(crowsnest.py) to pass the test cases and populate the Makefile: a make file is a program with a set of reusable commands. It reduces the possibility of errors and supports the Continuous Integration/Continuous Delivery platform.
```bash
make all
```
The command above installs the prerequisites, checks for syntax errors, and tests the code. The equivalent is below
```bash
make install
make lint
make test
```
One level lower in abstraction, the code above translates to
```bash
pip install --upgrade pip && pip install -r requirements.txt
pylint crowsnest.py
python -m pytest -xvv --cov=crowsnest test.py
```

6. Implement a workflow using GitHub Actions

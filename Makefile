install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C math_functions.py


test:
	python -m pytest -vv --cov=math_functions test_math_functions.py
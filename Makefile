all:

test:
	pipenv run python -m pytest tspsolver

demo:
	pipenv run python demo.py

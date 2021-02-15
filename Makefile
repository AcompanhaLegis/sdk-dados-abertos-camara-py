install:
	pip install -e .

dev:
	pip install -r requirements.txt

dist:
	rm -rf dist build
	python3 setup.py sdist bdist_wheel

release:
	python3 -m pip install --upgrade twine
	python3 -m twine upload dist/*

lint:
	flake8

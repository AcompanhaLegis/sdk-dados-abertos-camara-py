install:
	pip install -e .

clean:
	pip uninstall sdk-dados-abertos-camara
	rm -rf dist build

dev:
	pip install -r requirements.txt

dist:
	rm -rf dist build
	python3 setup.py sdist bdist_wheel

test:
	python3 -m unittest

release:
	python3 -m pip install --upgrade twine
	python3 -m twine upload dist/*

lint:
	flake8 sdk_dados_abertos_camara/*.py

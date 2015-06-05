.PHONY: build venv deps clean

build: venv deps

venv:
	virtualenv --no-site-packages --python=python3.4 .env
	
deps:
	.env/bin/pip install -r project/requirements.txt

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

.PHONY: build venv deps clean

build: venv deps init

venv:
	virtualenv --no-site-packages --python=python3.4 .env
	
deps:
	.env/bin/pip install -r project/requirements.txt

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

init:
	if [ ! -e var/run ]; then mkdir -p var/run; fi
	if [ ! -e var/log ]; then mkdir -p var/log; fi
	if [ ! -e export ]; then mkdir -p export; fi

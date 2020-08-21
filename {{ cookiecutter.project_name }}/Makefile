.PHONY: build venv deps clean init ioweb

build: venv deps init

venv:
	virtualenv -p python3 .env

deps:
	.env/bin/pip install -r requirements.txt

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

init:
	if [ ! -e var/run ]; then mkdir -p var/run; fi
	if [ ! -e var/log ]; then mkdir -p var/log; fi

ioweb:
	mkdir -p src
	if [ ! -e src/ioweb ]; then ln -s /web/ioweb src; fi
	if [ ! -e ioweb ]; then ln -s src/ioweb/ioweb; fi;
	.env/bin/pip install -e src/ioweb

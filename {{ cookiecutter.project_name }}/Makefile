.PHONY: build venv clean

build: venv init

venv:
	pipenv --three lock
	pipenv --three sync
	
clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

init:
	if [ ! -e var/run ]; then mkdir -p var/run; fi
	if [ ! -e var/log ]; then mkdir -p var/log; fi
	if [ ! -e export ]; then mkdir -p export; fi

.PHONY: init venv deps dirs clean pytest test release mypy pylint flake8 ruff check build coverage eradicate

FILES_CHECK_MYPY = {{ cookiecutter.project_name }} tests script
FILES_CHECK_ALL = $(FILES_CHECK_MYPY)
COVERAGE_TARGET = {{ cookiecutter.project_name }}

init: venv deps dirs

venv:
	virtualenv -p python3 .env

deps:
	curl -sS https://bootstrap.pypa.io/get-pip.py | python3 # a fix for manually built python
	pip install -U setuptools # a fix for manually built python
	.env/bin/pip install -r requirements_dev.txt
	{% if cookiecutter.packaging == "yes" %}.env/bin/pip install -e .{% endif %}

dirs:
	if [ ! -e var/run ]; then mkdir -p var/run; fi
	if [ ! -e var/log ]; then mkdir -p var/log; fi

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

pytest:
	pytest -n30 -x --cov $(COVERAGE_TARGET) --cov-report term-missing

test: check pytest
	tox -e check-minver

{% if cookiecutter.packaging == "yes" %}
release:
	git push \
	&& git push --tags \
	&& make build \
	&& twine upload dist/*
{% endif %}
mypy:
	mypy --strict $(FILES_CHECK_MYPY)

pylint:
	pylint -j0 $(FILES_CHECK_ALL)

ruff:
	ruff $(FILES_CHECK_ALL)

check: ruff mypy pylint

build:
	rm -rf *.egg-info
	rm -rf dist/*
	python -m build --sdist

coverage:
	pytest -n30 -x --cov $(COVERAGE_TARGET) --cov-report term-missing

eradicate:
	tox -e eradicate -- flake8 -j auto --eradicate-whitelist-extend="" $(FILES_CHECK_ALL)

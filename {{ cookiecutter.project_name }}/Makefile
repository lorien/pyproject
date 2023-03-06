.PHONY: init venv deps dirs clean pytest test release mypy pylint flake8 bandit ruff check build coverage eradicate

FILES_CHECK_MYPY = {{ cookiecutter.project_name }}
FILES_CHECK_ALL = $(FILES_CHECK_MYPY) tests

init: venv deps dirs

venv:
	virtualenv -p python3 .env

deps:
	.env/bin/pip install -U pip
	.env/bin/pip install -r requirements_dev.txt
	.env/bin/pip install -e .

dirs:
	if [ ! -e var/run ]; then mkdir -p var/run; fi
	if [ ! -e var/log ]; then mkdir -p var/log; fi

clean:
	find -name '*.pyc' -delete
	find -name '*.swp' -delete
	find -name '__pycache__' -delete

pytest:
	pytest --cov {{ cookiecutter.project_name }} --cov-report term-missing

test:
	make check \
	&& make pytest \
	&& tox -e py38-check

{% if cookiecutter.packaging %}
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

flake8:
	flake8 -j auto --isolated --select CCR --max-cognitive-complexity=17 $(FILES_CHECK_ALL)

ruff:
	ruff $(FILES_CHECK_ALL)

bandit:
	bandit -qc pyproject.toml -r $(FILES_CHECK_ALL)

check: mypy ruff pylint flake8 bandit

build:
	rm -rf *.egg-info
	rm -rf dist/*
	python -m build --sdist


coverage:
	pytest --cov {{ cookiecutter.project_name }} --cov-report term-missing

eradicate:
	tox -e eradicate -- flake8 -j auto --eradicate-whitelist-extend="" $(FILES_CHECK_ALL)

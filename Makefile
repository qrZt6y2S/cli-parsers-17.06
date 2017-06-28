# UNIX only


all: test


.install-deps: requirements-dev.txt
	@pip install -U -r requirements-dev.txt
	@touch .install-deps


.flake: .install-deps $(shell find ./cli_parsers/ -type f) \
                      $(shell find ./tests/ -type f)
	@flake8 ./cli_parsers/
	@touch .flake


.develop: .install-deps $(shell find ./cli_parsers/ -type f) .flake
	@pip install -e .
	@touch .develop


test: .develop
	@pytest -q ./tests


cov cover coverage:
	tox


clean:
	@rm -f `find . -type f -name '*.py[cod]' `
	@rm -rf `find . -type d -name '*.egg-info' `
	@rm -rf ./dist/
	@rm -rf ./.tox/
	@rm -f .install-deps
	@rm -f .flake
	@rm -f .develop


.PHONY: all test cov clean

MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

.PHONY: all
all: fmt clean index.md

.PHONY: clean
clean:
	rm -f .cache index.md

.PHONY: fmt
fmt:
	isort create.py
	black create.py
	flake8 --ignore E501,W503 create.py

index.md: create.py index.md.j2
	./create.py > index.md


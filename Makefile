.PHONY: help build

help: ## show this help message and exit
	@echo "usage: make [target]"
	@echo
	@echo "targets:"
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

bootstrap: ## setup development tools
	@brew install ttygif

pack:
	@python setup.py sdist
	@python setup.py bdist_wheel
	@open dist

%:
	@:
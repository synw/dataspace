help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  test               -- Run the unit tests"
	@echo

test:
	@echo ""
	@printf "Run the unit tests"
	@echo ""
	coverage run --source=dataspace -m pytest --maxfail=1 && coverage html && coverage xml coverage.xml
.PHONY:test
# UNIX only

clean:
	@rm -f `find . -type f -name '*.py[cod]' `
	@rm -rf `find . -type d -name '*.egg-info' `
	@rm -rf ./dist/

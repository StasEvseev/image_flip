
clean:
	@find . -name *.pyc -delete
	@rm -rf venv

venv:
	@python3.7 -m venv venv
	@venv/bin/pip install -r requirements.txt

test:
	@venv/bin/pytest

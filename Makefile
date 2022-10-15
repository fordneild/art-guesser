compile:
	pip-compile --output-file=requirements.txt requirements.in
	pip-compile --output-file=dev-requirements.txt dev-requirements.in
pip:
	pip install -r requirements.txt -r dev-requirements.txt
up:
	python ./server/main.py
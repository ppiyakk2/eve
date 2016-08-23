.install-deps:  requirements-dev.txt
	pip install -U -r requirements-dev.txt


flake:  .install-deps
#	python setup.py check -rms
	flake8 pyjogbot


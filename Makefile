.PHONY: install
install:
	npm install --global yarn
	yarn add mc-curseforge-api
	pip install -Ue .

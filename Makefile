.PHONY: install
install:
	npm install --global yarn
	yarn add mc-curseforge-api
	python3 -m pip install -Ue .

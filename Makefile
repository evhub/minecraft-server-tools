.PHONY: local-install
local-install:
	npm install --global yarn
	yarn add mc-curseforge-api
	python3 -m pip install -Ue .

.PHONY: aws-install
aws-install: update-repo
	sudo yum install python3 java-17-openjdk
	sudo python3 -m pip install -Ue .

.PHONY: update-repo
update-repo:
	git pull

.PHONY: install-client
install-client:
	install-client.bat

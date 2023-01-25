.PHONY: local-install
local-install:
	npm install --global yarn
	yarn add node-curseforge
	python3 -m pip install -Ue .

.PHONY: aws-install
aws-install: update-repo
	sudo yum install python3 java-17-amazon-corretto tuned
	sudo tuned-adm profile throughput-performance
	sudo python3 -m pip install -Ue .
	sudo python3 -m minecraft_server_tools.enable_large_pages

.PHONY: update-repo
update-repo:
	git pull

.PHONY: install-client
install-client:
	install-client.bat

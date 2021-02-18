.PHONY: install
install:
	npm install --global yarn
	yarn add mc-curseforge-api
	python3 -m pip install -Ue .

.PHONY: install-aws
install-aws: export NVM_DIR = "${HOME}/.nvm"
	cd ..; curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
	cd ..; . ~/.nvm/nvm.sh
	[ -s "${NVM_DIR}/nvm.sh" ] && \. "${NVM_DIR}/nvm.sh"
	nvm install node
	sudo yum install java-1.8.0-openjdk git python3
	npm install --global yarn
	yarn add mc-curseforge-api
	sudo python3 -m pip install -Ue .

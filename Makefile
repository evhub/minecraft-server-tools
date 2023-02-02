.PHONY: local-install
local-install:
	npm install --global yarn
	yarn add node-curseforge
	python3 -m pip install -Ue .

.PHONY: aws-install
aws-install: update-repo fix-spark
	sudo yum install python3 java-17-amazon-corretto tuned
	sudo yum update
	sudo tuned-adm profile throughput-performance
	sudo python3 -m pip install -Ue .
	sudo python3 -m minecraft_server_tools.setup_large_pages

.PHONY: update-repo
update-repo:
	git pull

.PHONY: fix-spark
fix-spark:
	sudo sysctl kernel.perf_event_paranoid=1
	sudo sysctl kernel.kptr_restrict=0

.PHONY: local-install
local-install: build pip-install
	npm install --global yarn
	yarn add node-curseforge

.PHONY: remote-install
remote-install: update-repo pip-install

.PHONY: aws-install
aws-install: update-repo fix-spark
	sudo yum -y install python3 java-17-amazon-corretto tuned
	sudo yum -y update
	sudo tuned-adm profile throughput-performance
	sudo python3 -m pip install -Ue .
	sudo python3 -m minecraft_server_tools.setup_large_pages

.PHONY: pip-install
pip-install:
	python -m pip install -Ue .

.PHONY: update-repo
update-repo:
	git pull

.PHONY: fix-spark
fix-spark:
	sudo sysctl kernel.perf_event_paranoid=1
	sudo sysctl kernel.kptr_restrict=0

.PHONY: build
build:
	coconut minecraft_server_tools-source minecraft_server_tools --strict

.PHONY: watch
watch:
	coconut minecraft_server_tools-source minecraft_server_tools --strict --watch

.PHONY: watch-verbose
watch-verbose:
	coconut minecraft_server_tools-source minecraft_server_tools --strict --watch --verbose

.PHONY: clean
clean:
	rm -rf ./minecraft_server_tools-source/__coconut_cache__

.PHONY: time
time:
	coconut minecraft_server_tools-source/update_mods.coco minecraft_server_tools --strict --package --force --verbose

.PHONY: time-no-cache
time-no-cache:
	coconut minecraft_server_tools-source/update_mods.coco minecraft_server_tools --strict --package --force --verbose --no-cache

.PHONY: profile
profile: export COCONUT_USE_COLOR=TRUE
profile:
	coconut minecraft_server_tools-source/update_mods.coco minecraft_server_tools --strict --package --force --verbose --profile 2>&1 | tee ./profile.log

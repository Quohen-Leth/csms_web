DC = docker-compose -f docker-compose.dev.yml

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build:	## Build project with compose
	$(DC) build --remove-orphans

.PHONY: up
up:	## Run project with compose
	$(DC) up -d

.PHONY: migrate
migrate: ## Run django migrations
	$(DC) exec web python3 src/manage.py migrate $(APP)

.PHONY: makemigrations
makemigrations: ## Make django migrations
	$(DC) exec web python3 src/manage.py makemigrations $(APP)

.PHONY: run
run: ## Run server
	$(DC) exec web python3 src/manage.py runserver 0.0.0.0:3000

.PHONY: stop
stop: ## Stop project containers with compose
	$(DC) stop

.PHONY: down
down: ## Reset project containers with compose
	$(DC) down --remove-orphans


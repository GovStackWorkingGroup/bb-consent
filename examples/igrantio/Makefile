.DEFAULT_GOAL := help
.PHONY: help
help:
	@echo "------------------------------------------------------------------------"
	@echo "iGrant.io Consent BB solution"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[0-9a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

destroy: ## Delete all containers and volumes
	@if [ -n "$$(docker container ls -aq)" ]; then \
		docker container rm -f $$(docker container ls -aq); \
	fi
	@if [ -n "$$(docker volume ls -q)" ]; then \
		docker volume rm $$(docker volume ls -q); \
	fi
	@echo "Destroyed all containers and volumes"

setup-test: ## Setup test environment
	./test_entrypoint.sh

down: ## Stop the playground
	docker-compose -f docker-compose.yaml down

clean: ## Stop and destroy volumes
	docker-compose -f docker-compose.yaml down -v

run-test-fixtures: ## Load fixtures in to text environment
	docker-compose -f docker-compose.yaml up fixtures
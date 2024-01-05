.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: up
up:
	docker-compose -p telegram_bot up -d --build

.PHONY: down
down:
	docker-compose -p telegram_bot down
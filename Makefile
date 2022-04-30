SHELL=/bin/bash

all:
	docker build -t gcr.io/strong-shelter-348808/fastapi -f docker/API/Dockerfile .
	docker build -t gcr.io/strong-shelter-348808/frontend -f docker/frontend/Dockerfile .
	docker push gcr.io/strong-shelter-348808/fastapi:latest
	docker push gcr.io/strong-shelter-348808/frontend:latest
	kubectl rollout restart deploy fastapi
	kubectl rollout restart deploy frontend
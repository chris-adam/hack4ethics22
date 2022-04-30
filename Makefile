SHELL=/bin/bash

all:
	docker build -t gcr.io/strong-shelter-348808/fastapi -f docker/API/Dockerfile .
	docker push gcr.io/strong-shelter-348808/fastapi:latest
	kubectl rollout restart deploy fastapi
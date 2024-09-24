deps:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt
	@echo "run: . .venv/bin/activate"

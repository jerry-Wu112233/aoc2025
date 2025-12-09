.PHONY: install run test clean shell

# Create venv and install dependencies
install:
	uv sync

# Run your project (assumes a module in src/your_project)
run:
	uv run python -m your_project

# Run pytest tests (you need pytest in optional/groups or add it yourself)
test:
	uv run pytest

# Clean venv and caches
clean:
	rm -rf .venv
	find . -type d -name "__pycache__" -exec rm -rf {} +

# Drop into a shell inside uv's environment
shell:
	uv run bash

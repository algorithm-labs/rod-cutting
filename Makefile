test: install
	poetry run pytest tests/

benchmark: benchmark@rod_size
	@#

benchmark@%: install
	poetry run pytest --benchmark-group-by=param:$* tests/benchmarks/

install:
	poetry install
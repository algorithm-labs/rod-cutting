test: install
	poetry run pytest tests/

benchmark: benchmark@rod_size
	@#

benchmark@%: install
	poetry run pytest --benchmark-group-by=param:$* --benchmark-columns="mean,stddev" tests/benchmarks/

install:
	poetry install
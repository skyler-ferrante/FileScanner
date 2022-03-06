# Build as single binaries
PY= pyinstaller -F

all:
	@$(PY) mark.py
	@$(PY) check.py
	@$(PY) info.py

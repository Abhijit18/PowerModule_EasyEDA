$ErrorActionPreference = "Stop"
python scripts/validate_repo.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
python -m unittest discover -s tests -v
exit $LASTEXITCODE

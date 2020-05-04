## install

```
pip install pytest pytest-cov argh PyYAML watchdog
```

## run

```
watchmedo shell-command -W --recursive --pattern '*.py' --command 'pytest -s -v --cov=. --cov-report=html' .
```

# Python Automation Framework

A lightweight API and UI automation framework built with:

- pytest
- requests
- Playwright
- GitHub Actions

## Features
- API client abstraction
- Page Object Model for UI tests
- Environment-based configuration
- CI-ready structure

## Quick start

### 1) Install
```bash
python -m venv .venv
source .venv/bin/activate   # mac/linux
# .venv\Scripts\activate    # windows (powershell)

pip install -r requirements.txt
python -m playwright install

## Roadmap
- [ ] Auth handling
- [ ] Reporting integration
- [ ] Test tagging
- [ ] Retry logic
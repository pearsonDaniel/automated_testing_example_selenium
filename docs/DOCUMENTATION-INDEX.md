# Documentation Index

This index maps the current, code-verified documentation set.

## Start Here

1. `../README.md`
2. `PROJECT_OVERVIEW.md`

## Setup

1. `setup/PROJECTSETUPLOCAL.md`
2. `setup/PROJECTSTRUCTURE.md`

## Testing and Reporting

1. `testing/TESTRUNNING.md`
2. `testing/TESTRESULTS.md`
3. `testing/TESTDEBUGERRORS.md`
4. `testing/TESTCREATEMOD.md`
5. `testing/TESTCOVERAGEGAPS.md`

## Historical/Reference

1. `PROJECT_SETUP.md` (legacy entry, now redirects)
2. `GIT_HISTORY.md`

## Source of Truth Policy

All docs in this folder are synchronized to runtime behavior in:

- `conftest.py`
- `pytest.ini`
- `src/pages/`
- `locators/`
- `test/`

When behavior changes in code, update docs in this order:

1. `README.md`
2. `PROJECT_OVERVIEW.md`
3. `testing/TESTRUNNING.md`
4. `testing/TESTRESULTS.md`

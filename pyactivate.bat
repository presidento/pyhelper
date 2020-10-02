@echo off
REM Activate Python Virtualenv within the current folder
IF NOT EXIST .venv\ py -m venv .venv
CALL .venv\Scripts\activate.bat

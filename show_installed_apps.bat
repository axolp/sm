@echo off

if "%1"=="" (
    echo Nie podano nazwy procesu.
    exit /b 1
)

adb -s %1 shell pm list packages


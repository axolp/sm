@echo off

if "%1"=="" (
    echo Nie podano nazwy procesu.
    exit /b 1
)


:: Tworzenie katalogu na urządzeniu Android
::adb shell mkdir /storage/emulated/0/BatteryMatter
:: Tworzenie pliku w nowo utworzonym katalogu
::adb shell touch /storage/emulated/0/BatteryMatter/data.txt
:: Uruchomienie polecenia top, filtrowanie wyników i dopisanie do pliku

adb -s %2 shell "top -b -n 1 | grep %1 | awk '{print $1, $6, $8, $9, $10, $11, $12}'"



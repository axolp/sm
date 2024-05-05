@echo off
echo Uruchamiam ADB i konfiguruję urządzenie...
:: Tworzenie katalogu na urządzeniu Android
adb shell mkdir /storage/emulated/0/BatteryMatter
:: Tworzenie pliku w nowo utworzonym katalogu
adb shell touch /storage/emulated/0/BatteryMatter/data.txt
:: Uruchomienie polecenia top, filtrowanie wyników i dopisanie do pliku
adb shell "top -b -n 1 | grep com.google.android.youtube | awk '{print $1, $6, $8, $9, $10, $11, $12}' >> /storage/emulated/0/BatteryMatter/data.txt"
echo Zakończono operacje ADB.
pause

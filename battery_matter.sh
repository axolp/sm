#!/bin/bash


adb shell mkdir -p /storage/emulated/0/BatteryMatter
adb shell touch /storage/emulated/0/BatteryMatter/data.txt
adb shell "top -b -n 1 | grep com.google.android.youtube | awk '{print \$1, \$6, \$8, \$9, \$10, \$11, \$12}' >> /storage/emulated/0/BatteryMatter/data.txt"

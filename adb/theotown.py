import os, time

i = 1
os.system("adb shell input keyevent 164")

while i < 4:
    print(i)
    os.system("adb shell input tap 2206 266")
    os.system("adb shell input tap 1370 666")
    # os.system("adb shell input tap 149 90")
    time.sleep(32)
    os.system("adb shell input tap 2142 82")
    i += 1
    time.sleep(10)

os.system("adb shell input keyevent 164")

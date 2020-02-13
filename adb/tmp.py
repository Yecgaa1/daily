import os,time
while True:
    os.system("adb shell am start -n info.flowersoft.theotown.theotown/info.flowersoft.theotown.theotown.MainActivity")
    time.sleep(65)
    print(1)
    i = 1
    while i < 4:
        os.system("adb shell input tap 2206 266")
        os.system("adb shell input tap 1370 666")
        os.system("adb shell input tap 149 90")
        time.sleep(28)
        os.system("adb shell input tap 2142 82")

    os.system("adb shell input tap 175 960")
    time.sleep(3)

    os.system("adb shell am force-stop info.flowersoft.theotown.theotown")
    time.sleep(3)
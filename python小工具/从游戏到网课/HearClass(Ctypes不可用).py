# _*_ coding:UTF-8 _*_
from __future__ import print_function

import ctypes
import ctypes.wintypes
import threading

import keyboard
import win32con
from pycaw.pycaw import AudioUtilities

RUN = False  # 用来传递运行一次的参数
EXIT = False  # 用来传递退出的参数
user32 = ctypes.windll.user32  # 加载user32.dll
id1 = 110  # 注册热键的唯一id，用来区分热键
id2 = 106
id3 = 107

state = 0


class AudioController(object):
    def __init__(self, process_name):
        self.process_name = process_name
        self.volume = self.process_volume()

    def mute(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                interface.SetMute(1, None)
                print(self.process_name, 'has been muted.')  # debug

    def unmute(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                interface.SetMute(0, None)
                print(self.process_name, 'has been unmuted.')  # debug

    def process_volume(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                print('Volume:', interface.GetMasterVolume())  # debug
                return interface.GetMasterVolume()


class Hotkey(threading.Thread):  # 创建一个Thread.threading的扩展类

    def run(self):
        global EXIT  # 定义全局变量，这个可以在不同线程间共用。
        global RUN  # 定义全局变量，这个可以在不同线程间共用。

        if not user32.RegisterHotKey(None, id1, win32con.MOD_SHIFT, win32con.VK_F9):  # 注册快捷键F9并判断是否成功，该热键用于执行一次需要执行的内容。
            print("Unable to register id", id1)  # 返回一个错误信息

        if not user32.RegisterHotKey(None, id2, 0, win32con.VK_F10):  # 注册快捷键F10并判断是否成功，该热键用于结束程序，且最好这么结束，否则影响下一次注册热键。
            print("Unable to register id", id2)

        # 以下为检测热键是否被按下，并在最后释放快捷键
        try:
            msg = ctypes.wintypes.MSG()

            while True:
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:

                    if msg.message == win32con.WM_HOTKEY:
                        if msg.wParam == id1:

                            RUN = True
                        elif msg.wParam == id2:

                            EXIT = True
                            return

                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageA(ctypes.byref(msg))

        finally:
            user32.UnregisterHotKey(None, id1)  # 必须得释放热键，否则下次就会注册失败，所以当程序异常退出，没有释放热键，
            # 那么下次很可能就没办法注册成功了，这时可以换一个热键测试
            user32.UnregisterHotKey(None, id2)


if __name__ == '__main__':

    hotkey = Hotkey()
    hotkey.start()
    audio_controller = AudioController('RainbowSix.exe')
    while True:

        if RUN == True:
            # 这里放你要用热键启动执行的代码
            print("1")
            if state == 0:
                audio_controller.mute()
                keyboard.send("play/pause media")
                state = 1
            else:
                keyboard.send("play/pause media")
                audio_controller.unmute()
                state = 0

            RUN = False

        elif EXIT == True:
            # 这里是用于退出循环的
            break

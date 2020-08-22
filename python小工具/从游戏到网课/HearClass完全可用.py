from __future__ import print_function

import socket  # 导入 socket 模块
import time

s = socket.socket()  # 创建 socket 对象
port = ("192.168.31.54", 19151)  # 设置端口

from pycaw.pycaw import AudioUtilities

from selenium import webdriver


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


def run(state):
    if state == '2':
        audio_controller.mute()
        driver.find_element_by_class_name("bilibili-player-video").click()

    else:
        driver.find_element_by_class_name("bilibili-player-video").click()
        audio_controller.unmute()


if __name__ == '__main__':
    audio_controller = AudioController('RainbowSix.exe')

    s.bind(port)  # 绑定端口
    driver = webdriver.Chrome()

    s.listen(5)  # 等待客户端连接
    while True:
        c, addr = s.accept()  # 建立客户端连接
        print('连接地址：', addr)
        c.send('欢迎来到智乃酱的书房！'.encode())
        while 1:
            a = c.recv(1024).decode()
            if a != "":
                run(a)
                a = ""
            else:
                time.sleep(1)

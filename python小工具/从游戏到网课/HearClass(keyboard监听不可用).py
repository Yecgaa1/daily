"""
Per session GetMute() SetMute() GetMasterVolume() SetMasterVolume() using
SimpleAudioVolume.
https://github.com/AndreMiras/pycaw/blob/develop/examples/audio_controller_class_example.py
"""

from __future__ import print_function

import keyboard
from pycaw.pycaw import AudioUtilities

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


def main():
    audio_controller = AudioController('chrome.exe')
    audio_controller.mute()
    audio_controller.unmute()


def run():
    global state
    if state == 0:
        audio_controller.mute()
        keyboard.send("play/pause media")
        state = 1
    else:
        keyboard.send("play/pause media")
        audio_controller.unmute()
        state = 0


if __name__ == "__main__":
    audio_controller = AudioController('chrome.exe')
    keyboard.add_hotkey('alt+q', run)

    recorded = keyboard.record(until='shift+alt+f1')

from talon import Module

import requests
import keyring


mod = Module()


@mod.action_class
class Actions:
    def pomodoro_next():
        """Advances the Clockwork Tomato pomodoro"""
        requests.get(
            "https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush",
            params={
                "deviceNames": "Tab S6",
                "text": "NextPomodoro",
                "apikey": keyring.get_password("join", "edjojob@gmail.com"),
            },
        )

    def pomodoro_end():
        """Ends a Clockwork Tomato session"""
        requests.get(
            "https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush",
            params={
                "deviceNames": "Tab S6",
                "text": "StopPomodoro",
                "apikey": keyring.get_password("join", "edjojob@gmail.com"),
            },
        )

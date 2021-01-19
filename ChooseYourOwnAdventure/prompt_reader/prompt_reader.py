import io
import os
import time

from string import ascii_uppercase

import vlc
from gtts import gTTS

class PromptReader:
    """Util class for reading story prompts out loud and capturing user input

    Methods:
        play_message: Plays the provided message using VLC
        get_input_from_prompt: Play provided message, and return user input
    """

    ENDED = 6
    CHOICE_NOT_ALLOWED = "That is not one of your options. Please choose from the following:"

    def play_message(self, message: str) -> None:
        """
        Use google speech to text to convert message to mp3, then play it using
        VLC
        """
        print(message)
        tts = gTTS(message, lang="en-us")
        tts.save("/tmp/tmp.mp3")
        player = vlc.MediaPlayer("/tmp/tmp.mp3")
        player.play()
        while player.get_state() != self.ENDED:
            continue
        os.unlink("/tmp/tmp.mp3")

    def get_input_from_prompt(self, prompt: str, choices: list) -> str:
        """
        Gets user input using provided prompt.
        """
        self.play_message(prompt)
        allowedChoices = set(ascii_uppercase[:len(choices)])
        count = 0
        choice = ''
        
        while choice not in allowedChoices and count < 10:
            for key, val in enumerate(choices):
                letter = ascii_uppercase[key]
                self.play_message(f'{letter}) {val}')
            choice = self.get_input()
            if choice not in allowedChoices:
                self.play_message(self.CHOICE_NOT_ALLOWED)
                count += 1

        try:
            return choices[ascii_uppercase.index(choice)]
        except IndexError:
            print('Too many incorrect Choices Provided')
            return ''

    def get_input(self):
        """
        Wrapper for getting user input to mock during tests
        """
        return input().strip().upper()


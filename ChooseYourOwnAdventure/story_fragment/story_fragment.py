from string import ascii_uppercase
import sys
from typing import Mapping, List

from .choice import Choice

from prompt_reader.prompt_reader import PromptReader

class StoryFragment:
    """Class to represent one fragment of a Choose Your Own Adventure Story.
    StoryFragments are composed of one Prompt, and an array of Choices.

    Constants: 
    Properties:
    Methods:
    """

    CHOICE_NOT_ALLOWED = "That is not one of your options. Please choose from the following:"

    prompt: str = ''
    choices: List[Choice] = []
    pr: PromptReader = PromptReader()

    def __init__(self, prompt: str, choices: List[Mapping[str, str]]):
        self.prompt = prompt
        self.choices = list(
            map(
                lambda choice : Choice(choice['prompt'], choice['next_fragment']),
                choices
            )
        )

    def play_fragment(self):
        self.pr.play_message(self.prompt)

    def play_choices(self):
        choice_prompts = [f'{index + 1}) {choice.prompt}' for index, choice in enumerate(self.choices)];
        self.pr.play_messages(choice_prompts);

    def get_next_fragment_from_choices(self):
        self.play_fragment()
        self.play_choices()
        choice = sys.maxsize
        count = 0

        while count < 10:
            choice = int(self.get_input()) - 1
            if 0 <= choice < len(self.choices):
                break
            self.pr.play_message(self.CHOICE_NOT_ALLOWED)
            count += 1

        if count >= 10:
            raise IOError('User entered too many invalid choices')
        
        return self.choices[choice].next_fragment

    def get_input(self):
        """
        Wrapper for getting user input to mock during tests
        """
        return input().strip()

from unittest import TestCase
from unittest.mock import patch

from prompt_reader.prompt_reader import PromptReader
from .utils import data_provider

class PromptReaderTests(TestCase):
    """
    Tests for the PromptReader class
    """

    def setUp(self):
        self.prompt_reader = PromptReader()

    @staticmethod
    def choices_provider():
        return [
            {
                'prompt': 'test prompt', 
                'input': 'A',
                'choices': ['Test Choice A'], 
                'calls': ['test prompt', 'A) Test Choice A'],
                'expected': 'Test Choice A'
            }, {
                'prompt': 'test prompt 2', 
                'input': 'A',
                'choices': ['Test Choice A', 'Test Choice B'], 
                'calls': ['test prompt 2', 'A) Test Choice A', 'B) Test Choice B'],
                'expected': 'Test Choice A'
            }, {
                'prompt': 'test prompt 2', 
                'input': 'B',
                'choices': ['Test Choice A', 'Test Choice B'], 
                'calls': ['test prompt 2', 'A) Test Choice A', 'B) Test Choice B'],
                'expected': 'Test Choice B'
            }, {
                'prompt': 'test prompt', 
                'input': 'A',
                'choices': ['Test Choice A'], 
                'calls': ['test prompt', 'A) Test Choice A'],
                'expected': 'Test Choice A'
            }
        ]

    @data_provider(choices_provider)
    @patch.object(PromptReader, 'play_message')
    @patch.object(PromptReader, 'get_input')
    def test_get_input_from_prompt(self, values, input_mock, play_mock):
        """
        Test getting input from prompt and choices
        """
        play_mock.return_value = None

        print(values)

        input_mock.return_value = values['input']
        actual = self.prompt_reader.get_input_from_prompt(values['prompt'], values['choices'])
        self.assertEqual(values['expected'], actual)
        for arg in values['calls']:
            play_mock.assert_any_call(arg)

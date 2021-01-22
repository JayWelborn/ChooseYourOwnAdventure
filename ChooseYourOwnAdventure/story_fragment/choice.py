class Choice:
    """This class represents a single choice in a CYOA Story fragment

    Properties:
        prompt: story prompt to be read
        next_fragment: name of story fragment to load if this choice is selected
    """

    prompt = ''
    next_fragment = ''

    def __init__(self, prompt: str, next_fragment: str):
        self.prompt = prompt
        self.next_fragment = next_fragment
    
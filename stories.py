"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""

        self.code = code
        self.title = title
        self.prompts = words
        # list of the prompts used in the story template"
        self.template = text
        # The story template including the prompts to be replaced

    def __repr__(self):
        return f"<Story {self.code} Title: {self.title}>"

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template
        # text is the story template with the prompts to be replaced by the answers generated from the form

        for (key, val) in answers.items():
            # unpack the answers dict into key value pairs
            text = text.replace("{" + key + "}", val)
            # for each key value pair, replace the key and {} with its associated value from the answers dict

        return text
        # returns the text from the story template with the answers in place of the prompts



story1 = Story(
    "s1",
    "Once Upon A Time",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "s2",
    "Wish You Were Here",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story3 = Story(
    "s3",
    "Best Day Ever",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

stories = {story.code: story for story in [story1, story2, story3]}


import re

class AddressCleaner:
    def __init__(self):
        self.whitespace = re.compile(r'\s+')
        self.separators = re.compile(r"[^;/—-]\b\b")
        self.non_letters_numbers = re.compile(r"[^a-zA-Z0-9\s,./-]")


    def trim_whitespace(self, text):
        return self.whitespace.sub(" ", text)

    def separate_address(self, text):
       return self.separators.sub(", ", text)

    def trim_letters_numbers(self, text):
        return self.non_letters_numbers.sub("", text)






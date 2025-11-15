import re


class AddressCleaner:
    def __init__(self):
        self.whitespace = re.compile(r'\s+')

        self.labels = re.compile(
            r'^(Registered Address|Billing Address|Shipping Address|'
            r'Address|Home Address|Office Address|Primary Address|'
            r'Secondary Address|Current Address|Permanent Address|'
            r'Mailing Address|Delivery Address|Residence Address|'
            r'Contact Address|Work Address|Business Address|Vendor Address|'
            r'Company Address|Customer Address|Client Address|'
            r'Supplier Address|Corporate Address|HQ Address|'
            r'Location Address|Default Address|Registered Location|'
            r'Shipping Location|Billing Location|Delivery Location|'
            r'Pickup Address|Dropoff Address|Address Line|'
            r'Street Address|Full Address|Destination Address):\s*',
            re.IGNORECASE
        )

        self.separators = re.compile(r'[;/—–]')

        self.dash_separator = re.compile(r'\s+-\s+')

        self.bad_chars = re.compile(r'[@#$%^&*()[\]{}|\\~`]')

        self.multiple_commas = re.compile(r',\s*,+')

        self.space_before_comma = re.compile(r'\s+,')

        self.comma_no_space = re.compile(r',(\S)')

    def remove_labels(self, text):
        return self.labels.sub('', text)

    def normalize_separators(self, text):
        text = self.separators.sub(',', text)
        text = self.dash_separator.sub(', ', text)
        return text

    def remove_bad_symbols(self, text):
        return self.bad_chars.sub('', text)

    def collapse_whitespace(self, text):
        return self.whitespace.sub(' ', text)

    def fix_commas(self, text):
        text = self.multiple_commas.sub(',', text)
        text = self.space_before_comma.sub(',', text)
        text = self.comma_no_space.sub(r', \1', text)
        return text

    def clean(self, text):
        text = self.remove_labels(text)
        text = self.normalize_separators(text)
        text = self.remove_bad_symbols(text)
        text = self.collapse_whitespace(text)
        text = self.fix_commas(text)
        text = text.strip()
        return text
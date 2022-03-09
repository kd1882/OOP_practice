import re
import json

class Name:
    '''
    This class accepts a name argument and parses it into full, first, middle, and last
    '''
    suffixes = ['jr', 'sr']
    prefixes = ['mr', 'mrs', 'ms']

    def __init__(self, name):
        self.raw = name
        self.full = self._get_full_name()
        split = self.full.split()
        self.first = split[0]
        self.middle = split[1] if len(split)==3 else None
        self.last = split[-1] if len(split)==3 or len(split)==2 else None

    def _get_full_name(self):
        '''
        This function removes suffixes and prefixes from the raw name and returns the result
        '''
        full = self.raw.lower().replace('.', '')
        for x in self.suffixes + self.prefixes:
            full = full.replace(x, '')
        return full.strip()


class Profile(Name):

    '''
    We want to extend the Name class to handle user profiles (which will include a name and a description).
    Create a new class called Profile which inherits from Name that:
    1) Receives the following arguments: name and description.
    2) Handles the name argument in the same way as the Name class.
    3) Adds description as a class attribute.
    4) Includes a function that parses gmail addresses out of the description field matching the following format: Text123@gmail.com (tip: use regex)
    5) Saves the parsed gmail addresses in a class attribute called "gmails"
    6) Overwrites the _get_full_name method by capitalizing the first letter for each part of the name.
    7) BONUS: Be able to caste the class object as a dict which includes all the class attributes.
    '''

    def __init__(self, name, description):
        super(Profile, self).__init__(name)
        self.description = description
        self.gmails = self._parse_email()

    def _parse_email(self):
        email_input = description
        parsed_email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', email_input)
        return parsed_email

    def _get_full_name(self):
        full = self.raw.lower().replace('.', '')
        for x in self.suffixes + self.prefixes:
            full = full.replace(x, '')
        return full.strip().title()

if __name__ == '__main__':
    name = 'John B Jacobs Jr'
    description = 'My email is JJacobs123@gmail.com!'
    bonus = True
    profile = Profile(name, description)
    print(f'Full Name: {profile.full}')
    print(f'Gmail Addresses: {profile.gmails}')
    if bonus:
        print('Dictionary Format:')
        print(vars(profile))
        # print(json.dumps(dict(profile), indent=2))

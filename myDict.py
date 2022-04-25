##### Define my personal data dictionary #####
import time
import os

class myDict():
    """Class to define my personal data
    personal_data : dictionary
    return: dictionary
    """
    def __init__(self, file_name="myDict.txt"):
        self.dict = self.personal_data(file_name=file_name)

    def personal_data(self, file_name):
        """Define personal data"""
        personal_data = {}
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                for line in f:
                    key, value = line.split(",").strip()
                    personal_data[key] = value.strip()
        else:
            personal_data = {
                'name': 'Suki',
                'last_name': 'Ogihara',
                'age': '38',
                'birthday': '1983/08/02',
                'country': 'United States',
                'city': 'Philadelphia',
                'email': 'ituki82@gmail.com',
                'US phone': '+1 267-566-8610',
                'Japanese phone': '+81 70-4765-8610',
            }
        return personal_data
    
    def update(self, key, value):
        """Update personal data"""
        personal_data = self.dict
        personal_data[key] = value
        with open("myDict.txt", "w") as f:
            for key, value in personal_data.items():
                f.write(key + "," + value + "\n")

        return personal_data

import requests


def check_status(self):
    if self.status_code:
        print(self.status_code)
        print(" success ")
    elif self.status_code:
        print("no joy on that link mate")




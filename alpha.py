import json
import difflib
from difflib import get_close_matches

data=json.load(open("data.json"))


def searchy(a):
    a=a.lower()
    if a in data:
        return data[a]
    elif a.title() in data:
        return data[a.title()]
    elif a.upper() in data:
        return data[a.upper()]
    elif len(get_close_matches(a,data.keys())) >0:
        yn=input("Did you mean %s instead? Enter Y is yes, or N if no."%get_close_matches(a,data.keys())[0])
        yn=yn.upper()
        if yn=="Y":
            return data[get_close_matches(a,data.keys())[0]]
        elif yn=="N":
            return "Thank you for using this program."
            return ""
        else:
            return "Invalid input"
    else:
        return "The word doesn't exist. Please double check it."


key=input("Enter the word \n")

output=searchy(key)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)

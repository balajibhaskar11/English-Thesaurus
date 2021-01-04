import json
import difflib
#from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    #elif (SequenceMatcher(None,word,"rain").ratio() > 0.8):
    #    return data["rain"]
    elif ( len(get_close_matches(word,data.keys())) > 0 ):
        word1 = get_close_matches(word,data.keys())[0]
        x = input("Did you mean %s instead? Enter Y is yes, or N if no: " % word1)
        x = x.upper()
        if x == "Y":
            return data[word1]
        elif x=="N":
            return "Thw word doesn't exist....Please double check it."
        else:
            return "We dint understand your entry."
    else:
        return "Thw word doesn't exist....Please double check it."


word = input("Enter the word: ")

output = translate(word) 

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
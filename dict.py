import json
import difflib 
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))

def searchDict(keyword):
    if keyword in data:
        return data[keyword]
    elif len(gcm(keyword,data.keys()))>0:
        suggestion = gcm(keyword,data.keys())[0]
        response =input("Word not found in the dictionary. Did you mean {0}? Y/N: " .format(suggestion))
        if(response.lower()=="y"):
           return searchDict(suggestion)
        else:
            print("Sorry try again.")
    else:
        print("The word you're looking for doesn't exist in the dictionary. Please try again.")

serchKeyword = input("Enter the word you would like to know the meaning: ")
output =searchDict(serchKeyword.lower())

if type(output) == list:
    for item in output:
        print("Def: {0}".format(item))
else:
    print(output)


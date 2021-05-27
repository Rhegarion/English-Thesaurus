# AUTHOR : RITIK RANJAN 
# AN ENGLISH TO ENGLISH DICTIONARY CODE
# DIFFLIB IS A STRING OPERATION LIBRARY WHICH IS USED HERE

import json
from difflib import get_close_matches


Data = json.load(open("data.json"))

def meaning (word) :
    ''' this function gets a word and returns its meaning '''
    word = word.lower()
    if word in Data :
        return Data[word]
    elif word.title() in Data:
        return Data[word.title()]
    elif word.upper() in Data :
        return Data[word.upper()]
    elif len(get_close_matches(word,Data.keys())) > 0 :
        yn = input("did you mean {} instead ? Enter Y if yes or N if no: ".format(get_close_matches(word,Data.keys())[0]))
        if yn == "Y" :
            return Data[get_close_matches(word ,Data.keys())[0]]
        elif yn=="Y" :
            return "The word doesnt exist. Please double check it ."
        else:
            return "we didnt understand your entry."
    else:
        return "The word doesnt exist. Please double check your entry."



word = input("Enter word:")
output = meaning(word)
if type(output) == list :
    for item in output :
        print(item)
else:
    print(output)


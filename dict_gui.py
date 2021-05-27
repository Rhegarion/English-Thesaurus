from tkinter import *
import json
from difflib import get_close_matches


Data = json.load(open("data.json"))

window = Tk()

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


def get_meaning() :
    finder = meaning(w.get())
    
    Meaning1 = Label(window , text= finder[0])
    Meaning1.pack()




e1 = Label(window , text = 'Enter word :')
e1.pack()

w = StringVar()
e2 = Entry(window , textvariable= w)
e2.pack()

b1 = Button(window , text="Meaning", command=get_meaning)
b1.pack()





window.mainloop()

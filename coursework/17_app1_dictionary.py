#bug : there are some words in the dictionary 
        #are consisting of upper and lower case letters
            #fixed but if someone wrote it wrong , program won't help

import json
#import difflib #library to compare text
from difflib import get_close_matches


def read_file(file_path) :
    data = json.load(open(file_path))
    return data

def find_defintion(word,data_file):
    word_lower = word.lower() #lowercase
    if (word_lower in data_file ) :
        return('\n'.join(data_file[word_lower])) #some words ar combination or lower and upper cases
    elif (word in data_file) :
        return('\n'.join(data_file[word]))
    elif bool(get_close_matches( word_lower , data.keys() , n =5)) : 
        matches = get_close_matches( word_lower , data.keys(),  n =5)
        nums = [1,2,3,4,5]
        content = ""
        for i , j in zip(nums , matches):
             content = content + "%s)%s " % (i,j)

        try : 
            word_2 = int(input("Did you mean any of these : " + content + " ? \n \tif no enter 0 , if yes , Enter its number : "))
            if (word_2 == 0):
                return "Sorry! , You can try again!"
            elif (word_2 < 0 or word_2 > (len(matches))) :
                return "you have entered wrong number , Try again!"
            else : 
                return ("you have chosen : " + matches[word_2 - 1] + '\n' + '\n'.join(data_file[matches[word_2 - 1]]))
        except ValueError :
            return "Wrong Input"
    else :
        return "The word doesn't exist. Please double check it."

data = read_file("17_app1_dictionary/data.json")

word = input("Enter a word : ")

print(find_defintion(word , data))
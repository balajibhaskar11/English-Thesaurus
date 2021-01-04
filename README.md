# English-Thesaurus
Python Command line interface application where users can find the word definitions.
This program searches for the given word, if in case the word matching word isn't found the program searches for best possible match using get_close_matches function. Now if there's a match the program asks the user if he/she meant that best matched word. If 'Y' , the defintion for that best matched word gets displayed and if 'N' , program prints "The word doesn't exist....Please double check it.".
If the input is other than 'Y'/'N' program prints " We dint understand your entry. "


To read a JSON File, we have to use "import json" command
After importing we can open and load the contents of json file into a variable in the form of list. 
data = json.load( open("fileName.json") )

Now we have to compare sequences( in this case strings ) to get the best match for the input word.
For that, I have used difflib by importing it using "import difflib" command and "from difflib import get_close_matches"

get_close_matches(inputWord, dataSet, n) is used to find the n best matches.
By default n=3.
To get the top best match, we can use get_close_matches(inputWord, dataSet, n)[0] since get_close_matches returns a list.

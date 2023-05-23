from nltk.corpus import stopwords
#Load the word tokenizer package
from nltk.tokenize import word_tokenize
#define the user input
input_str = "'Stop words are the words that are filtered before"
#crete object for stopwords
stop_word = set(stopwords.words("english"))
#convert word into tokens
token = word_tokenize(input_str)
#remove stopwords from the list of tokens
output = [i for i in token if not i in stop_word]
#remove the stopwords and print the sentence
print("remove stopwords :", output)

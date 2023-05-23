
from nltk.stem import WordNetLemmatizer
#creating the Object for Lemmatizer
lemmatizer = WordNetLemmatizer()
#Printing the lemma of word happier
print("happier:",
lemmatizer.lemmatize("happier",pos="a"))

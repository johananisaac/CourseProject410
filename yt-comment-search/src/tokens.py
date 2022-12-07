import re
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

text = "+ What if you uninstall Windows 10\\n-You have uninstalled windows 10\\nbig brain🧠"

# Lowercase text
text = text.lower()

# Remove punctuation
text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)

# Remove extra spaces
text = re.sub(r'\s{2,}', ' ', text)

# Tokenize text
tokens = text.split(" ")

# Remove extra space if text ends with punctuation
if tokens[-1] == '':
	tokens.pop()

# Stemming
stemmer = PorterStemmer()
tokens = [stemmer.stem(token) for token in tokens]

# Stopwords filtering
nltk.download('stopwords')
tokens = [token for token in tokens if token not in stopwords.words('english')]

print(tokens)
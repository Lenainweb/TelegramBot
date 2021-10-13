import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.model_selection import train_test_split

def clean(text):
  cleaned_text = ''
  for ch in text.lower():
    if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя ':
      cleaned_text = cleaned_text + ch
  return cleaned_text

def get_intent(text):
  for intent in BOT_CONFIG['intents'].keys():
    for example in BOT_CONFIG['intents'][intent]['examples']:
      cleaned_example = clean(example)
      cleaned_text = clean(text)
      if nltk.edit_distance(cleaned_example, cleaned_text) / max(len(cleaned_example), len(cleaned_text)) < 0.4:
        return intent
  return 'not_found'

def bot(text):
  intent = get_intent(text)
  if intent != 'not_found':
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])
  else:
    return random.choice(BOT_CONFIG['not_found']['responses'])

input_text = ''
while input_text != 'exit':
  input_text = input()
  response = bot(input_text)
  print(response)

with open('/content/BOT_CONFIG_new.json') as f:
  BOT_CONFIG = json.load(f)


X = []
y = []
for intent in BOT_CONFIG['intents']:
  for example in BOT_CONFIG['intents'][intent]['examples']:
    X.append(example)
    y.append(intent)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = TfidfVectorizer(preprocessor=clean, ngram_range=(1, 3), analyzer='char')

X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
len(vectorizer.get_feature_names())

clf = RandomForestClassifier(n_estimators=300)
clf.fit(X_train_vectorized, y_train)

clf.score(X_train_vectorized, y_train)

clf.score(X_test_vectorized, y_test)

clf.predict(vectorizer.transform(['где ты живешь?']))



def get_intent_by_model(text):
  return clf.predict(vectorizer.transform([text]))[0]

def bot(text):
  intent = get_intent_by_model(text)
  return random.choice(BOT_CONFIG['intents'][intent]['responses'])


input_text = ''
while input_text != 'exit':
  input_text = input()
  response = bot(input_text)
  print(response)
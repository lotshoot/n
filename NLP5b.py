from nltk import get_similar_sentences

# This is the input sentence
text = "This is a sample sentence."

# This is the number of similar sentences to generate
n = 5

# This is the language code
language_code = 'en'

# Generate similar sentences
similar_sentences = get_similar_sentences(text, n, language_code)

# Print the similar sentences
for sentence in similar_sentences:
  print(sentence)

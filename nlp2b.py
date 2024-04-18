import nltk
from nltk.corpus import PlaintextCorpusReader
#nltk.download('punkt')  #download this

# Replace this with the actual directory path of your Gutenberg corpus
corpus_root = "D:\\M.sc. IT\\Second Year\\NLP practical"
# Update this path

# Create file list reader
filelist = PlaintextCorpusReader(corpus_root, '.*')

print('\n File list: \n')
print(filelist.fileids())
print('\n Corpus Root:')
print(filelist.root)

print ('\n\nStatistics for each text:\n')
print ('Avg Word Length\tAvg Sentence Length\tAvg Word Frequency\tFileName')
for fileid in filelist.fileids():
  num_chars = len(filelist.raw(fileid))
  num_words = len(filelist.words(fileid))
  num_sents = len(filelist.sents(fileid))

  # Calculate average word length
  avg_word_len = num_chars / num_words  

  # Calculate average sentence length (number of words per sentence)
  if num_sents > 0:  # Avoid division by zero
      avg_sent_len = num_words / num_sents
  else:
      avg_sent_len = 0

  # Calculate average word frequency (total words / unique words)
  num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))
  avg_word_freq = num_words / num_vocab

  # Print formatted output with proper labels
  print("{:.2f}".format(avg_word_len), "\t\t\t", "{:.2f}".format(avg_sent_len), "\t\t\t", 
        "{:.2f}".format(avg_word_freq), "\t\t", fileid)


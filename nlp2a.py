import nltk
from nltk.corpus import brown
print ('File ids of brown corpus\n',brown.fileids())
ca01 = brown.words('ca01')
# display first few words
print('\nca01 has following words:\n',ca01)

print('\nca01 has',len(ca01),'words')
#categories or files
print ('\n\nCategories or file in brown corpus:\n')
print (brown.categories())

print ('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\t\tFileName')
for fileid in brown.fileids():
 num_chars = len(brown.raw(fileid))
 num_words = len(brown.words(fileid))
 num_sents = len(brown.sents(fileid))
 num_vocab = len(set([w.lower() for w in brown.words(fileid)]))
 print (int(num_chars/num_words),'\t\t\t', int(num_words/num_sents),'\t\t\t', int(num_words/num_vocab),'\t\t\t', fileid)

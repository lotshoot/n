from inltk.inltk import setup
setup('hi')
from inltk.inltk import tokenize
hindi_text = """प्राकृतिक भाषा सीखना बहुि तिलचस्प है।"""
# tokenize(input text, language code)
print(tokenize(hindi_text, "hi"))

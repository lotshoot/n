import re

def segment_hash_tag(text):
    pattern = re.compile("[^\w']")
    return pattern.sub('', text)

def segment_url(text):
    splitwords = ["www","com","in"]
    words = re.split('\s|(?<!\d)[,.](?!\d)', text)
    return "".join([each for each in words if each not in splitwords])

def segment_word(a, words):
    ans = []
    for k in range(len(a)+1):
        if a[:k] in words:
            ans.append(a[:k])
            break
    return ans[-1] if ans else None

# Reading the corpus
with open("D:\\M.sc. IT\\Second Year\\NLP practical\\Word.txt", 'r') as f:
    lines = f.readlines()
    words = set([e.strip() for e in lines])

print("MENU")
print("-----------")
print(" 1 . Hash tag segmentation ")
print(" 2 . URL segmentation ")
print("enter the input choice for performing word segmentation")
choice = int(input())

if choice == 1:
    text = "#whatismyname"
    print("input with HashTag", text)
    a = segment_hash_tag(text)
elif choice == 2:
    text = "www.whatismyname.com"
    print("input with URL", text)
    a = segment_url(text)
else:
    print("wrong choice...try again")
    a = ""

print(a)
answer = []
while a:
    ans_word = segment_word(a, words)
    if ans_word:
        answer.append(ans_word)
        a = a[len(ans_word):]
    else:
        break

Aft_Seg = " ".join(answer)
print("output")
print("---------")
print(Aft_Seg)  # print After segmentation the input

from tkinter.filedialog import askopenfilename
import docx
import requests, random 
from bs4 import BeautifulSoup 

do_not_replace = [
    "i","I","and","the","am","hi"
]

def get_synonyms(querry):
    URL = "http://moby-thesaurus.org/search?q=" + querry
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    synonyms = []
    for match in soup.findAll('li', attrs = {}):
        #print(word.a.text)
        word = match.a.text
        if "\n" in word:
            word = word[:-1]
        synonyms.append(word)
    return synonyms


def doit(sent):
    spl = sent.split(" ")
    for word in random.choices(spl, k=int((0.3)*len(spl))):
        if word in do_not_replace:
            continue
        syn = get_synonyms(word)
        if len(syn) == 0:
            continue
        replace_word = random.choice(syn)
        try:
            spl[spl.index(word)] = replace_word
            print(word + " => " + replace_word)
        except:
            pass
    sss = ' '.join(word for word in spl)
    return sss


filename = askopenfilename()
print(filename)
doc = docx.Document(filename)
sentence = doc.paragraphs[0].text

#sentence = "Usually, the dog eats fish, meat, milk, rice, bread, etc. "
s = doit(sentence)

print("before: "+sentence)
print("aafter: "+s)

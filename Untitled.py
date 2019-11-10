import os
from pip._internal import main
def pip_install(package):
    if package == "docx":
        os.system("pip uninstall docx -y")
        main(['install', "python-docx"])
    try:
        main(['install', package])
    except Exception as identifier:
        pass
try:
    from tkinter.filedialog import askopenfilename
    import sys
    import docx
    import requests
    import random
    from bs4 import BeautifulSoup 
except Exception as e:
    print(e);print("So installing it!!")
    e = str(e)
    pkg = e[e.index("'")+1:-1]
    pip_install(pkg)
    #os.system("python " + os.path.basename(__file__))
#reimporting them
from bs4 import BeautifulSoup 
from tkinter.filedialog import askopenfilename
import sys
import docx
import requests, random




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


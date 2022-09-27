import sys
import requests
import random

inp1 = sys.argv[1]
inp2 = str(sys.argv[2])


mlen = ""
help = '''
Usage : python3 EzPass.py [Options] {Password Length}

-l <password length>    Choose  password length
-h    Help
'''

if inp1 == '-l':
    mlen = inp2

else:
    print(help)


apis = ["d1468251dcc15bd72245101c1fc07fae5c3747257092d3230","1eirq2gnxpe0x2crebxeo1pdnc3mdk6fpw7io56j6nw02zyj7","c23b746d074135dc9500c0a61300a3cb7647e53ec2b9b658e"]
api = "d1468251dcc15bd72245101c1fc07fae5c3747257092d3230"

def convleet(rw):
    word = []
    for i in rw:
        if i == "a":
            i = random.choice(['a','@','4'])
        elif i == "o":
            i = random.choice(['o','0'])
        elif i == "e":
            i = random.choice(['3','e'])
        elif i == "g":
            i = random.choice(['g','9','6'])
        elif i == "s":
            i = random.choice(['5','s','$','&'])
        elif i == "t":
            i = random.choice(['7','t'])
        elif i == "b":
            i = random.choice(['b','8'])
        elif i == "i":
            i = random.choice(['i','1','!'])
        elif i == "c":
            i = random.choice(['c','('])
        elif i == "h":
            i = random.choice(['h','#'])
        elif i == "r":
            i = random.choice(['r','2'])
        # print(i,end='')
        word.append(i)
    pasword = ''.join(word)
    return pasword

def getword(mlen):
    global api

    r = requests.get('https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength='+ str(mlen) + '&maxLength='+ str(mlen) +'&api_key=' + api)
    i=0

    while (r.status_code!=200) and (i < len(apis)-1):
        i = i+1
        api = apis[i]

    r = requests.get('https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength='+ str(mlen) + '&maxLength='+ str(mlen) +'&api_key=' + api)

    rj = r.json()

    rw = rj['word']
    return rw


password = convleet(getword(mlen))
print('\n')
print(password)


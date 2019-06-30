import json
import os

b = open(r"F:\2019Hashtag\allEnglishHashtagFinal.txt", "r",encoding='UTF-8')
out = b.read()
out = json.loads(out)
print(len(out))
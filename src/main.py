import MeCab
import markovify

import re

m = MeCab.Tagger("-O wakati")

with open("data/samples.txt", "r") as f:
    samples = f.read()


corpus = "".join(
    [
        m.parse(s)
        for s in samples.replace("?", "？")
        .replace("!", "！")
        .replace("。", "。\n")
        .replace("[*", "")
        .replace("[_", "")
        .replace("[!", "")
        .replace("[/", "")
        .replace("[$", "")
        .replace('["', "")
        .replace(">", "")
        .replace("[", "")
        .replace("]", "")
        .replace("\t", "")
        .replace("　", "\n")
        .split("\n")
        if s != ""
        if not re.search(r"https?://", s)
    ]
)

model = markovify.NewlineText(corpus)

for i in range(100):
    sentence = model.make_short_sentence(max_chars=280, tries=20)
    if sentence:
        print("".join(sentence.split()))

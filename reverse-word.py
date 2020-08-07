"""
get reverse word order
"""

sentence = "A quick brown fox."

print(sentence[::-1])

slist = sentence.split(" ")

print(slist)

slist.reverse()

print(slist)

print(" ".join(slist))
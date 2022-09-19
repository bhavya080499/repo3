#1
s=input("enter number")
d = {
    1:['a','G','k','i'],
    2:['G','b','c'],
    3:['a','k','G','c'],
}
count=0
for i in d:
    count=count+1
print(count)
#2
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
#3
def match_words(words):
  ctr = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr
print(match_words(['abc', 'xyz', 'aba', '1221']))
#4
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))
#5

d =	{
  "name": "kelly",
  "age": "25",
  "salary": 8000,
  "city":"New york"
}
d.update({"name": "kelly"})
print(d)
#6


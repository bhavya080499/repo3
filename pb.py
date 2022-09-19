languages = ['a', 'b', 'c']
int = ['1', '2', '3']
dictionary = dict(zip(languages, int))
print(dictionary)
####
lst = []
for i in range(1, 6):
    lst += [i ** 2]
for i in range(6, 26):
    lst += [i]
for i in range(26, 31):
    lst += [i ** 2]
print(lst)
######
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
##########
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "The quick brown fox jumps over the lazy dog"))
#############
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
###############
print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2%3)
print(2**3)
print(2//3)
#############
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)
####################
d = {"key1": 10, "key2": 23}
if "key2" in d:
    d.update({"key2": 20})
print(d)
#20#

# print("hello world")
# name=input("enter your name here:  ")
# print(f"your name has {len(name)} charcters")
# word=input("type your word: ")
# first_word=word.replace(" ", "")
# print(f"your word has this number of charcter {len(first_word)}")
m=5
string=[]
for i in range(1,6):
   text = input(f"enter string{i}")
   string.append(text)
   i=i 
for name in string:
    word=name.replace(" ", "")
    print(f"number of this charcter is {len(word)}")


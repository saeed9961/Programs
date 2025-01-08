name = input("enter your name:" )
split_words = name.split()
print(split_words)
for i in split_words:
    print(f"{i} occurs {split_words.count(i)}")
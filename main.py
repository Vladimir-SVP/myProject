root_word = 'rich'
other_words = ['richiest', 'orichalcum', 'cheers']
same_words = []
for i in other_words:
    
    if str(root_word) not in ''.join(i):
        continue
    else:
        same_words.append(i)
print(same_words)
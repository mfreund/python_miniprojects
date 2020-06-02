import string


sentence = input("Please enter a sentence: ")
count = {'upper': 0, 'lower': 0, 'punctuation': 0, 'total': 0}

for letter in sentence:
    count['total'] += 1
    if letter.isupper():
        count['upper'] += 1
    elif letter.islower():
        count['lower'] += 1
    elif letter in string.punctuation:
        count['punctuation'] += 1

print(f"Upper case: {count['upper']}")
print(f"Lower case: {count['lower']}")
print(f"Punctuation: {count['punctuation']}")
print(f"Total chars: {count['total']}")

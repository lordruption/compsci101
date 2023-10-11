first_set = []
second_set = []
index = 0

prompt = "Enter a sequence of words: "
sequence = input(prompt).split()

for word in sequence:
    if index == 0:
        first_set.append(word)
        index = 1
    elif index == 1:
        second_set.append(word)
        index = 0

result_1 = ' '.join(map(str, first_set))
result_2 = ' '.join(map(str, second_set))

print("1.",result_1)
print("2.",result_2)

#Programming is so much fun, I can't wait to learn more
#['Programming', 'so', 'fun,', "can't", 'to', 'more']
#['is', 'much', 'I', 'wait', 'learn']
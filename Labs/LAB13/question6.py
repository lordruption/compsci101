def get_string_length_tuples(word_list):
    result_list = []
    for i in word_list:
        word_length = len(i)
        formatted = (i , word_length)
        result_list.append(formatted)
    return result_list




word_list = ['fish', 'barrel', 'like', 'noon', 'sand', 'bank']
result = get_string_length_tuples(word_list)
print(result)
print(type(result))
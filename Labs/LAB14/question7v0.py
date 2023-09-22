def get_words(filename):









filename = "many_words1.txt"
data_tuple = get_words(filename)
print(data_tuple[1]," letter words beginning with ",data_tuple[0],": ",data_tuple[2],sep="")
# 15 letter words beginning with e: ['electrophoresis', 'entrepreneurial', 'experimentation', 'extracurricular', 'extralinguistic']
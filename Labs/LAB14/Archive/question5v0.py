def process_barchart(filename):
    alist = []
    text_open = open(filename, "r")
    text_read = text_open.read()
    text_list = text_read.split() 
    for word in text_list:
        count = 0
        for char in word:
            if char == "#":
                count = count + 1
                alist.append((word[0],count))
            else:
                continue
    tuple_final = tuple(alist)
    return tuple_final
    text_open.close()




	
filename = "barchart1.txt"
print(f"Letter frequencies from {filename}: {process_barchart(filename)}")
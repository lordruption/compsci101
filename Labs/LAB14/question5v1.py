def process_barchart(filename):
    alist = []
    text_open = open(filename, "r")
    text_read = text_open.read()
    text_list = text_read.split() 
    # Above is complete
    for line in text_list:
        count = line.count("#")
        alist.append((line[0],count))
    tuple_final = tuple(alist)
    text_open.close()
    return tuple_final






	
filename = "barchart1.txt"
print(f"Letter frequencies from {filename}: {process_barchart(filename)}")

#Letter frequencies from barchart1.txt: (('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 3), ('f', 1), ('g', 1), ('h', 2), ('i', 1), ('j', 1), ('k', 1), ('l', 1), ('m', 1), ('n', 1), ('o', 4), ('p', 1), ('q', 1), ('r', 2), ('s', 1), ('t', 2), ('u', 2), ('v', 1), ('w', 1), ('x', 1), ('y', 1), ('z', 1))
#Letter frequencies from barchart1.txt: (('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 3), ('f', 1), ('g', 1), ('h', 2), ('i', 1), ('j', 1), ('k', 1), ('l', 1), ('m', 1), ('n', 1), ('o', 4), ('p', 1), ('q', 1), ('r', 2), ('s', 1), ('t', 2), ('u', 2), ('v', 1), ('w', 1), ('x', 1), ('y', 1), ('z', 1))

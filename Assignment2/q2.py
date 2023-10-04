#This function takes a string list then returns it in dictionary format
def get_maori_english_dictionary(contents):
    maori_english_dictionary = {}
    listcontent = list(contents)
    for item in listcontent:
        #This turns 'Waipuke - Flood' to 'Waipuke': 'Flood'
        split_item = item.split(" - ")
        key = split_item[0]
        value = split_item[-1]
        maori_english_dictionary[key] = value
    return maori_english_dictionary







contents = ['Tīhi - Cheese', 'Āporo - Apple', 'Ārani - Orange', 'Panana - Banana', 'Pea - Pear',
            'Kapu - Cup', 'Karaehe - Glass', 'Naihi - Knife', 'Pune - Spoon', 'Pereti - Plate',
            'Pouaka hukapapa - Refrigerator', 'Umu - Stove', 'Wenerei - Wednesday', 'Taite - Thursday',
            'Paraire - Friday', 'Rāhoroi - Sa', 'Waka noho - Caravan', 'Waka-rererangi - Aeroplane',
            'Rorohiko - Computer','Pouaka whakaata - Television', 'Kiriata - Cinema',
            'Tiakarete - Chocolate', 'Waea - Telephone']
print(get_maori_english_dictionary(contents))
def get_name(te_reo_intro):
    first_name = []
    last_name = []
    removed_intro = te_reo_intro[3:]
    list_removed_intro = removed_intro.split(' ')
    first_name = list_removed_intro[0]
    last_name = list_removed_intro[1]
    space = " "
    return first_name + space + last_name





print(get_name("Ko Daniel Wilson taku ingoa.")) # Daniel Wilson
print(get_name("Ko Ann Cameron taku ingoa.")) #Ann Cameron

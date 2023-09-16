def get_sequence_number(term):
    if term == 0:
        return 0
    elif term == 1:
        return 0
    elif term == 2:
        return 1
    elif term >= 3:
        term_minus_1 = get_sequence_number(term-1)
        term_minus_2 = get_sequence_number(term-2)
        term_minus_3 = get_sequence_number(term-3)
        return term_minus_1 + term_minus_2 + term_minus_3


# T3 = T2 + T1 + T0 = 1
# Tn = Tn-1 + Tn-2 + Tn-3
# T0 = 0, T1 = 0, and T2 = 1









term = 5
print("Term", term,"of the sequence is", get_sequence_number(term))
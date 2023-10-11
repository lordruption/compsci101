def get_pell_number(n):
    pel_number = [0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, 80782]
    if n >= 0:
        return pel_number[n]




n = 5
print(f"Pell({n}) = {get_pell_number(n)}")




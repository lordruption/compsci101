import statistics
def get_min_median_max(a_list):
    a_list.sort()
    middle = statistics.median(a_list)
    return (a_list[0], middle,a_list[-1])














print(get_min_median_max([2, -4, 99, 12, 56, 25]))

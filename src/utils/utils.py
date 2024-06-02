def get_max_size_cnt(cnts):
    max_size_index = 0
    max_size = 0
    for i, cnt in enumerate(cnts):
        if cnt.size > max_size:
            max_size = cnt.size
            max_size_index = i
    return max_size, max_size_index
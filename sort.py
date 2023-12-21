def sort_col1(li, max_rank=42, rank=lambda x: x):
    counts = [[] for _ in range(max_rank + 1)]
    for index, ele in enumerate(li):
        counts[rank(ele)].append(index)
    return [ele for li in counts for ele in li]

#######################################################
def date_digits1(date):
    return  [int(ele[14:16]+ele[17:]) for ele in date]

def from_digit1(digits):
    date = '2019-08-30 08:'
    str_dig = str(digits)
    if len(str_dig) < 4:
        str_dig = '0' * (4-len(str_dig)) + str_dig
    date += str_dig[0:2] + ':' + str_dig[2:]

    return date

def sort_col2(li,max_rank=5959, rank=lambda x:x):
    li = date_digits1(li)
    counts = [[] for i in range(max_rank+1)]
    for index, ele in enumerate(li):
        counts[rank(ele)].append(index)
    return [ele for li in counts for ele in li]
#########################################################
def date_digits2(date):
    return [int(ele[11:13]+ele[14:16]+ele[17:]) for ele in date]

def sort_col4(li,max_rank=170802, rank=lambda x:x):
    li = date_digits2(li)
    counts = [[] for i in range(max_rank+1)]
    for index, ele in enumerate(li):
        counts[rank(ele)].append(index)
    return [ele for li in counts for ele in li]
#########################################################
def counting_sort_radix(list_, max_rank=18, rank=lambda x: x):
    counts = [[] for i in range(max_rank + 1)]
    for index, ele in enumerate(list_):
        counts[rank(ele)].append(index)
    return [ele for li in counts for ele in li]

def sort_col3(col_data):
    simple_map = dict()
    for i in range(0, 10):
        simple_map[str(i)] = i
    alphabet = "afhnrs"
    alphebet_u = alphabet.upper()
    for idx, val in enumerate(alphebet_u):
        simple_map[val] = 10 + idx

    length = len("05F0055N") - 1
    index = [i for i in range(len(col_data))]
    for itx in range(length):
        value_to_sort = [simple_map[ele[-itx - 1]] for ele in col_data]
        index = counting_sort_radix(value_to_sort)
        col_data = col_data.iloc[index]
    index = col_data.index
    return index
#########################################################
def sort_col6(li, rank=lambda x: x):
    li = (li * 1000).round().astype('int64')
    max_rank = max(li)
    counts = [[] for _ in range(max_rank + 1)]
    for index, ele in enumerate(li):
        counts[rank(ele)].append(index)
    return [ele for li in counts for ele in li]
#########################################################
def sort_col7(li, rank=lambda x: x):
    li = [0 if ele=='Y' else 1for ele in li]
    max_rank = max(li)
    counts = [[] for _ in range(max_rank + 1)]
    for index, ele in enumerate(li):
        counts[rank(ele)].append(index)
    return [ele for li in counts for ele in li]
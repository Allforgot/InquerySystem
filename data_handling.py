from sort import *
# from sort import sort_col1
import pandas as pd
import time

sort_function = {0: sort_col1, 1: sort_col2, 2: sort_col3,
                 3: sort_col4, 4:sort_col3, 5:sort_col6, 6:sort_col7}
def search_data(params):
    # Add code to search data based on a query
    data = params['data']

    # filter part
    select = params['select']
    for ele in select:
        col = ele['col_idx']
        select_data = ele['data']
        data = data[data.iloc[:,col].isin(select_data)]
        data = data.reset_index(drop=True)


    filter = params['filtering']
    for ele in filter:
        col = ele['col_idx']
        from_ = ele['from']
        to = ele['to']

        sort_func = sort_function[col]
        sort_idx = sort_func(data.iloc[:, col])
        data = data.iloc[sort_idx, :]
        from_idx_start = 0
        from_idx_end = data.shape[0]
        while from_idx_end>=from_idx_start:
            mid_idx = (from_idx_start+from_idx_end)//2
            if data.iloc[mid_idx, col] == from_:
                break
            if data.iloc[mid_idx, col] < from_:
                from_idx_start = mid_idx + 1
            else:
                from_idx_end = mid_idx - 1
        while data.iloc[mid_idx-1, col] == from_:
            mid_idx -= 1
        from_idx = mid_idx

        to_idx_start = 0
        to_idx_end = data.shape[0]
        while to_idx_end>=to_idx_start:
            mid_idx = (to_idx_start+to_idx_end)//2
            if data.iloc[mid_idx, col] == to:
                break
            if data.iloc[mid_idx, col] < to:
                to_idx_start = mid_idx + 1
            else:
                to_idx_end = mid_idx - 1
        while data.iloc[mid_idx+1, col] == to:
            mid_idx += 1
        to_idx = mid_idx
        data = data.iloc[from_idx:to_idx+1, :]
        # data = data[(data.iloc[:, col] >= from_) & (data.iloc[:, col] <= to)]
        data = data.reset_index(drop=True)
    return data

def sort_data(params):
    # Add code to sort data based on a key
    data = params['data']

    for i in range(len(params['sorting'])-1, -1, -1):
        ele = params['sorting'][i]
        col = ele['key']
        order = ele['order']
        sort_func = sort_function[col]
        sort_idx = sort_func(data.iloc[:, col])
        data = data.iloc[sort_idx, :]
        if order == 1:
            data = data.iloc[::-1,:]
        data = data.reset_index(drop=True)
    return data


def join_data(data1, data2):
    # Add code to join two datasets based on a key
    new_data = pd.concat([data1, data2])
    new_data = new_data.reset_index(drop=True)
    return new_data

if __name__ == '__main__':

    data = pd.read_csv('data.csv')
    params = {}
    params['data'] = data
    select_cond1 = {'col_idx':0,'data':[31]}
    params['select'] = [select_cond1]

    filtering_cond1 = {'col_idx': 1, 'from': '2019-08-30 08:42:35', 'to': '2019-08-30 08:51:45'}
    filtering_cond2 = {'col_idx': 5, 'from': 5.0, 'to': 31.0}
    filtering_list = [filtering_cond1, filtering_cond2]
    sorting_cond = {'key': 1, 'order': 0}
    sorting_list = [sorting_cond]
    params['filtering'] = filtering_list
    params['sorting'] = sorting_list


    # params2 = {}
    # params2['data'] = data
    # select_cond1 = {'col_idx':1, }
    # filtering_cond4 = {'col_idx': 5, 'from': 8.3, 'to': 13.9}
    # filtering_list2 = [filtering_cond4]


    t = time.time()
    df2 = sort_data(params)
    t1 = time.time()
    # df_new = join_data(data, data)
    test2 = search_data(params)

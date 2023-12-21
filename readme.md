# Inquiry System

## Functions

### Basic Functions

### GUI

### Data Handling

- sort
- search
- join

### File Handling

- read data from the file
- output data to file

## API

### data handling

```python
def data_handling(params):
    pass

params = {
    'data': data_frame,
    'filtering': [
        {
            'col_idx': column_index_1, # int
            'from': data_start, # any type
            'to': data_end # any type
        },
        {
            'col_idx': column_index_2, # int
            'from': data_start, # any type
            'to': data_end # any type
        }
    ],
    'sorting': [
        {
            'key': key_1, # int
            'order': 0 # 0 for ascending, 1 for descending
        }
    ]
}
```





## Generate UML
```bash
pyreverse -ASmy -o png InquirySystem
```
def to_query_string(data):
    '''
    Converts in put to query string.
    '''
    key_value_pairs = []
    for key, value in data.items():
        if type(value) == list:
            for element in value:
                key_value_pairs.append(f'{key}={element}')
        else:
            key_value_pairs.append(f'{key}={value}')
    query_string = '&'.join(key_value_pairs)
    return query_string

def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    float_sm = 0
    for i in data:
        if type(data[i]) == float:
            float_sm += data[i]
    return float_sm
data = {
    1: 22.4, 
    2: 3.5, 
    4: 1, 
    6: 7.6, 
    5: 2, 
    7: 3
  }
print(sum_float_values(data))
def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    box = []
    for i in data:
        if type(i) == int:
            box.append(i)
    return box

data = {
    'a': 1, 
    3 : 2, 
    'c': 3,
    10:'a'
  }

print(find_int_keys(data))
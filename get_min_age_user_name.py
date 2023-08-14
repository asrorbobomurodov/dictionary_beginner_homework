def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    mx = 0
    name = ''
    for i in data:
        if mx < i['age']:
            mx = i['age']
    mn = mx   
    
    for i in data:
        if mn > i['age']:
            mn = i['age'] 
            name = i['name']
    return name

data = [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  },
  {
    'name': 'Ban', 
    'age': 29
  }
]

print(get_min_age_user_name(data))


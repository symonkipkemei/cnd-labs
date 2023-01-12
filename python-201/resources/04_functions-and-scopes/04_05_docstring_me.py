# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km:float)-> float:
    """Converts kilometers to miles

    Args:
        km (float): Kilometers

    Returns:
        float: miles
    """
    
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)

mile = km_to_miles(900)
print(mile)
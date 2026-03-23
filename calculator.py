def sum_numbers(*args):
    """
    Returns the sum of all provided numbers.
 
    Args:
        *args: Any number of numeric values (int or float).
 
    Returns:
        The sum of all arguments. Returns 0 if no arguments are provided.
 
    Raises:
        TypeError: If any argument is not a number.
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Expected a number, got {type(arg).__name__}")
    return sum(args)
 
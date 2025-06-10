def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a>b:
        print("a is the largest")
    elif b>a:
        print("b is the largest")
    else: 
        print("all of em are equal")    
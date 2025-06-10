def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a<b and a<c:
        print("a is the smallest")
    elif b<a and b<c:
        print("b is the smallest")
    elif c<a and c<b:
        print("c is the smallest")
    else: 
        print("all of em are equal")    
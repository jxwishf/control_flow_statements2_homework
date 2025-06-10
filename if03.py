def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a<b and a<c) or (a>b and a<c) :
        print("a is in the middle")
    elif (b<a and b<c) or (b<a and b>c):
        print("b is in the middle")
    elif (c<a and c<b) or (c<a and c>b):
        print("c is in the middle")
    else: 
        print("all of em are equal")   
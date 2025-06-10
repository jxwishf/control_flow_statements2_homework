def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    d1 = n // 10000
    d2 = (n // 1000) % 10
    d3 = (n // 100) % 10
    d4 = (n // 10) % 10
    d5 = n % 10
    if d1 >= d2 and d1 >= d3 and d1 >= d4 and d1 >= d5:
        largest = d1
    elif d2 >= d3 and d2 >= d4 and d2 >= d5:
        largest = d2
    elif d3 >= d4 and d3 >= d5:
        largest = d3
    elif d4 >= d5:
        largest = d4
    else:
        largest = d5

        return largest
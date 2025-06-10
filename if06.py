def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    d0 = n // 10000      # First digit (index 0)
    d1 = (n // 1000) % 10  # Second digit (index 1)
    d2 = (n // 100) % 10   # Third digit (index 2)
    d3 = (n // 10) % 10    # Fourth digit (index 3)
    d4 = n % 10            # Fifth digit (index 4)

    if d0 >= d1 and d0 >= d2 and d0 >= d3 and d0 >= d4:
        return 0
    elif d1 >= d2 and d1 >= d3 and d1 >= d4:
        return 1
    elif d2 >= d3 and d2 >= d4:
        return 2
    elif d3 >= d4:
        return 3
    else:
        return 4
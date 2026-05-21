# Climbing Stairs Problem (Fibonacci Pattern)

# You can take 1 or 2 steps at a time.
# Find total distinct ways to reach the top.

# -------------------------------------------------------------
# Key Idea:
# ways(n) = ways(n-1) + ways(n-2)
# -------------------------------------------------------------


# Version 1 (with return) 
def climb1(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Main
if __name__ == "__main__":
    n = 4

    print("climb1 (return):", climb1(n))  

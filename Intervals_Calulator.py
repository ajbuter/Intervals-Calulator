import sympy as sp

def get_intervals_of_continuity(expr_str):
    x = sp.symbols('x')
    
    try:
        # Parse the function input
        f = sp.sympify(expr_str)
    except sp.SympifyError:
        return "Invalid function input. Please use proper Python/math syntax."

    # Get the domain where function is real-valued
    domain = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)
    
    # Express the domain as intervals
    if isinstance(domain, sp.Union):
        intervals = list(domain.args)
    else:
        intervals = [domain]

    # Convert intervals to string for user display
    interval_strings = [str(interval) for interval in intervals]

    return interval_strings


def main():
    print("=== Continuity Interval Calculator ===")
    print("Enter a function f(x). Example: sin(x)/x, log(x), 1/(x-2), sqrt(x), etc.")
    expr_input = input("f(x) = ")

    intervals = get_intervals_of_continuity(expr_input)

    print("\nIntervals where f(x) is continuous:")
    for i, interval in enumerate(intervals, 1):
        print(f"  Interval {i}: {interval}")

if __name__ == "__main__":
    main()

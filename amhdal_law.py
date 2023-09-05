def amhdal_law(sequential_fraction, speedup):
    if not (0 <= sequential_fraction <= 1):
        raise ValueError("Swquential fraction must be between 0 and 1.")
    if speedup < 1:
        raise ValueError("Speedup factor must be greayher than or equal to 1.")

    parallel_fraction = 1 - sequential_fraction
    overall_speedup = 1 / ((1 - parallel_fraction) + (parallel_fraction / speedup))
    return overall_speedup

sequential_fraction = 0.3
speedup = 5

overall_speedup = amhdal_law(sequential_fraction, speedup)
print(f"Overall speedup according to Amhdal's Law: {overall_speedup: .2f}")

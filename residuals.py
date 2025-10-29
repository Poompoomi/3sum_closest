import math
from itertools import combinations

def sliding_window_target(N, target, window_size=3):
    """
    Find combinations in N that sum to target using sliding-window
    on log-normalized and sorted numbers, allowing negatives to fill residuals.
    
    Args:
        N: list of integers (positives and negatives)
        target: integer, target sum
        window_size: int, initial sliding window size
    Returns:
        List of valid combinations
    """
    
    # Step 1: shift numbers to handle negatives
    shift = abs(min(N)) + 1 if min(N) < 0 else 0
    N_shifted = [x + shift for x in N]
    
    # Step 2: log normalization
    N_log = [math.log(x) for x in N_shifted]
    
    # Step 3: per-element log target
    per_element_log_target = math.log(target + window_size*shift) / window_size
    
    # Step 4: sort numbers by distance to per-element log target
    N_sorted = [x for _, x in sorted(zip([abs(l - per_element_log_target) for l in N_log], N))]
    
    # Split positives and negatives
    positives = [x for x in N_sorted if x > 0]
    negatives = [x for x in N_sorted if x <= 0]
    
    valid_combinations = []
    
    # Step 5: sliding window
    for w_size in range(window_size, 1, -1):  # try window_size down to 2
        for i in range(len(positives) - w_size + 1):
            window = positives[i:i+w_size]
            window_sum = sum(window)
            residual = target - window_sum
            
            # Step 6: try to fill residual using negatives
            found = False
            for r in range(1, len(negatives)+1):
                for neg_subset in combinations(negatives, r):
                    if sum(neg_subset) == residual:
                        # valid combination found
                        valid_combinations.append(window + list(neg_subset))
                        found = True
                        break
                if found:
                    break
            
            # Step 7: check if window alone matches target
            if window_sum == target:
                valid_combinations.append(window)
    
    return valid_combinations


# Example usage
N = [-14, 13, -10, 9, 16, -3, 4, 15, -6, 17]
target = 19
result = sliding_window_target(N, target)
print(result)

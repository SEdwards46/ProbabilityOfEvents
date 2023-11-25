import random

def generate_random_set():
  # Function to generate a random set with two values in the range [1, 6]
    return {random.randint(1, 6), random.randint(1, 6)}

def main():
  # Total number of trials
    total_trials = 1000

   # Initialize event values
    same_values_count = 0
    sum_to_seven_count = 0

  # Run the experiment for the specified number of trials
    for _ in range(total_trials):
        random_set = generate_random_set()

      # Check if the set has the same values
        if len(random_set) == 1:
            same_values_count += 1

       # Check if the sum of the values in the set is 7
        elif sum(random_set) == 7:
            sum_to_seven_count += 1

    # Calculate probabilities for each event
    probability_same_values = same_values_count / total_trials
    probability_sum_to_seven = sum_to_seven_count / total_trials

    # Print results out to the console in proper format 
    print(f"Number of events with the same values: {same_values_count}")
    print(f"Probability of same values: {probability_same_values:.4f}")

    print(f"\nNumber of events with values adding up to 7: {sum_to_seven_count}")
    print(f"Probability of sum to seven: {probability_sum_to_seven:.4f}")

if __name__ == "__main__":
    main()
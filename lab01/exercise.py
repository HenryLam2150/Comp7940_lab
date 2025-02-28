def find_factors(num):
    factors = []
    for i in range(1, num + 1):  # Loop from 1 to num inclusive
        if num % i == 0:          # Check if i is a factor of num
            factors.append(i)      # Add i to the list of factors
    return factors
if __name__ == '__main__':
    l = [52633, 8137, 1024, 999]
    factors_dict = {}

    for number in l:
        factors_dict[number] = find_factors(number)  # Store the factors in a dictionary

    # Print the factors for each number
    for number, factors in factors_dict.items():
        print(f"Factors of {number} are: {factors}")
import json
import requests

# URL to fetch JSON data
site = "https://api.npoint.io/2b57052af2060e84dc86"

# Function to convert elements to numbers
def convert_number(user_list):
    return [int(num) for num in user_list[1:]]  # Skip the first element (role)

# Function to replace specified numbers
def replace_number(number_list, being_replace, to_replace):
    return [to_replace if num == being_replace else num for num in number_list]

if __name__ == '__main__':

    # Fetching and loading JSON into text
    r = requests.get(site)
    data = r.json()
    print(data)

    text = data['users']

    # Debugging output
    for i in text:
        print("parse " + str(i))

    # Convert all elements (except the first one) into numbers
    y = convert_number(text[0])
    print("y")
    print(y)

    # Replace all number 1 by the number 10
    z = replace_number(number_list=y, being_replace=1, to_replace=10)
    print("z")
    print(z)

    # Calculate the sum of the modified list
    total_sum = sum(z)
    for i in z:
        print("sum = " + str(total_sum) + "; i =" + str(i))

    print("Total = " + str(total_sum))
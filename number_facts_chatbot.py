import requests

def get_number_fact(number):
    """Fetches a random fact about a number from the Numbers API."""
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Unable to fetch fact."

# Example usage
while True:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    if user_input.isdigit():
        fact = get_number_fact(user_input)
        print(fact)
    else:
        print("Please enter a valid number.")

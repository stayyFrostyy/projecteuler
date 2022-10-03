
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

def main():
    with open("Project Euler\Python\monkey.txt", 'r') as f:
        data = f.read()
    
    data = data.split("\n")
    data = [int(number) for number in data if number != ""]

    total = sum(data)
    
    return str(total)[:10]


print(main())
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

while True:
    print()
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye.")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice.")
        continue

    a_text = input("First number: ")
    b_text = input("Second number: ")

    try:
        a = float(a_text)
        b = float(b_text)
    except:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = sub(a, b)
    elif choice == "3":
        result = mul(a, b)
    else:
        result = div(a, b)

    print("Result:", result)

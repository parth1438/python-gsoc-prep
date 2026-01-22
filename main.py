def greet(name, age):
    return f"Hello, {name}, age {age}! Welcome to GSoC prep 🚀"

if __name__ == "__main__":
    user = input("Enter your name: ")
    age = input("Enter your age: ")
    print(greet(user, age))

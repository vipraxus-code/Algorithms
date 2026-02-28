def greet(name):
    print(f"Hello, {name}!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print(f"How are you, {name}?")

def bye():
    print("Bye!")

greet("Alexandr")
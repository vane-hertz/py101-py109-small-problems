def greetings(names, labels):
    welcome = "Hello, "
    welcome += ' '.join(names)
    welcome += "! Nice to have a "
    welcome += labels["title"] + " " + labels["occupation"]
    welcome += " around."
    return welcome

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
with open('data/alice.txt') as file:
    text = file.read()

    
num_rabbits = text.lower().split().count('rabbit')

print(f'Lewis Carroll uses the word "rabbit" {num_rabbits} times')
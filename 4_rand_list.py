import random

# rand head and tail
rand_num = random.randint(1, 10)
if rand_num % 2 == 0:
    print("Heads")
else:
    print("Tails")

# rand name
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))
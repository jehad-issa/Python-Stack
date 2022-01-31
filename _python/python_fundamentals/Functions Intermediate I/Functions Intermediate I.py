# 1
# import random
# def randInt():
#     print(int(random.random()*100))
# randInt()

# 2 randInt(max=100)
# import random
# def randInt():
#     print(int(random.random()*100))
# randInt()

# 3 randInt(min=50)
import random
def randInt():
    values = list(range(50,100))
    print(int(random.choice(values)))
randInt()

# randInt(min=50, max=100) returns a random integer between 50 and 100

# import random
# def randInt():
#     values = list(range(50,100))
#     print(random.choice(values))
# randInt()
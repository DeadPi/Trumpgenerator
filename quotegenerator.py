import random

part1=["Thank you","Putin", "Hillary", "Merkel", "The Democrats", "Mexico", "China", "Germany"]
part2=["has no talent", "on the way down", "will do something", "i hate it!", "looking like a fool"]
part3=["got destroyed by my ratings", "rigged the election", "had a much smaller crowd", "will pay for the wall"]
part4=["So sad", "Apologize", "So true", "Media won't tell you", "Big trouble", "Fantastic!", "Stay tuned!"]

bestWords = [part1, part2, part3, part4]
for i in range(0,4):
    print(bestWords[i][random.randint(0, len(bestWords[i])-1)])

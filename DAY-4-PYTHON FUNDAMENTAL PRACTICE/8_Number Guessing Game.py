secret=50
for i in range(5):
    n=int(input())
    if n<secret:
        print("Too Low")
    elif n>secret:
        print("Too High")
    else:
        print("Correct")
        break
else:
    print("Game Over")
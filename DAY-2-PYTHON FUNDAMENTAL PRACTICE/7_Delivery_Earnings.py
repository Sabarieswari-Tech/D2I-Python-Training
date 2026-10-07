n=int(input())
distances=list(map(int,input().split()))
total_distance=0
total_earnings=0
for d in distances:
    total_distance+=d
    if d<=5:
        earning=d*40
    else:
        earning=5*40+(d-5)*8
    total_earnings+=earning
average=total_distance/n
print(f"Total Distance: {total_distance:.2f} km")
print(f"Total Earnings: ₹{total_earnings:.2f}")
print(f"Average Distance: {average:.2f} km")
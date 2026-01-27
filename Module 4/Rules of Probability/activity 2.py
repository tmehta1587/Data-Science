

set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

union = set1.intersection(set2)

total_guests = list(union)

print("Total guests to be invited in party are :", len(total_guests))
print("Guest List:", total_guests)


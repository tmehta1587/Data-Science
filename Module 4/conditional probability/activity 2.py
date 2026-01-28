
def prob_a_and_b(a, b, total):
    
    prob_a = orange/total

    prob_bga = blue/(total-1)

    prob_AandB = prob_a * prob_bga

    return round(prob_AandB, 3)

orange = int(input("Enter number of orange balls"))
blue = int(input("Enter number of blue balls"))
total = orange+blue

print('Probability of Getting 1st orange and 2nd blue ball:')
print(prob_a_and_b(orange, blue, total))

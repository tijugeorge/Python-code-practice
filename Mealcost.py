mealCost = float(raw_input('Enter'))
tipPercent = int(raw_input())
taxPercent = int(raw_input())
def totalCost(T):
    tip = float(mealCost*(tipPercent/100))
    tax = float(mealCost*(taxPercent/100))
    totalCost = mealCost + tip + tax
    print 'The total cost of the order is: %r'%round(totalCost)
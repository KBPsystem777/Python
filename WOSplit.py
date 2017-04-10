
#Variables Declaration
budget = int(input("Enter Budget for 715: "))
w1 = int(input("Enter WO1 715 budget: "))
w2 = int(input("Enter WO2 715 budget: "))
w3 = int(input("Enter WO3 715 budget: "))
w4 = int(input("Enter WO4 715 budget: "))
w5 = int(input("Enter WO5 715 budget: "))
w6 = int(input("Enter WO6 715 budget: "))
w7 = int(input("Enter WO7 715 budget: "))
w8 = int(input("Enter WO8 715 budget: "))
w9 = int(input("Enter WO9 715 budget: "))
w10 = int(input("Enter WO10 715 budget: "))
w11 = int(input("Enter WO11 715 budget: "))
w12 = int(input("Enter W12 715 budget: "))
w13 = int(input("Enter W13 715 budget: "))


#Calculation
w1split = (w1/budget)
w2split = (w2/budget)
w3split = (w3/budget)
w4split = (w4/budget)
w5split = (w5/budget)
w6split = (w6/budget)
w7split = (w7/budget)
w8split = (w8/budget)
w9split = (w9/budget)
w10split = (w10/budget)
w11split = (w11/budget)
w12split = (w12/budget)
w13split = (w13/budget)


#Display output
print('''======Work Orders Split: ==========''')
print('Split for WO1 is: ', w1split)
print('Split for WO2 is: ', w2split)
print('Split for WO3 is: ', w3split)
print('Split for WO4 is: ', w4split)
print('Split for WO5 is: ', w5split)
print('Split for WO6 is: ', w6split)
print('Split for WO7 is: ', w7split)
print('Split for WO8 is: ', w8split)
print('Split for WO9 is: ', w9split)
print('Split for WO10 is: ', w10split)
print('Split for WO11 is: ', w11split)
print('Split for WO12 is: ', w12split)
print('Split for WO13 is: ', w13split)

#Updated: 4/10/2017
#Test Split
#This is to test the work orders split:
test_wo = int(w1split + w2split + w3split + w4split + 
w5split + w6split + w7split + 
w8split + w9split + w10split + 
w11split + w12split + w13split)
print('Work order split is: ', test_wo)




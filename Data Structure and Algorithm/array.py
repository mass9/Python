number = [1,020,30,40,50,60]
print(number[3]) # This is calls as random indexing -> O(1) if we know the index []

number[2] = "Prashant"
#for i in number:
 #   print(i)

#for i in range(len(number)):
  #  print(number[i])

print(number[0:-3])

#O(n) serach running time
maximum = number[1]
for num in number:
    if num > maximum:
        maximum = num
print(maximum)

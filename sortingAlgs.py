#initialize junk
import random
itemList = []
listLength = 0
#definitions
def SelectionSort():
    step = 1
    #for every item in the itemList
    for i in itemList:
        smallestNumber = len(itemList) + 1
        smallestNumberIndex = 0
        #find the smallest number in the itemList
        for number in itemList:
            if itemList.index(number) >= itemList.index(i):
                if number < smallestNumber or smallestNumberIndex == 0:
                    smallestNumber = number
                    smallestNumberIndex = itemList.index(number)
        #print the steps it takes to sort
        if not itemList[smallestNumberIndex] == itemList[itemList.index(i)]:
            print(str(step) + ". Swap " + str(itemList[smallestNumberIndex]) + " and " + str(itemList[itemList.index(i)]) + ".")
            #swap the smallest number with the current number
            itemList[smallestNumberIndex] = i
            itemList[itemList.index(i)] = smallestNumber
            step += 1
def BubbleSort():
    step = 1
    sortedPairs = 0
    while sortedPairs < len(itemList) - 1:
        for i in range(len(itemList) - 1):
            firstIndex = i
            secondIndex = i + 1
            if itemList[firstIndex] > itemList[secondIndex]:
                sortedPairs = 0
                print(str(step) + ". Swap " + str(itemList[firstIndex]) + " and " + str(itemList[secondIndex]) + ".")
                itemList[firstIndex], itemList[secondIndex] = itemList[secondIndex], itemList[firstIndex]
                step += 1
            else:
                sortedPairs += 1
#UI
print("How many items would you like to sort?")
listLength = int(input())
for i in range(listLength):
    itemList.append(i + 1)
random.shuffle(itemList)
print("Which algorithm?")
print("1 - Selection Sort")
print("2 - Bubble Sort")
choice = int(input())
print("Shuffled list:")
for printout in itemList:
    print(printout)
print("")
print("Steps:")
if choice == 1:
    SelectionSort()
if choice == 2:
    BubbleSort()
print("")
print("Sorted list:")
for printout in itemList:
    print(printout)

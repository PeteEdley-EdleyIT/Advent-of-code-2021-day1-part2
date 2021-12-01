measurments = []
count = 0
position = 0
threeMeasurments = []

with open('finalinput.txt') as file:
    for line in file:
        measurments.append(int(line.rstrip()))


while (position != len(measurments)-2) :
    threeMeasurments.append(measurments[position]+measurments[position+1]+measurments[position+2])
    position += 1


lastValue = threeMeasurments[0]

for position in range(1,len(threeMeasurments)):
    if (threeMeasurments[position] > lastValue):
        count += 1

    lastValue = threeMeasurments[position]

print(count)
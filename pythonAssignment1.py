import random
import numpy as np
import matplotlib.pyplot as plt
import csv

def genReadings(seed, amount):
    readings = np.empty(0)
    random.seed(seed)
    for i in range(amount):
        readings = np.append(readings, round(float(random.randint(min_sensor, max_sensor-1))+random.random(), 2 ))
    return readings

def analyzeReadings(data, threshold):
    d = np.array(data)
    print(np.size(d))
    print(np.mean(d))
    print(np.max(d))
    print(np.min(d))
    print(np.std(d))
    print(np.count_nonzero(d > threshold))

def plotReadings(data, threshold, block):
    d = np.array(data)
    l = np.arange(len(d))
    fig, ax = plt.subplots()
    ax.hlines(y=float(threshold), xmin=0, xmax=len(d), label='Threshold', colors='r', linestyles='dashed')
    ax.plot(l, d)
    ax.grid(visible=True)
    ax.title.set_text('Sensor Readings')
    ax.set_xlabel('Sample')
    ax.set_ylabel('Value')
    plt.show(block=block)

def plotHistogram(data, block):
    d = np.array(data)
    fig, hist = plt.subplots()
    hist.hist(data, bins=20, rwidth=0.75)
    hist.grid(visible=True)
    hist.title.set_text('Sensor Readings')
    hist.set_xlabel('Value')
    hist.set_ylabel('Frequency')
    plt.show(block=block)

def userInput(text, varType):
    while True:
        print(text)
        try:
            if varType == "int":
                return int(input())
            elif varType == "float":
                return float(input())
            elif varType == "str":
                return input()
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def genCSV(data, filename):
    d = np.array(data)
    with open(filename+'.csv', 'w', newline='') as csvfile:
        fieldnames = ['sample', 'reading']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(d)):
            writer.writerow({'sample': i, 'reading': d[i]})
        print("CSV file stored as "+filename+".csv")

sensor = userInput("Enter the sensor type:", "str")
reading_n = userInput("How many readings:", "int")
min_sensor = userInput("Minimum sensor value:", "int")
max_sensor = userInput("Maximum sensor value:", "int")
alert_threshold = userInput("Alert threshold:", "float")

output = genReadings(10, reading_n)
print(output)
analyzeReadings(output, alert_threshold)

while True:
    print("Generate CSV file? (y/n)")
    plot = str(input())
    if plot == 'y':
        print("Filename?")
        filename = input()
        genCSV(output, filename)
        break
    elif plot == 'n':
        break

plotReadings(output, alert_threshold, False)
plotHistogram(output, True)




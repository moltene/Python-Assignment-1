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
    print("Readings: "+str(np.size(d)))
    print("Mean: "+str(round(np.mean(d),2)))
    print("Maximum Value: "+str(np.max(d)))
    print("Minimum Value: "+str(np.min(d)))
    print("Standard Deviation: "+str(round(np.std(d),2)))
    print("Number of readings above threshold: "+str(np.count_nonzero(d > threshold)))
    print("Readings above threshold: "+str(d[d > threshold]))

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
            print("Invalid input. Enter valid value.")

def genCSV(data, filename):
    d = np.array(data)
    with open(filename+'.csv', 'w', newline='') as csvfile:
        fieldnames = ['sample', 'reading']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(d)):
            writer.writerow({'sample': i, 'reading': d[i]})
        print("CSV file stored as "+filename+".csv")

def loadCSV(filename):
    readings = np.empty(0)
    with open(filename+'.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            readings = np.append(readings, float(row['reading']))
    return readings

if __name__ == "__main__":
    print("SENSOR MONITOR")
    while True:
        print("Generate sensor data or load from CSV file? (g/l)")
        setting = str(input())
        if setting == 'g':
            sensor = userInput("Enter the sensor type:", "str")
            while True:
                reading_n = userInput("How many readings:", "int")
                if reading_n > 0: break
                else: print("Cannot have less than 1 reading. Enter valid value")
            min_sensor = userInput("Minimum sensor value:", "int")
            while True:
                max_sensor = userInput("Maximum sensor value:", "int")
                if max_sensor > min_sensor: break
                else: print("Maximum sensor value cannot be lower than minimum value. Enter valid value.")
            alert_threshold = userInput("Alert threshold:", "float")

            output = genReadings(10, reading_n)
            break
        elif setting == 'l':
            print("Filename?")
            filename = input()
            output = loadCSV(filename)
            alert_threshold = userInput("Alert threshold:", "float")
            print("Readings loaded from "+filename+".csv")
            break
        else:
            print("Invalid input. Enter valid value.")

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




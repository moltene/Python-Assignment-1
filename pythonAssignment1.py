import random
import numpy as np
import matplotlib.pyplot as plt

readings = np.empty(0)

def genReadings(seed, amount):
    readings = np.empty(0)
    random.seed(seed)
    for i in range(amount):
        readings = np.append(readings, float(random.randint(min_sensor, max_sensor-1))+random.random())
    return readings

def analyzeReadings(data, threshold):
    d = np.array(data)
    print(np.size(d))
    print(np.mean(d))
    print(np.max(d))
    print(np.min(d))
    print(np.std(d))
    print(np.count_nonzero(d > threshold))

def plotReadings(data, threshold):
    d = np.array(data)
    l = np.arange(len(d))
    fig, ax = plt.subplots()
    ax.hlines(y=float(threshold), xmin=0, xmax=len(d), label='Threshold', colors='r', linestyles='dashed')
    ax.plot(l, d)
    plt.show()

def plotHistogram(data):
    d = np.array(data)
    fig, hist = plt.subplots()
    hist.hist(data, bins=len(d))
    plt.show()

print("Enter the sensor type:")
sensor = input()
print("Sensor type:", sensor)
print("How many readings:")
reading_n = int(input())
print("Readings:", reading_n)
print("Minimum sensor value:")
min_sensor = int(input())
print("Minimum sensor value:", min_sensor)
print("Maximum sensor value:")
max_sensor = int(input())
print("Maximum sensor value:", max_sensor)
print("Alert threshold:")
alert_threshold = float(input())
print("Alert threshold:", alert_threshold)

output = genReadings(10, reading_n)
print(output)
analyzeReadings(output, alert_threshold)
plotReadings(output, alert_threshold)
plotHistogram(output)


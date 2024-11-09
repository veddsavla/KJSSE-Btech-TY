import os

processNum = int(input("Enter number of processes: "))
currentTime = 0

arrivalTime = []
burstTime = []
completionTime = [0] * processNum
turnaroundTime = [0] * processNum
waitTime = [0] * processNum

for i in range(processNum):
    arrivalTime.append(int(input(f'Enter arrival time for process {i+1}: ')))
    burstTime.append(int(input(f'Enter burst time for process {i+1}: ')))

print(f'1. FCFS\n2. SJF')
choice = int(input(f'Which scheduling algorithm do you want to run: '))
os.system('cls')

if choice == 1:
    tempArrivalTime = arrivalTime.copy()
    if min(tempArrivalTime) != 0:
        currentTime += min(tempArrivalTime)
    
    for i in range(processNum):
        currentProcess = tempArrivalTime.index(min(tempArrivalTime))
        tempArrivalTime[currentProcess] = 999
        currentTime += burstTime[currentProcess]
        completionTime[currentProcess] = currentTime

elif choice == 2:
    tempArrivalTime = arrivalTime.copy()
    readyQueue = []
    
    if min(tempArrivalTime) != 0:
        currentTime += min(tempArrivalTime)
    
    while 0 in completionTime:
        readyQueue = []
        for j in range(processNum):
            if tempArrivalTime[j] <= currentTime and completionTime[j] == 0:
                readyQueue.append(j)
        if not readyQueue:
            currentTime += 1
            continue
        sjf = 1000
        for j in readyQueue:
            if sjf > burstTime[j]:
                sjf = burstTime[j]
                currentProcess = j
        readyQueue.remove(currentProcess)
        tempArrivalTime[currentProcess] = 999
        currentTime += burstTime[currentProcess]
        completionTime[currentProcess] = currentTime

for i in range(processNum):
    turnaroundTime[i] = completionTime[i] - arrivalTime[i]
    waitTime[i] = turnaroundTime[i] - burstTime[i]

avgTurnaroundTime = sum(turnaroundTime) / processNum
avgWaitTime = sum(waitTime) / processNum

print(f'Turn around time for all processes is {turnaroundTime}')
print(f'Wait time for all processes is {waitTime}')
print(f'Average turn around time is {avgTurnaroundTime}')
print(f'Average wait time is {avgWaitTime}')

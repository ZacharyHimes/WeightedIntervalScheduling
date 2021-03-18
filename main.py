# store the requests on a csv file {start, finish, value}
# Find maximum weight subset of mutually compatible jobs.
# input number of jobs n = 4
# job Details {start Time, Finish Time, importance weight}
# Job 1: 0, 3, 1
# Job 2: 2, 5, 2
# Job 3: 4, 7, 3
# Job 4: 6, 9, 4
# Job 4: 8, 11, 5

import csv
from operator import attrgetter
from tabulate import tabulate

class Job:
    def __init__(self, start, end, weight):
        self.start = int(start)
        self.end = int(end)
        self.weight = int(weight)


jobs = []
with open('job2.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        jobs.append(Job(row[0], row[1], row[2]))
sorted_jobs = sorted(jobs, key=attrgetter('end'))
index = (len(sorted_jobs))
index = index - 1


def ComputeP(index):
    p = [0] * (index)
    j = index - 1
    z = index - 2
    while j >= 0:
        if sorted_jobs[j].start <= 0 or z < 0:
            p[j] = -1
            j = j - 1
            z = j - 1
        elif sorted_jobs[j].start >= sorted_jobs[z].end:
            p[j] = z
            j = j - 1
            z = j - 1
        else:
            z = z - 1
    return p


M = [None] * (index + 1)
M[0] = sorted_jobs[0].weight
p2 = ComputeP(len(sorted_jobs))


def ComputeOpt(j):
    if j == -1:
        return 0
    elif M[j] is not None:
        return M[j]
    else:
        M[j] = max(sorted_jobs[j].weight + ComputeOpt(p2[j]), ComputeOpt(j-1))
        M[j-1] = sorted_jobs[j-1].weight + ComputeOpt(p2[j-1])
    return M[j]


def FindSolution(j):
    if j <= 0:
        return
    elif sorted_jobs[j].weight + M[p2[j]] > M[j - 1]:
        print("Index:",j ," Start Time: ",sorted_jobs[j].start, "| End Time: ", sorted_jobs[j].end ,"| Duration: ", sorted_jobs[j].weight)
        FindSolution(p2[j])
    else:
        FindSolution(j - 1)


ComputeOpt(index)
print("\n")
print("CSV file loaded: {start, end, duration}")
for i in sorted_jobs:
    print(i.start, i.end, i.weight)
print("--------------------------")
print("\n\n")
print("List of Jobs to get the optimal amount of work done: ")
print("-----------------------------------------------------")
FindSolution(index)



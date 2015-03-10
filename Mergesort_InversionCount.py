"""
David Schonberger
Coursera/Stanford course by Tim Roughgarden
Algorithms: Design and Analysus, Part I
Programming Assignment 1 - Inversion Count via Mergesort
Created: 1/28/2015

Reads in a file of the integers 1..100000 randomly permuted
Counts the number of inversions
"""
def mergeSort(lst, c):
    if len(lst) < 2:
        return lst
    m = len(lst) / 2
    return merge(mergeSort(lst[:m], c), mergeSort(lst[m:], c), c)
    
def merge(l, r, c):
    res = []
    while(l and r):
        if(l[0] <= r[0]):
            s = l
        else:
            s = r
        res.append(s.pop(0))
        if(s == r and not s == l):
            c[0] += len(l)
            
    res.extend(l if l else r)
    return res

p = "C:/Users/David/Documents/TechStuff/OnlineCourses/Coursera/Algos_DesignAndAnalysis_PartI_Roughdarden_sp2015/Week1/"
fn = "IntegerArray.txt"

lst = []
with open(p+fn) as f:
    for line in f:
        l = int(line.strip('\n'))
        lst.append(l)

count = [0]
r =  mergeSort(lst, count)
print count[0]

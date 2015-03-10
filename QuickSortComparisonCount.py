"""
David Schonberger
Coursera/Stanford course by Tim Roughgarden
Algorithms: Design and Analysus, Part I
Programming Assignment 2 - Comparison Count in Quicksort
Created: 2/1/2015

Reads in a file of the integers 1..100000 randomly permuted
Counts the number of comparisons done in Partition subroutine
of Quicksort.
Counts in three cases of how pivot is chosen:
1. Use first elt
2. Use last elt
3. Use 'median of three'
"""

def quicksort(a, lo, hi):
    global count
    if(hi < lo + 1):
        return a
    m = 2
    a = choose_pivot(a, lo, hi, m)
    pividx = partition(a, lo, hi)
    count +=  hi - lo
    quicksort(a, lo, pividx - 1)
    quicksort(a, pividx + 1, hi)
    

def swap(a , lo_idx, hi_idx):
    tmp = a[lo_idx]
    a[lo_idx] = a[hi_idx]
    a[hi_idx] = tmp
    return a

def choose_pivot(a, lo, hi, method = 0):
    """
    input: 
    -a , the list of numbers
    -lo and hi, the leftmost and rightmost indices
    - method, 0, 1, or 2 to indicate how pivot is chosen:
      0 -> choose first elt
      1 -> choose last elt
      2 -> choose median of three
    selects pivot based on method then swaps pivot into
    first elt of a
    """
    if(method == 1):
        a = swap(a, lo, hi)
    elif(method == 2):
        elo = a[lo]
        ehi = a[hi]
        l = hi - lo + 1
        if(l % 2 == 0):
            emid = a[lo + l/2 - 1]
        else:
            emid = a[lo + l/2]
        tmparr = list([elo, ehi, emid])
        tmparr.sort()
        median = tmparr[1] #median of three
        piv_idx = a.index(median)
        a = swap(a, lo, piv_idx)
        
    return a
    
  
def partition(a, lo, hi):
    p = a[lo]
    i = lo + 1
    for j in range(lo + 1 , hi + 1):
        if(a[j] <= p):
            a = swap(a, j, i)
            i += 1
    a = swap(a, lo, i - 1)
    return i - 1

p = "C:/Users/David/Documents/TechStuff/OnlineCourses/Coursera/Algos_DesignAndAnalysis_PartI_Roughdarden_sp2015/Week2/"
fn = "QuickSort.txt"

arr = []
with open(p+fn) as f:
    for line in f:
        l = int(line.strip('\n'))
        arr.append(l)


count = 0
quicksort(arr, 0, len(arr)-1)
print count
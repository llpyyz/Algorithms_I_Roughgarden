"""
David Schonberger
3/8/2015
Roughgarden Algorithms I
HW 6 - Median Maintenance
Uses double heap, h_lo and h_hi
h_lo holds left half of data, h_hi holds right half.

Every element in h_lo is <= every elt in h_hi.

The median so far is always the root of one of the
two heaps.

H_lo stores negative of given number, so then extract_min
on h_lo produces the max element among the low half. 

Also, extract_min on h_hi produces the min elt of the upper
half.

Initial elet always stored in h_lo.

The curr elt processed after first elt is compared
to root of h_lo. If <=, inset into h_lo, else insert
into h_hi.

If abs(len(h_lo) - len(h_hi)) > 1, need to rebalance by removing
root of one and inserting into other heap.

Implementation of Heap data structure
Uses an array to hold data
Implements the following operations:
Done:
1. Insert(key) - insert the given key in proper place
2. Extract-Min - remove min (root)
3. Delete(key) - delete key from arbitrary place in heap

To do:
4. Heapify(list) - quick way to create initial heap
"""
import random
import datetime

#when one has 2 more elts than other, rebalance
def rebalanceHeaps(h1 , h2):
    if(len(h1) > len(h2)):
        elt = heapExtractMin(h1)
        heapInsert(h2,-elt)
    else:
        elt = heapExtractMin(h2)
        heapInsert(h1,-elt)

#helper fcn to calculate parent node index
def calcParent(i):
    if(i <= 1):
        return 0
    elif(i % 2 == 0):
        return i/2 - 1
    else:
        return i/2

#helper fcn to swap a child and its parent
def bubble(heap, p , c):
    tmp = heap[p]
    heap[p] = heap[c]
    heap[c] = tmp
    return heap

def heapInsert(heap, key):
    if(len(heap) == 0):
        heap.append(key)
    else:
        heap.append(key) #add to end of list
        key_idx = len(heap) - 1
        p = calcParent(key_idx) #parent of key
        while(p >= 0 and heap[p] > key):
            heap = bubble(heap , p , key_idx)
            key_idx = p
            p = calcParent(key_idx)
            
        
    return heap

#input: l = size of heap, i = node index
#output: true if node at index i has two children, else false
def hasTwoChildren(l, i):
    return l >= 2 * i + 3

#return index of smaler child of heap[i]
#if heap[i] is a leaf, returns i since it has no children
def findIndexOfMinChild(heap, i):
    if isLeaf(len(heap) , i):
        childIdx = i
    elif(hasTwoChildren(len(heap), i)):
        if(heap[2 * i + 1] <= heap[2 * i + 2]):
            childIdx = 2 * i + 1
        else:
            childIdx = 2 * i + 2
    else:
        childIdx = 2 * i + 1
        
    return childIdx

def isLeaf(l, i):
    return l < 2 * i + 2

def heapExtractMin(heap):
    if(len(heap) <= 2):
        minval = heap.pop(0)
    else:
        minval = heap[0] #min to be returned
        heap[0] = heap.pop() #move last leaf to root
        i = 0
        minChildIdx = findIndexOfMinChild(heap, i)
        while(heap[i] > heap[minChildIdx]):
            bubble(heap, i, minChildIdx)
            i = minChildIdx
            minChildIdx = findIndexOfMinChild(heap, i)
            
    return minval

def heapDelete(heap, key):
    if(key in heap):
        idx = heap.index(key)
        if(idx == 0):
            heapExtractMin(heap)
        elif(idx == len(heap) - 1):
            heap.pop()
        else:
            heap[idx] = heap.pop() #move last elt to deleted space
            
            #either bubble up if needed...            
            p = calcParent(idx)
            while(heap[p] > heap[idx]):
                bubble(heap, p, idx)
                idx = p
                p = calcParent(idx)
                
            #or bubble down if needed
            minChildIdx = findIndexOfMinChild(heap, idx)
            while(heap[idx] > heap[minChildIdx]):
                bubble(heap, idx, minChildIdx)
                idx = minChildIdx
                minChildIdx = findIndexOfMinChild(heap, idx)

def heapHeapify(arr):
    pass

p = "C:/Users/David/Documents/TechStuff/OnlineCourses/Coursera/Algos_DesignAndAnalysis_PartI_Roughdarden_sp2015/Week6/"
fn = "Median_5.txt"
#fn = "Median_10.txt"
#fn = "Median_17.txt"
#fn = "Median.txt"

l = []
data = open(p+fn,"r")
for x in data:
    l.append(int(x))

#print l

l = []
size = 10000
random.seed(11)

for i in range(size):
    l.append(random.randint(1,1000))
    

bef = datetime.datetime.now()

h_lo = []
h_hi = []
mod = 10000
median_sum = 0
for i in range(len(l)):
    #print "inserting", l[i]
    if(i == 0):
        h_lo = heapInsert(h_lo , -l[0])
        median_sum  = (median_sum + l[0]) % mod
    else:
        if(l[i] <= -h_lo[0]):
            h_lo = heapInsert(h_lo, -l[i])
        else:
            h_hi = heapInsert(h_hi, l[i])
        if(abs(len(h_lo) - len(h_hi)) > 1):
            rebalanceHeaps(h_lo, h_hi)
            
        if(i % 2 == 1 or len(h_lo) > len(h_hi)):
            median_sum  = (median_sum - h_lo[0]) % mod
        else:
            median_sum  = (median_sum + h_hi[0]) % mod
    
    #print h_lo, h_hi, median_sum,"\n***\n"
    

print median_sum

aft = datetime.datetime.now()
print "et:",aft - bef

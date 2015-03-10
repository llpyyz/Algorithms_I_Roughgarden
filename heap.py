"""
David Schonberger
2/24/2015
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


l = []
size = 13
random.seed(8)

for i in range(size):
    l.append(random.randint(1,100))
    
print l

h = []
for i in range(len(l)):
    
    h = heapInsert(h,l[i])
    print h

print "min:" , heapExtractMin(h), h

h = heapInsert(h, random.randint(1,100))

print h

rndidx = random.randint(0,len(h) - 1)
print "deleting item" ,h[rndidx], " at index", rndidx

heapDelete(h,h[len(h)-1])

print h


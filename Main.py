import time
import random
import matplotlib.pyplot
import copy
import math

maxNumbers = 300 + 1
maxIntv = 99


def bubbleSort(L):

    tStart = time.perf_counter()

    swapped = True

    while swapped == True:
        swapped = False
        for i in range(0, len(L)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True

    tEnd = time.perf_counter()
    tSum = tEnd - tStart

    return tSum


def insertionSort(Lst):
    tStart = time.perf_counter()

    for i in range(1, len(Lst)):
        ele = Lst[i]
        index_left = i-1
        while index_left > -1 and Lst[index_left] > ele:
            Lst[index_left + 1] = Lst[index_left]
            Lst[index_left] = ele
            index_left = index_left - 1

    tEnd = time.perf_counter()
    tSum = tEnd - tStart

    return tSum


def selectionSort(Lst):

    tStart = time.perf_counter()

    temp = 0
    for i in range(len(Lst)):
        minIndex = i
        for e in range(i, len(Lst)):
            if Lst[minIndex] > Lst[e]:
                minIndex = e

        temp = Lst[i]
        Lst[i] = Lst[minIndex]
        Lst[minIndex] = temp

    tEnd = time.perf_counter()
    tSum = tEnd - tStart

    return tSum


def mergeSortedLists(A, B):
    newList= list()
    a = 0; b = 0
    # Füge beide Listen zusammen bis eine leer ist("Mischen")
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            newList.append(A[a])
            a += 1
        else:
            newList.append(B[b])
            b += 1
    while a < len(A): # Wenn Liste A mehr Komponentenenthält, hänge diese an die neue Liste
        newList.append(A[a])
        a += 1
    while b < len(B): # Wenn Liste B mehr Komponenten enthält, hänge diese an die neue Liste
        newList.append(B[b])
        b += 1

    return newList

def mergeSort(A):

    if len(A) <= 1: # Basisfall
        return A

    else:
        mid = math.floor(len(A)/2)

        leftHalf = mergeSort(A[:mid])
        rightHalf = mergeSort(A[mid:])

        newList = mergeSortedLists(leftHalf, rightHalf)

    return newList

def quickSort(A):

    tStart = time.perf_counter()

    n = len(A)
    recQuickSort(A, 0, n-1)

    tEnd = time.perf_counter()
    tSum = tEnd - tStart

    return tSum

def recQuickSort(A, first, last):
    if first >= last:
        return
    else:
        pivot = A[first]
        pivotPos = partitionArray(A, first, last)

        recQuickSort(A, first, pivotPos-1)
        recQuickSort(A, pivotPos+ 1, last)

def partitionArray(A, first, last):
    pivot = A[first]
    left = first + 1
    right = last
    while left <= right: # solange Partitionierung nicht abgeschlossen
        while (left <= right) and (A[left] < pivot):# finde Schl�ssel gr��er Pivot
            left += 1
        while (right >= left) and (A[right] >= pivot): # finde Schl�ssel kleiner Pivot
            right -= 1
        if left < right:# vertausche beide Schl�ssel falls Partitionierung noch nicht beendet
            A[left], A[right] = A[right], A[left]
    if right != first: # Pivot-Element an die richtigeStellebringen
        A[first] = A[right]
        A[right] = pivot

    return right # liefere Position des Pivot-Elements zur�ck

def createList(maxNumbers):
    iList = [random.randint(0, maxIntv) for i in range(0, maxNumbers)]

    return iList


def testListsGenerator(maxNumbers):
    lst = []
    for i in range(0, maxNumbers):
        lst.append(createList(i))

    return lst


def tMeasure(aList):
    lstTime = []  # Liste mit Laufzeiten abhaengig von der Laenge der Liste

    for i in aList:
        s = time.perf_counter()
        mergeSort(i)
        e = time.perf_counter()
        diff = e - s
        lstTime.append(diff)

    return lstTime


def plot():
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)

    originalLst = testListsGenerator(maxNumbers)
    bubbleList = copy.deepcopy(originalLst)
    insertionList = copy.deepcopy(originalLst)
    selectionList = copy.deepcopy(originalLst)
    mergeList = copy.deepcopy(originalLst)
    quickList = copy.deepcopy(originalLst)

    ax.plot([i for i in range(0, maxNumbers)], [bubbleSort(j) for j in bubbleList], '.', color='r', )
    ax.plot([i for i in range(0, maxNumbers)], [insertionSort(j) for j in insertionList], '.',
            color='g')
    ax.plot([i for i in range(0, maxNumbers)], [selectionSort(j) for j in selectionList], '.',
            color='b', )
    ax.plot([i for i in range(0, maxNumbers)], [quickSort(j) for j in quickList], '.', color='m', )
    ax.plot([i for i in range(0, maxNumbers)], tMeasure(mergeList), '.', color='y', )

    ax.set_title("Elemente in Liste")
    ax.legend(['BubbleSort', 'InsertionSort', 'SelectionSort', 'QuickSort', 'MergeSort'])
    ax.set_xlabel('Anzahl Elemente in Liste')
    ax.set_ylabel('Zeit in s')

    matplotlib.pyplot.show()


def main():
    plot()

main()
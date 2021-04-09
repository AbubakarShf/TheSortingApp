from tkinter import *
import random
import time
import tkinter as tk

# Global Array
Array = []
ArrayBackup1 = []
start_time = 0
flag=1

# Functions

def Reset():
	global flag
	global Array
	global ArrayBackup1
	Array=[]
	ArrayBackup1=[]
	flag=1
	InputArraySize.delete(0,END)
	InputMaxNum.delete(0, END)
	InputMinNum.delete(0, END)
	TextRandomArray.delete("1.0","end")
	TextSortedArray.delete("1.0","end")
	TimeQuickSort.delete("1.0","end")
	TimeHeapSort.delete("1.0","end")
	TimeCountingSort.delete("1.0","end")
	TimeInsertionSort.delete("1.0","end")

def Logic():
	global flag
	if(flag<=1):
		for i in range(0, int(InputArraySize.get())):
			Array.append(random.randint(int(InputMinNum.get()), int(InputMaxNum.get())))
		global ArrayBackup1
		ArrayBackup1 = Array

		for i in range(len(Array)):
			TextRandomArray.insert(tk.END, str(Array[i]) + ', ')
	flag=flag+1

def InsertionSort(arr):

	for i in range(1, len(arr)):

		key = arr[i]

		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key
def InsertionSortSubFunc():
	TimeInsertionSort.delete("1.0", "end")
	TextSortedArray.delete("1.0", "end")
	Array=ArrayBackup1
	start_time = time.time()
	InsertionSort(Array)
	end_time = time.time()
	TotalTime = end_time - start_time
	TimeInsertionSort.insert(tk.END, str(TotalTime) + ' sec')
	for i in range(len(Array)):
		TextSortedArray.insert(tk.END, str(Array[i]) + ', ')

def partition(arr, low, high):
	i = (low - 1)  # index of smaller element
	pivot = arr[high]  # pivot

	for j in range(low, high):

		if arr[j] < pivot:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return (i + 1)


def quickSort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi - 1)
		quickSort(arr, pi + 1, high)


def QuickSortSubFunc():
	TimeQuickSort.delete("1.0", "end")
	TextSortedArray.delete("1.0", "end")
	Array=ArrayBackup1
	start_time = time.time()
	quickSort(Array, 0, len(Array) - 1)
	end_time = time.time()
	Cal_Time = end_time - start_time

	for i in range(0, len(Array)):
		TextSortedArray.insert(tk.END, str(Array[i]) + ', ')

	TimeQuickSort.insert(tk.END, str(Cal_Time)+' sec')

def CountingSort(array, maxval):
	n = len(array)
	m = maxval + 1
	count = [0] * m               # init with zeros
	for a in array:
		count[a] += 1             # count occurences
	i = 0
	for a in range(m):            # emit
		for c in range(count[a]): # - emit 'count[a]' copies of 'a'
			array[i] = a
			i += 1
	return array

def CountingSortSubFunc():
	TimeCountingSort.delete("1.0", "end")
	TextSortedArray.delete("1.0", "end")
	Array=ArrayBackup1
	Max = 0
	for i in range(0, len(Array)):
		if (Max < Array[i]):
			Max = Array[i]

	start_time = time.time()
	CountingSort(Array,Max)
	end_time = time.time()
	Cal_Time = end_time - start_time
	for i in range(0, len(Array)):
		TextSortedArray.insert(tk.END, str(Array[i]) + ', ')
	TimeCountingSort.insert(tk.END, str(Cal_Time)+' sec')

# Heap Sort Function
def heapify(arr, n, i):
	# Find largest element among root and children
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	# If root is not largest, swap with largest
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)

def HeapSort(arr):
	n = len(arr)

	# Build max heap
	for i in range(n // 2, -1, -1):
		heapify(arr, n, i)

	for i in range(n - 1, 0, -1):
		# Swap
		arr[i], arr[0] = arr[0], arr[i]

		# Heapify root element
		heapify(arr, i, 0)

def HeapSortSubFunc():
	TimeHeapSort.delete("1.0", "end")
	TextSortedArray.delete("1.0", "end")
	Array=ArrayBackup1

	start_time = time.time()
	HeapSort(Array)
	end_time = time.time()
	Cal_Time = end_time - start_time
	for i in range(0, len(Array)):
		TextSortedArray.insert(tk.END, str(Array[i]) + ', ')
	TimeHeapSort.insert(tk.END, str(Cal_Time)+' sec')


# GUI
window = Tk()
window.configure(background='grey')
window.title("Algo Project")
LabelAppName = Label(window, text="Welcome to Sorting Project", font=("Roboto", 20, "bold"), width=80).grid(row=0,
																											column=0)
LabelSize = Label(window, text="Array Size: ", font=("Roboto", 15, "bold"), fg='black', bg='grey')
LabelSize.place(x=80, y=100)
InputArraySize = Entry(window, widt=20, font=("Roboto", 15, "bold"))
InputArraySize.place(x=170, y=130)

LabelMinNum = Label(window, text="Min Num: ", font=("Roboto", 15, "bold"), fg='black', bg='grey')
LabelMinNum.place(x=80, y=200)
InputMinNum = Entry(window, widt=9, font=("Roboto", 15, "bold"))
InputMinNum.place(x=190, y=200)

LabelMaxNum = Label(window, text="Max Num: ", font=("Roboto", 15, "bold"), fg='black', bg='grey')
LabelMaxNum.place(x=320, y=200)
InputMaxNum = Entry(window, widt=9, font=("Roboto", 15, "bold"))
InputMaxNum.place(x=420, y=200)

TextRandomArray = Text(window, width=40, height=6, font=("Roboto", 15, "bold"))
TextRandomArray.place(x=180, y=320)
BtnRandomArr = Button(window, text="Random Array: ", command=lambda: Logic(), font=("Roboto", 15, "bold"), fg='white',
					  bg='black')
BtnRandomArr.place(x=80, y=270)

LabelSortingTech = Label(window, text="~Sorting Methodes~ ", font=("Roboto", 20, "bold"), fg='black', bg='grey')
LabelSortingTech.place(x=900, y=100)

BtnCountingSort = Button(window, text="Counting Sort: ",command=lambda : CountingSortSubFunc(),font=("Roboto", 14, "bold"),
						 fg='white', bg='black', )
BtnCountingSort.place(x=860, y=190)
TimeCountingSort = Text(window, width=10, height=1, font=("Roboto", 15, "bold"))
TimeCountingSort.place(x=1100, y=195)

BtnHeapSort = Button(window, text="Heap Sort: ",command=lambda : HeapSortSubFunc(),font=("Roboto", 14, "bold"), fg='white', bg='black')
BtnHeapSort.place(x=860, y=250)
TimeHeapSort = Text(window, width=10, height=1, font=("Roboto", 15, "bold"))
TimeHeapSort.place(x=1100, y=250)

BtnInsertionSort = Button(window, text="Insertion Sort: ", font=("Roboto", 14, "bold"), fg='white', bg='black',
						  command=lambda: InsertionSortSubFunc())
BtnInsertionSort.place(x=860, y=310)
TimeInsertionSort = Text(window, width=10, height=1, font=("Roboto", 15, "bold"))
TimeInsertionSort.place(x=1100, y=310)

BtnQuickSort = Button(window, text="Quick Sort: ", command=lambda: QuickSortSubFunc(), font=("Roboto", 14, "bold"),
					  fg='white', bg='black')
BtnQuickSort.place(x=860, y=370)
TimeQuickSort = Text(window, width=10, height=1, font=("Roboto", 15, "bold"))
TimeQuickSort.place(x=1100, y=370)

TextSortedArray = Text(window, width=40, height=6, font=("Roboto", 15, "bold"))
TextSortedArray.place(x=180, y=540)

LabelSortedArray = Label(window, text="~Sorted Array~ ", font=("Roboto", 20, "bold"), fg='black', bg='grey')
LabelSortedArray.place(x=90, y=490)

BtnReset=Button(window, text="Reset", command=lambda: Reset(),width=10, font=("Roboto", 14, "bold"),
					  fg='white', bg='black')
BtnReset.place(x=1040, y=640)

window.geometry("1300x760")
window.mainloop()

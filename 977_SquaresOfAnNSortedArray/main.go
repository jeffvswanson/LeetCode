package main

/*
Leetcode problem 977, Squares of an N-sorted Array

Given an array of integers A sorted in non-decreasing order, return 
an array of the squares of each number, also in sorted non-decreasing order.

Example:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
*/

import "fmt"

func main() {
	inputSlice := []int {-20, -10, -4, -1, 0, 3, 10}
	fmt.Printf("The original array is %v.", inputSlice)
	inputSlice = sortedSquares(inputSlice)
	fmt.Printf("\nThe squared and sorted array is %v.", inputSlice)
}

func sortedSquares(A []int) []int {
	for idx, val := range A {
	  A[idx] = val * val
	}
	A = divideAndConquer(A)
	return A
  }
  
  func divideAndConquer(A []int) []int {
	// Base case: if the length of A is one or empty the slice is sorted 
	// by default
	if len(A) < 2 {
	  return A
	}
	
	a := divideAndConquer(A[0:len(A)/2])
	b := divideAndConquer(A[len(A)/2:])
	
	sortedSlice := mergeSort(a, b)
	
	return sortedSlice
  }
  
  func mergeSort(a, b []int) []int {
	mergedSlice := make([]int, len(a) + len(b))
	// Set up the indices for arrays a and b
	var i, j int
	
	
	for k := 0; k < len(mergedSlice); k++ {
	  // Check if an array is out of elements and copy of the rest of 
	  // the elements left in the other array
	  if i >= len(a) {
		for j < len(b) {
		  mergedSlice[k] = b[j]
		  j++
		  // Increment k since this is an inner loop
		  k++
		}
		break
	  } else if j >= len(b) {
		for i < len(a) {
		  mergedSlice[k] = a[i]
		  i++
		  k++
		}
		break
	  }
	  
	  // Merge the slices
	  if a[i] <= b[j] {
		mergedSlice[k] = a[i]
		i++
	  } else {
		mergedSlice[k] = b[j]
		j++
	  }
	}
	
	return mergedSlice
  }
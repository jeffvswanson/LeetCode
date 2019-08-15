package main

/*
https://leetcode.com/problems/sort-array-by-parity/, accessed 28 March 2019

Given an array A of non-negative integers, return an array consisting of all
the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
*/

import "fmt"

func main() {
	A := []int{3, 1, 2, 4, 8, 7, 6, 2, 3, 4, 8, 9}
	fmt.Println("The input array is", A)

	A = sortArrayByParity(A)

	fmt.Println("The parity sorted array is", A)
}

func sortArrayByParity(A []int) []int {
	// Create an empty slice to copy values
	parityArray := make([]int, len(A))
	// Create slice indices
	evenIndex := 0
	oddIndex := len(A) - 1

	for _, val := range A {
		if val%2 == 0 {
			parityArray[evenIndex] = val
			evenIndex++
		} else {
			parityArray[oddIndex] = val
			oddIndex--
		}
	}

	return parityArray
}

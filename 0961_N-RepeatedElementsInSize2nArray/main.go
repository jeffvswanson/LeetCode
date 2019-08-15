package main

import "fmt"

/*
From leetcode.com
In an array A of size 2N, there are N+1 unique elements, and exactly one of
these elements is repeated N times.

Return the element repeated N times.
*/

func main() {
	inputArray := []int{5, 1, 5, 2, 5, 3, 5, 4}

	fmt.Printf("The element repeated exactly n time in the array is %d.",
		repeatedNTimes(inputArray))
}

func repeatedNTimes(A []int) int {

	// Assign element as -1 to track errors
	findElement := -1

	n := len(A) / 2
	m := make(map[int]int)

	for _, item := range A {
		m[item]++
	}

	for key, value := range m {
		if value == n {
			findElement = key
		}
	}
	return findElement
}

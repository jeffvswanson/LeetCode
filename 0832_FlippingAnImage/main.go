package main

/*
https://leetcode.com/problems/flipping-an-image/, accessed 31 March 2019

Given a binary matrix A, we want to flip the image horizontally, then invert
it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced
by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
*/

import "fmt"

func main() {
	A := [][]int{{1, 1, 0, 0}, {1, 0, 0, 1}, {0, 1, 1, 1}, {1, 0, 1, 0}}

	fmt.Println("The initial setup is:")
	fmt.Println(A)

	A = flipAndInvertImage(A)

	fmt.Println("The flipped and inverted slice is:")
	fmt.Println(A)
}

func flipAndInvertImage(A [][]int) [][]int {

	// Iterate over the rows of A
	for rowIndex, row := range A {
		// Get the last index position in the row
		endIndex := len(row) - 1
		// Iterate over each value in the row, column position
		for colIndex, val := range row {
			// Stop, the pointers have crossed.
			if colIndex > endIndex {
				break
			}

			// Swap the values
			tmp := val
			A[rowIndex][colIndex] = A[rowIndex][endIndex]
			A[rowIndex][endIndex] = tmp

			// Invert the values
			if A[rowIndex][colIndex] == 0 {
				A[rowIndex][colIndex] = 1
			} else if A[rowIndex][colIndex] == 1 {
				A[rowIndex][colIndex] = 0
			}

			// Before the loop ends endIndex = rowIndex
			// At this point we would invert the value twice.
			// Decrement and continue the loop to break out of the loop.
			if endIndex == colIndex {
				endIndex--
				continue
			}

			if A[rowIndex][endIndex] == 0 {
				A[rowIndex][endIndex] = 1
			} else if A[rowIndex][endIndex] == 1 {
				A[rowIndex][endIndex] = 0
			}

			endIndex--
		}
	}

	return A
}

package main

/*
https://leetcode.com/problems/hamming-distance/, accessed 11 May 2019

The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are
different.
*/

import (
	"fmt"
	"strconv"
)

func main() {
	x := 1
	y := 4

	dist := hammingDistance(x, y)

	fmt.Printf("The Hamming distance of %d and %d is %d in binary.\n", x, y, dist)
}

func hammingDistance(x int, y int) int {
	binX := intToBin(strconv.Itoa(x))
	binY := intToBin(strconv.Itoa(y))

	xBinX := []rune(binX)
	xBinY := []rune(binY)
	xBinX, xBinY = makeEqualLength(xBinX, xBinY)

	var dist int
	for idx, val := range xBinX {
		if val != xBinY[idx] {
			dist++
		}
	}

	return dist
}

func intToBin(d string) string {
	// Converts a decimal integer to its binary representation.

	dividend, _ := strconv.Atoi(d)
	if dividend/2 == 0 {
		remainder := dividend % 2
		return strconv.Itoa(remainder)
	}

	remainder := strconv.Itoa(dividend % 2)
	quotient := strconv.Itoa(dividend / 2)
	return intToBin(quotient) + remainder
}

func makeEqualLength(bin1, bin2 []rune) ([]rune, []rune) {
	// Makes num1 and num2 have the same length by padding on the left with zeros.

	if len(bin1) < len(bin2) {
		numZeros := len(bin2) - len(bin1)
		for i := 0; i < numZeros; i++ {
			bin1 = append([]rune{48}, bin1...)
		}
	} else if len(bin1) > len(bin2) {
		numZeros := len(bin1) - len(bin2)
		for i := 0; i < numZeros; i++ {
			bin2 = append([]rune{48}, bin2...)
		}
	}

	return bin1, bin2
}

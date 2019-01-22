package main

import (
	"fmt"
	"strings")

func main() {
	var J string
	var S string

	numJewels := numJewelsInStones(J, S)
	fmt.Printf("The total number of jewels you have is %v", numJewels)
}

func numJewelsInStones(J, S string) int {
	totalJewels := 0

	xJ := strings.Split(J, "")
	xS := strings.Split(S, "")

	for _, value := range xS {
		for _, val := range xJ {
			if value == val {
				totalJewels += 1
			}
		}
	}
	return totalJewels
}

// go through the Jewels list, J and see if any element is in the Stones list S

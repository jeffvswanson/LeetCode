package main

import "fmt"

func main() {
	xi := []int{2, 7, 11, 15}
	ans := 9
	ansIndices := twoSum(xi, ans)
	fmt.Printf("The two indices adding to %v are %v and %v", ans, ansIndices[0], ansIndices[1])
}

func twoSum(nums []int, target int) []int {
	for index, value := range nums {
		for j, val := range nums {
			if index == j {
				continue
			} else if value+val == target {
				return []int{index, j}
			}
		}
	}
	return nil
}

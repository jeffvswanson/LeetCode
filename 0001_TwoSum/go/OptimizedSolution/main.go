package main

import "fmt"

func main(){
	xi := []int{2,7,11,15}
	target := 9
	answer := twoSum(xi, target)

	fmt.Printf("The two indices which add to %v are %v", target, answer)
}

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
	var complement int

	for index, value := range nums {
		complement = target - value
		_, ok := m[complement]
		if ok {
			return []int{index, m[complement]}
		}
		m[value] = index
	}
	return nil
}
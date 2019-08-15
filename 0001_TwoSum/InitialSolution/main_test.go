package main

import (
	"testing"
)

func TestTwoSum(t *testing.T) {
	xi := []int{2, 7, 11, 15}
	target := 9
	answer := twoSum(xi, target)
	expect := []int{0, 1}

	if answer == nil {
		t.Errorf("Expected %v, got %v", expect, answer)
	} else if len(answer) != len(expect) {
		t.Errorf("Expected %v, got %v", expect, answer)
	} else {
		for i := range answer {
			if answer[i] != expect[i] {
				t.Errorf("Expect %v, got %v", expect, answer)
			}
		}
	}

}

func BenchmarkTwoSum(b *testing.B) {
	xi := []int{2, 7, 11, 15}
	target := 9
	for i := 0; i < b.N; i++ {
		twoSum(xi, target)
	}
}

package main

import "testing"

func TestIntToBin(t *testing.T) {
	// binary representation of 5
	expected := "101"
	got := intToBin("5")
	if got != expected {
		t.Errorf("Expected: %v, Got: %v\n", expected, got)
	}
}

func TestMakeEqualLength(t *testing.T) {
	// rune encoding of 5 (101) and 1 (1) in binary, respectively
	bin1 := []rune{49, 48, 49}
	bin2 := []rune{49}

	expected := [][]rune{[]rune{49, 48, 49}, []rune{48, 48, 49}}
	got1, got2 := makeEqualLength(bin1, bin2)
	got := [][]rune{got1, got2}

	for idx, val := range expected {
		for i, v := range val {
			if v != got[idx][i] {
				t.Errorf("Expected:\t%v\nGot:\t\t%v\n", val, got[idx])
			}
		}
	}
}

func TestHammingDistance(t *testing.T) {
	expected := 2
	// 4 in binary = 100, 1 = 1
	got := hammingDistance(4, 1)

	if expected != got {
		t.Errorf("Expected: %v, Got: %v\n", expected, got)
	}
}

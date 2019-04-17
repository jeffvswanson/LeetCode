package main

import "testing"

var benchmarkResult bool
var judgeCircleTestTable = []struct {
	path     string // input
	expected bool   // expected result
}{
	{"U", false},
	{"D", false},
	{"L", false},
	{"R", false},
	{"UD", true},
	{"LR", true},
}

func TestJudgeCircle(t *testing.T) {
	for _, tt := range judgeCircleTestTable {
		got := judgeCircle(tt.path)
		if got != tt.expected {
			t.Errorf("judgeCircle(%s), \tExpected: %t, got: %t", tt.path,
				tt.expected, got)
		}
	}
}

func BenchmarkJudgeCircle(b *testing.B) {
	robotPath := "UDLR"
	var atOrigin bool

	for i := 0; i < b.N; i++ {
		atOrigin = judgeCircle(robotPath)
	}
	benchmarkResult = atOrigin
}

package main

import "testing"

func TestDefangIPaddr(t *testing.T) {

	tests := map[string]struct {
		input string
		want  string
	}{
		"1-digit address":     {input: "1.1.1.1", want: "1[.]1[.]1[.]1"},
		"multi-digit address": {input: "200.100.50.0", want: "200[.]100[.]50[.]0"},
	}

	for name, tc := range tests {
		t.Run(name, func(t *testing.T) {
			got := defangIPaddr(tc.input)
			if got != tc.want {
				t.Errorf("expected: %s, got: %s", tc.want, got)
			}
		})
	}
}

func BenchmarkDefangIPaddr(b *testing.B) {
	for n := 0; n < b.N; n++ {
		defangIPaddr("200.100.50.1")
	}
}

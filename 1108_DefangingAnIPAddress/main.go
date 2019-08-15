/*Given a valid (IPV4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]"

Example 1:
	Input: address = "1.1.1.1"
	Output: "1[.]1[.]1[.]1"

Example 2:
	Input: address = "255.100.50.0"
	Output: "255[.]100[.]50[.]0"
*/
package main

import (
	"fmt"
)

func main() {

	address := "1.1.1.1"
	fmt.Println(defangIPaddr(address))
}

func defangIPaddr(address string) string {

	var d string
	for _, r := range address {
		if r != '.' {
			d += string(r)
		} else {
			d += "[.]"
		}
	}

	return d
}

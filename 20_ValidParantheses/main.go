package main

func main() {
	output := isValid()
}

func isValid(s string) bool {
 
	// byte code for open parentheses, '(', 40.
	// byte code for close parentheses, ')', 41.
	// byte code for open brace, '{', 123.
	// byte code for close brace, '}', 125.
	// byte code for open bracket, '[', 91.
	// byte code for close bracket, ']', 93.
	
	// short circuit to true if empty string
	if len(s) == 0 { return true}
	
	output := false
	openChars := make([]rune, 0)
	
	for _, character := range(s) {
	  if character == '(' || character == '[' || character == '{' {
		openChars = append(openChars, character)
	  }
	  
  
	  if character == ')' && openChars[len(openChars) - 1] == '(' {
		output = true
		openChars = openChars[:len(openChars) - 1]
	  } else if character == ']' && openChars[len(openChars) - 1] == '[' {
		output = true
		openChars = openChars[:len(openChars) - 1]
	  } else if character == '}' && openChars[len(openChars) - 1] == '{' {
		output = true
		openChars = openChars[:len(openChars) - 1]
	  } else { output = false }
	}
	return output
  }
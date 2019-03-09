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
	
	openChars := make([]rune, 0)
	closeChars := make([]rune, 0)
	
	for _, character := range(s) {
	  if character == '(' || character == '[' || character == '{' {
		openChars = append(openChars, character)
	  } else if character == ')' || character == ']' || character == '}' {
		closeChars = append(closeChars, character)
	  }
	  
	  // Short circuit the tests below if there are not elements in the slice
	  if len(openChars) == 0 {continue}
	  
	  if character == ')' && openChars[len(openChars) - 1] == '(' {
		openChars, closeChars = removeElement(openChars, closeChars)
	  } else if character == ']' && openChars[len(openChars) - 1] == '[' {
		openChars, closeChars = removeElement(openChars, closeChars)
	  } else if character == '}' && openChars[len(openChars) - 1] == '{' {
		openChars, closeChars = removeElement(openChars, closeChars)
	  }
	}
	
	if len(openChars) == 0 && len(closeChars) == 0 {return true}
  
	return false
  }
  
  func removeElement(openStack, closeStack []rune) ([]rune, []rune) {
	openStack = openStack[:len(openStack) - 1]
	closeStack = closeStack[:len(closeStack) - 1]
	return openStack, closeStack
  }
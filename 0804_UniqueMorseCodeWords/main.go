package main
/*
From https://leetcode.com/problems/unique-morse-code-words/, 
accessed 12 March 2019

International Morse Code defines a standard encoding where each letter is 
mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps 
to "-...", "c" maps to "-.-.", and so on.

Now, given a list of words, each word can be written as a concatenation of the 
Morse code of each letter. For example, "cba" can be written as "-.-..--...", 
(which is the concatenation "-.-." + "-..." + ".-"). We'll call such a 
concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
*/

import ("fmt")

func main() {
	words := []string {"gin", "zen", "gig", "msg"}

	uniqueWords := uniqueMorseRepresentations(words)

	fmt.Printf("The number of unique words is %d", uniqueWords)
}

func uniqueMorseRepresentations(words []string) int {
	alphabetToMorseMap := make(map[rune]string)
	morseWordMap := make(map[string]string)

	var uniqueWords int

	morseLetters := []string {
	  ".-","-...","-.-.","-..",".","..-.","--.","....","..",
	  ".---","-.-",".-..","--","-.","---",".--.","--.-",
	  ".-.","...","-","..-","...-",".--","-..-","-.--","--..",
	}
	alphabet := []rune {
		'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
		'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
		'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
	}

	for idx, letter := range(alphabet) {
		alphabetToMorseMap[letter] = morseLetters[idx]
	}

	for _, word := range(words) {
		var morseLetter string
		var morseWord string
		
		for _, letter := range(word) {
			morseLetter = alphabetToMorseMap[letter]
			fmt.Printf("The morse letter representation of %c is %s\n", letter, morseLetter)
			morseWord = morseWord + morseLetter
		}
		fmt.Printf("The morse representation of %s is %s\n\n", word, morseWord)
		morseWordMap[morseWord] = word
	}

	uniqueWords = len(morseWordMap)

	return uniqueWords
}
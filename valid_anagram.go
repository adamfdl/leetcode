package main

func isAnagram(s string, t string) bool {

	if len(s) != len(t) {
		return false
	}

	charactersInS := make(map[rune]int)
	for _, char := range s {
		charactersInS[char]++
	}

	charactersInT := make(map[rune]int)
	for _, char := range t {
		charactersInT[char]++
	}

	for char, _ := range charactersInS {
		// Checks if the characters in S donest exist in T
		_, ok := charactersInT[char]
		if !ok {
			return false
		}

		// Compare the frequency
		if charactersInS[char] != charactersInT[char] {
			return false
		}
	}

	return true
}

// Time complexity O(n)
// Space complexity of O(1)
// TODO: Can try to do array of alphabet so you can achieve
// TODO: Clarify regarding the inputs!

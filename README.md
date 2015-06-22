# py-dela
Python DELA Dictionary Library

This python library handles DELA dictionaries used by Unitex such as [THESE](http://www-igm.univ-mlv.fr/~unitex/index.php?page=7).

# Example
	if __name__ == '__main__':
		lexicon = Lexicon("/home/ulysses/Applications/Unitex3.1beta/Portuguese (Brazil)/Dela/")
		print(lexicon.get_lemmas(sys.argv[1]))

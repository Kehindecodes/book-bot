from stats import count_words,count_char_occurence, sorted_occurence
import sys


def main ():
   if len(sys.argv) > 1:
      words = get_book_text(sys.argv[1])
      length = count_words(words)
      char_occurence = count_char_occurence(words)
      sorted = sorted_occurence(char_occurence)
      print (f"""

               ============ BOOKBOT ============
               Analyzing book found at books/frankenstein.txt...
               ----------- Word Count ----------
               Found {length} total words
               --------- Character Count -------
               {sorted}
               ============= END ===============
            """)
   else:
      print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)

def get_book_text (file_path) :
   with open(file_path) as f :
     return f.read()

main()
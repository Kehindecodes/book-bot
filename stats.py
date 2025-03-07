def count_words(words):
  return len(words.split())


def count_char_occurence(text):
  occurences = {}
  lower_case_text = text.lower()
  for char in lower_case_text :
    if char.isalpha() :
      if char in occurences:
          occurences[char] += 1
      else:
          occurences[char] = 1
    else:
      continue

  return occurences

def sorted_occurence(occurences):
 return {key.strip('"').strip("'"): value for key, value in occurences.items()}





def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letter(text):
  text_lower = text.lower()
  text_list = []
  for i in range (0, len(text)):
    text_list.append(text_lower[i])
  count_letter = {}
  for letter in text_list:
    if letter in count_letter:
      count_letter[letter] += 1
    else:
      count_letter[letter] = 1
  return count_letter

def get_final_result(dict):
  dict2 = []
  for item in dict:
    dict2.append({"name": item, "num": dict[item]})

  def sort_on(item):
    return item["num"]

  dict2.sort(reverse=True, key=sort_on)
  
  return dict2


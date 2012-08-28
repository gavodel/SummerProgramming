f = open('C:\Users\Gavin\Documents\GitHub\SummerProgramming\\words.txt',
	'r')

# line = "this is a line"
# count_line(line) -> char_count, word_count
# -> 11 4
total_char_count = 0
total_word_count = 0
	
def count_line(line):
	words = line.split(" ")
	number_of_words=len(words)
	number_of_chars=0 
	for word in words:
		number_of_chars += len(word)
	return number_of_words, number_of_chars

	
y = f.readlines()

for i in range(0,len(y)):	
	temp_words, temp_chars = count_line(y[i])
	total_word_count += temp_words
	total_char_count += temp_chars
average = total_char_count / float(total_word_count) 
print "average is %d"%average
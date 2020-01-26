# inspired by https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/

text_p1 = ('the weather is lovely today', 'sunny')
text_p2 = ('the weather is sunny and the skies are clear', 'sunny')
text_p3 = ('the sun is out and it is hot', 'sunny')

text_n1 = ('it is raining today', 'not_sunny')
text_n2 = ('the weather is cold', 'not_sunny')
text_n3 = ('it is snowing and the rain is falling', 'not_sunny')

def print_frequencies(pwords, nwords):
	for k, v in pwords.items():
		print('{} : {}'.format(k, v))

	for k, v in nwords.items():
		print('{} : {}'.format(k, v))

def calculate_unique_words(training_set):
	concatenated_text = ''
	len_cnt = 0
	for text in training_set:
		sentence = text[0]
		concatenated_text += sentence + ' '  

	# [:-1] is to remove trailing space
	unique_word_count = len(set(concatenated_text.split(' ')[:-1]))
	print('added {} unique words to count'.format(unique_word_count))
	#print(set(concatenated_text.split(' ')[:-1]))

	return unique_word_count

def initialize_categories(training_set):
	pwords = dict()
	nwords = dict()

	# initialize frequencies
	for text in training_set:
		words = text[0].split(' ')
		category = text[1]
		
		for word in words:
			# format of tuple is (word count in category, frequency)
			if category == 'sunny':
				pwords[word] = (0, 0.0)
			elif category == 'not_sunny':
				nwords[word] = (0, 0.0)
			else:
				print('invalid category: {}'.format(category))
				exit(-1)

	# fill in word counts
	for text in training_set:
		words = text[0].split(' ')
		category = text[1]

		for word in words:
			if category == 'sunny':
				count = pwords[word][0]
				pwords[word] = (count + 1, 0.0)
			elif category == 'not_sunny':
				count = nwords[word][0]
				nwords[word] = (count + 1, 0.0)

	return pwords, nwords

def generate_frequencies(training_set):
	print('generating frequencies..')
	pwords, nwords = initialize_categories(training_set)
	pword_count = len(pwords)
	nword_count = len(nwords)
	unique_word_count = calculate_unique_words(training_set)


	for text in training_set:
		words = text[0].split(' ')
		category = text[1]

		# feature tuple is (word count, frequency)
		for word in words:
			if category == 'sunny':
				pwords[word] = (pwords[word][0], pwords[word][1] + 1 / (pwords[word][1] + pword_count))
			elif category == 'not_sunny':
				nwords[word] = (nwords[word][0], nwords[word][1] + 1 / (nwords[word][1] + nword_count))

	return pwords, nwords

def assemble_probability(input_text, frequencies):
	score = 0.0

	# calculate score for input text
	for word in input_text.split(' '):
		if word in frequencies:
			score += frequencies[word][1]

	return score
	
tset = list()
tset.append(text_p1)
tset.append(text_p2)
tset.append(text_p3)
tset.append(text_n1)
tset.append(text_n2)
tset.append(text_n3)
pwords, nwords = generate_frequencies(tset)
#print_frequencies(pwords, nwords)
score_p = assemble_probability('it is raining today', pwords)
score_n = assemble_probability('it is raining today', nwords)

print('score positive: {}, score negative: {}'.format(score_p, score_n))

if score_p > score_n:
	print('it is sunny')
else:
	print('it is not sunny')
# inspired by https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/

text_p1 = ('the weather is lovely today', 'sunny')
text_p2 = ('the weather is sunny and the skies are clear', 'sunny')
text_p3 = ('the sun is out and it is hot', 'sunny')

text_n1 = ('it is raining today', 'cold')
text_n2 = ('the weather is cold', 'cold')
text_n3 = ('it is snowing and the rain is falling', 'cold')

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

def generate_frequencies(training_set):
    print('generating frequencies..')
    
    unique_word_count = calculate_unique_words(training_set)
    pwords = dict()
    nwords = dict()

    for text in training_set:
    	word_category = text[1]

    	# calculate frequencies in category 1 and category 2 (in this case sunny, cold)
    	if word_category == 'sunny':
	        for word in text[0].split(' '):
	            if word not in pwords:
	                # first time word is seen - calculate frequency
	                pwords[word] = (word, 1 / unique_word_count)
	            else:
	                # create new tuple and add new word frequency to word existing frequency
	                pwords[word] = (pwords[word][0], pwords[word][1] + (pwords[word][1] / unique_word_count))
    	elif word_category == 'cold':
	        for word in text[0].split(' '):
	            if word not in nwords:
	                # first time word is seen - calculate frequency
	                nwords[word] = (word, 1 / unique_word_count)
	            else:
	                # create new tuple and add new word frequency to word existing frequency
	                nwords[word] = (nwords[word][0], nwords[word][1] + (nwords[word][1] / unique_word_count))
    	else:
	    	print('unknown category {}'.format(word_category))
	    	return (None, None)
    
tset = list()
tset.append(text_p1)
tset.append(text_p2)
tset.append(text_p3)
tset.append(text_n1)
tset.append(text_n2)
tset.append(text_n3)
generate_frequencies(tset)

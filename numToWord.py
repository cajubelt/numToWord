ones = ["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def hundredsToWord(number):
	assert number < 1000 #only deal with three-digit numbers
	output = ""
	if number > 99: #deal with hundreds place
		hundreds_place = number / 100
		output = ones[hundreds_place] + " hundred"

	remainder = number % 100 #deal with tens place
	ones_place = remainder % 10
	tens_place = remainder / 10
	if 10 < remainder and remainder < 20: #deal with teens special case
		output += " " + teens[ones_place]
	else: #deal with non-teens tens and ones places
		if tens_place != 0:
			output += " " + tens[tens_place]
		if ones_place != 0:
			output += " " + ones[ones_place]

	return output


thousands = ["", " thousand ", " million ", " billion ", " trillion ", " quadrillion "]

def numToWordRecursive(number,commas):
	output = ""
	if number > 0:
		output = numToWordRecursive(number / 1000, commas+1) + hundredsToWord(number % 1000)  + thousands[commas]
	return output

def numToWord(number):
	output = numToWordRecursive(number,0)
	while output[-1] == " ":
		output = output[:-1]
	while output[0] == " ":
		output = output[1:]
	output += "!"
	return output


print numToWord(1051546)
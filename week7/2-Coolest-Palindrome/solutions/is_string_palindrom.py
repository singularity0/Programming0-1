def is_string_palindrom(string):
	new_string = ''
	marks = [',', '.', '?', '!', ' ']

	for c in string:
		if c not in marks:
			new_string += c

	new_string = new_string.lower()

	for i in range(0, len(new_string)//2):
		if new_string[i] == new_string[len(new_string)-1-i]:
			continue
		else:
			return False
	return True
print(is_string_palindrom("A Toyota!"))
print(is_string_palindrom("bozaa"))
print(is_string_palindrom(" kapak! "))
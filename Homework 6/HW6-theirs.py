from elementsfixed import elements, Radio_Active

# Problem 3 isn't really possible or useful because dictionaries are orderless in Python.
# This ends up being horrendously complex for no real value
# Could totally do it in PHP though ;D

# Problem 4
Radio_Active_by_Alpha = sorted(Radio_Active)

# Problem 5
# Has a rather obnoxious oversight: Most of the elements in the 'radioactive' list aren't
# actually in the elements dictionary! I've made a demo-only import called elementsfixed
# This is because the elements dictionary only goes to atomic number 81.
charges = {}
for element in Radio_Active:
	charges[element] = elements[element]['charge']
print charges

# Problem 6
stable = []
for element in elements:
	if element not in Radio_Active:
		stable.append(element)
print stable

# Problem 7
# Same issue: Most of the radioactive elements aren't actually in this elements dictionary
# I've used elementsfixed to test this answer.
radioactive_metals = []
for element in Radio_Active:
	if elements[element]['type'] == 'metal':
		radioactive_metals.append(element)
print radioactive_metals
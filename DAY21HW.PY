freq_dict = {"bananas": 6, "apple": 9, "mango": 7}

element = "mango"

if element in freq_dict:
    print(f"{element} occurs {freq_dict[element]} times")
else:
    print(f"{element} not found")

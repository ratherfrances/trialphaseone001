


c = "6011000000000000"

#slices 
visa_slice = c[0:1:1] #"4"
amex_slice = c[0:2:1]
mastercard_slice = c[0:2:1]
discover_slice = c[0:4:1]
#lists
amex_list = ["34","37"]
mastercard_list = ["51", "52", "53", "54", "55"]

if visa_slice == "4" and len(c) == 16:
	card_type = "Visa"
elif amex_slice in amex_list and len(c) == 15: 
	card_type = "AMEX"
elif mastercard_slice in mastercard_list and len(c) == 16: 
	card_type = "Mastercard"
elif discover_slice == "6011" and len(c) == 16: 
	card_type = "Discover"
else: 
	card_type = "Invalid"
print(card_type)
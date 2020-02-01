# This is the program for CRC receiving side. 

# Defining the XOR operation for mod2 division
def xor(a, b): 
 
	result = [] 

	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 

	return ''.join(result) 

# Modulus 2 division

def mod2div(divident, divisor): 

	pick = len(divisor) 
	tmp = divident[0 : pick] 
	while pick < len(divident): 

		if tmp[0] == '1': 
			tmp = xor(divisor, tmp) + divident[pick] 

		else:  
			tmp = xor('0'*pick, tmp) + divident[pick] 

		# increment pick to move further 
		pick += 1

	# For the last n bits, we have to carry it out 
	# normally as increased value of pick will cause 
	# Index Out of Bounds. 
	if tmp[0] == '1': 
		tmp = xor(divisor, tmp) 
	else: 
		tmp = xor('0'*pick, tmp) 

	checkword = tmp 
	return checkword 

# Function used at the receiver side to decode 
# data received by sender 
def decodeData(data, key): 

	l_key = len(key) 

	# Appends n-1 zeroes at end of data 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 

	return remainder 


def BinaryToDecimal(binary):  
	string = int(binary, 2) 
	return string 


# entering the key 
# Key should be same ono both transmission side and receiver side.
key = "1001"
data = "111011011000011110100111001111000011110110100"
ans = decodeData(data, key) 
print("Remainder after decoding is->"+ans) 

tmp = "0" * (len(key) - 1) 
if ans == tmp: 
    print("Data is ->"+data + " \nReceived No error FOUND")
    received_data = data[ 0 : len(data) - len(ans)]
    print("Decoded data is -> " + received_data) 
else: 
    print("Error in data")
    
str_data =' '
for i in range(0, len(data), 7): 
	temp_data = data[i:i + 7] 
	decimal_data = BinaryToDecimal(temp_data) 
	str_data = str_data + chr(decimal_data) 
	
# printing the result 
print("The Binary value after string conversion is:", 
	str_data)
print(len(str_data))

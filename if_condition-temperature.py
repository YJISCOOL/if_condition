temp_unit = input("what is the unit(\'C/\'F): ")
temp = int(input("what is the temperature now? "))

if temp_unit == "\'C":
	temp_F = str(temp * 1.8 + 32)
	print (temp, temp_unit + ' is equal to ' + temp_F + '\'F')

else:
	temp_C = str((temp - 32) * (5/9))
	print (temp, temp_unit + ' is equal to ' + temp_C + '\'C')
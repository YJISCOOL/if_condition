height = float(input('身高： '))
weight = float(input('體重： '))
BMI = (weight/ height**2)

if BMI < 18.5:
	print ('體重過輕')
elif 18.5 <= BMI < 24:
	print ('正常範圍')
elif 24<= BMI < 27:
	print ('過重')
elif 27<= BMI < 30:
	print ('輕度肥胖')
elif 30<= BMI < 35:
	print ('中度肥胖')
else:
	print ('重度肥胖')
	
	
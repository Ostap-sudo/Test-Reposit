h = float(input("Print your height (in meters): "))
w = int(input("Print your weight in kg: "))
IMT = w/(h*h)
print(round(IMT,2))
if IMT < 18.5:
	print ("Underweight")
if IMT >= 18.5 and IMT <24.9:
	print ("Healthy Weight")
if IMT > 24.9 and IMT <=29.9:
	print("Overweight")
if IMT > 30.0:
	print("Obesity")
else:
	print("Try again")
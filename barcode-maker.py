import barcode
from barcode.writer import ImageWriter
val = ''
validVal = False
length = 0

while validVal == False:
	validVal = True
	val = input("Enter Barcode Value excluding the check digit: ")
	length = len(val)
	standard = 'ean13'
	if length == 11: 
		standard = 'upca'
		checkSum = barcode.upc.UniversalProductCodeA(val).calculate_checksum()

	elif length == 12: 
		standard = 'ean13'
		checkSum = barcode.ean.EuropeanArticleNumber13(val).calculate_checksum()
		
	else: 
		validVal = False
		print("Please enter a value with either 7, 11, or 12 digits excluding the check digit")

fullVal = val + str(checkSum)

ean = barcode.get(standard, val, writer=ImageWriter())
filename = ean.save('{}-({})-barcode'.format(standard, fullVal))

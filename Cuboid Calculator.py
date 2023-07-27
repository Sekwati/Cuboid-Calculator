import math

print("Cuboid Calculator")
#Input data
width  = float(input("\nEnter the width (cm): "))
length = float(input("Enter the length(cm): "))
height = float(input("Enter the height(cm): "))

#Calculations
area = 2 * (length * width+ length * height + width * height)
volume = length * width * height
Space_Diagonal = math.sqrt(math.pow(length,2) + math.pow(width,2) + math.pow(height,2))

#Printing Output
print("\nArea of the cuboid is ", round(area, 4) , " square cm")
print("Space diagonal of the cuboid ", round(Space_Diagonal, 3) , " cm")
print("Volume of the cuboid is ", round(volume, 2) , "cubic cm")

print("\n**Cuboid dimensions:**")
print(f"width = ", width, "cm", " \t length = ", length, "cm" "\t height = ", height, "cm" )
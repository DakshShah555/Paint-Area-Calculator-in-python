# 1 can = 5 sq meters

'''def no_cans(height,width):
    cans=(height*width)/5
    return cans

height=float(input("Enter the height of the wall in (meters):"))
width=float(input("Enter the width of the wall in (meters):"))

print(f"Total number of cans required {no_cans(height,width)}")'''

def paint_calc(height, width, cover):
    cans = (height * width) / cover
    cans = round(cans)
    return cans

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print(paint_calc(test_h, test_w, coverage))

def calc_area(radius):
    area=3.14*radius*radius
    print("Area of circle is:"+ str(area))
    radius*=2
    return
r=float(input("Enter radius:"))
print("Radius before calling function:",r)
calc_area(r)
print("Radius after calling function:",r)
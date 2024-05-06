def calc_volume(*args):
    vol=3.142*args[0]*args[0]*args[1]
    print("volume of the cylinder is:"+str(vol))
    args*=2
    return
dimensions=[2,3]
print(dimensions)
calc_volume(dimensions[0],dimensions[1])
print(dimensions)
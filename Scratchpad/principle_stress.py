import math

 

sigma_x = input("Enter sigma_x: ")
sigma_y = input("Enter sigma_y: ")
shear_xy = input("Enter shear_xy: ")
sigma_max = (sigma_x + sigma_y)/2 + math.sqrt(((sigma_x - sigma_y)/2)^2 + shear_xy^2)
sigma_min = (sigma_x + sigma_y)/2 - math.sqrt(((sigma_x - sigma_y)/2)^2 + shear_xy^2)
print("sigma_max: " + sigma_max + "\nsigma_min: " + sigma_min);
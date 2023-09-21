#userinput
wavelength = round(float(input("Enter the wavelength: ")), 1)

#function
if wavelength < 380:  
    print("Outside the visible range.")
elif 380 <= wavelength < 450:
    print(f"{wavelength} nm is Violet.")
elif 450 <= wavelength < 495:
    print(f"{wavelength} nm is Blue.")
elif 495 <= wavelength < 570:
    print(f"{wavelength} nm is Green.")
elif 570 <= wavelength < 590:
    print(f"{wavelength} nm is Yellow.")
elif 590 <= wavelength < 620:
    print(f"{wavelength} nm is Orange.")
elif 620 <= wavelength <= 620:
    print(f"{wavelength} nm is Red.")
elif 620 < wavelength:
    print("Outside the visible range.")

import ctypes
import time,os
#Do not forget to give the same format of pictures to program and before starting rename all photos to numbers like  1.jpg :)
#----------------------------------------------------------------------------------------------

direct=input("enter wallpapers file(example: C:/Users/admin/Desktop/wallpapers/): ")
pas="."+input("enter pictures format(example: png): ")
times=int(input("enter times you want to repeat(example: 10)(type 0 for endless loop): "))
delay,i=int(input("enter delay time(example: 5): ")),1
#----------------------------------------------------------------------------------------------

print("starting...")        #start process

if times==0:
    print("press Ctrl+c to stop :)")
    while True:
        fdir=direct+f"{i}"+pas      #finall path
        if os.path.exists(fdir):    #Check if photo exist or not
            ctypes.windll.user32.SystemParametersInfoW(20,0,fdir,0)         #change wallpaper
            time.sleep(delay)       #set a delay between changing wallpaper
        else:   #reset photos number and start from the first picture
            i=1
            fdir=direct+f"{i}"+pas
            ctypes.windll.user32.SystemParametersInfoW(20,0,fdir,0)
            time.sleep(delay)
        i+=1   
else:    
    for j in range(1,times):
        fdir=direct+f"{i}"+pas
        if os.path.exists(fdir):
            ctypes.windll.user32.SystemParametersInfoW(20,0,fdir,0)
            time.sleep(delay)
        else:
            i=1
            fdir=direct+f"{i}"+pas
            ctypes.windll.user32.SystemParametersInfoW(20,0,fdir,0)
            time.sleep(delay)
        i+=1

print("Done!")  #finish process
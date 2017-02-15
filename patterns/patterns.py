from microbit import *
    
Square = Image("99999:90009:90009:90009:99999")      

SquaredDiag = Image("99999:99099:90909:99099:99999")      

Diag = Image("90009:09090:00900:09090:90009")      

CrossedDiag = Image("90909:0999:99999:09990:90909")      

Cross = Image("00900:00900:99999:00900:009")      

SquaredCross = Image("99999:90909:99999:90909:99999")      

allImages = [Square,SquaredDiag,Diag,CrossedDiag,Cross,SquaredCross]
display.show(allImages, delay=1000, loop=True)

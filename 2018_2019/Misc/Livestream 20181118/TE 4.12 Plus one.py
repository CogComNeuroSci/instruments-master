#Een priemgetal is een natuurlijk getal groter dan 1 dat slechts twee natuurlijke getallen als deler heeft, namelijk 1 en zichzelf

getal = -10 #getal ingeven die je wilt testen

if getal < 2:
    print("Dit kan niet, je moet een getal groter dan 1 ingeven")

priemgetal = True

## Esther: by looping over all the numbers in range(), you are also using 0 which can't be used as the denominator in a division
for i in range(getal):
    ## Esther: I see you avoid the division by 0 by adding 1
    ## Esther: this is a creative solution, but maybe a bit less clean that skipping 0 in the first place
    if getal%(i+1) == 0:
        ## Esther: are you trying to avoid the number 1 and the number itself, which is a good intention
        ## Esther: however, the number 1 can be avoided from the start (along with a bunch of other numbers)
        ## Esther: you actually don't need to verify the number itself, you even don't need to verify any number larger than the largest integer smaller than the square root of the number
        ## Esther: try to apply this idea to the number 36 (with divisors 1,2,3,4,6,9,12,18,36)
        if (i+1) != 1 and (i+1) != getal:
            priemgetal = False

if priemgetal == True:
    print("{0} is een priemgetal".format(getal))
else:
    print("{0} is geen priemgetal".format(getal))
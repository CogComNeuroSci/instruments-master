#voor de reactietijden te meten zou ik opteren voor de core.MonotonicClock functie
### Esther: deze klok kan je niet herzetten wanneer je wil, dus alles hangt af van de rest van je code
trial_timer = core.MonotonicClock()

##dit zou ik gebruiken voor de verticale gabor stimulus een seconde lang te tonen.
timer = core.CountdownTimer(1)
### Esther: niet fout, maar time.sleep(1) volstaat ook

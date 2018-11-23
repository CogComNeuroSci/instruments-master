from psychopy import visual
import time, numpy

#zonnenstelsel
win = visual.Window(size = (600,600), color = "black", units = 'norm')

zon = visual.Circle(win, radius = 0.15, fillColor = "yellow", lineColor ="yellow", pos =(0,0))
planeet = visual.Circle(win, radius = 0.07, fillColor = "blue", lineColor = "blue",pos = (0.705, 0.236))
maan = visual.Circle(win, radius = 0.02, fillColor = "white", lineColor = "white", pos = (0.707, 0.356))
zon.draw()
planeet.draw()
maan.draw()
win.flip()
time.sleep(1)

#van gele zon tot rode reus
sizes = [0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.30, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7,0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84,0.85, 0.86, 0.87, 0.88, 0.89,0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0, 1.01, 1.02,1.03]

for i in sizes:
    reus = visual.Circle( win, radius = i, pos = (0,0), lineColor = "yellow", fillColor = "yellow")
    reus.draw()
    planeet.draw()
    maan.draw() 
    win.flip()
    time.sleep(0.05)

#feedback botsing
pos_planeet = (0.705, 0.236)
pos_maan = (0.707, 0.356)
pos_reus = (1.03, 1.03)

if pos_reus > pos_planeet and pos_reus > pos_maan:
    info = "De planeet en de maan hebben tegelijk de rode reus geraakt."
elif pos_reus < pos_planeet and pos_reus > pos_maan:
    info = "De maan heeft de rode reus geraakt."
else: 
    info = "Geen enkele van de hemellichamen heeft de rode reus geraakt."

info_text = visual.TextStim(win, text = info)
info_text.draw()
win.flip()
time.sleep(1)

#rotaties 
positie_planeetX = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
positie_planeetY =[    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
positie_maanX = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
positie_maanY = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

positie_planeet = numpy.array(["positie_planeetX", "positie_planeetY"])
positie_maan = numpy.array(["positie_maanX", "positie_maanY"])

for e in positie_planeet:
    planeet_2 = visual.Circle(win, radius = 0.07, fillColor = "blue", lineColor = "blue",pos = e)
for f in positie_maan:
    maan_2 = visual.Circle(win, radius = 0.02, fillColor = "white", lineColor = "white", pos = f)

reus.draw()
planeet_2.draw()
maan_2.draw()
win.flip()
time.sleep(0.05)


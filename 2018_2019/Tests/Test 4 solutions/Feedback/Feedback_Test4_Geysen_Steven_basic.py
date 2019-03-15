# Project:		Test 4
# Date:			06/03/2019
# Author(s):	Geysen Steven (01611639)
# Notes:		.csv bijzetten op einde



# Basics

from psychopy import core, event, gui, monitors, visual
import numpy as np
import os

## Text with infinite wait.Keys
def text_IWKeys(win, text, key_list):
	'''display text, key to continue.
	waits forever'''
	text.draw()
	win.flip()
	event.waitKeys(keyList = key_list)

## Text without space (core.wait())
def text_core(win, text, duration):
	'''Display text, wait duration to continue.
	uses core.wait'''
	text.draw()
	win.flip()
	core.wait(duration)

## Window
mon = monitors.Monitor('my laptop screen')
mon.setDistance(40)					## How far is pp from screen (cm)
mon.setWidth(38)					## How wide is screen (cm)
mon.setSizePix((1536,864))			## Size in pixels

win = visual.Window(size = (1000,700), units = 'norm', monitor = mon)

## Clock for RT
my_clock = core.Clock()


# Data file

## GUI
info_details = {'Participant nummer':0, 'Naam participant':'Voornaam', 'Geslacht':['Man', 'Vrouw', 'Andere'], 'Leeftijd':0, 'Handvoorkeur':['Links', 'Rechts', 'Ambidexter']}

## Working directory
my_directory = os.getcwd()

## New file for every new participant and session
already_exists = True
while already_exists:

	## Dialog box 
	infoDlg = gui.DlgFromDict(dictionary = info_details, title = 'Test 4')
	Subject = str(info_details['Participant nummer'])

	## Folder
	directory_to_write_to = my_directory + '/data'
	if not os.path.isdir(directory_to_write_to):
		os.mkdir(directory_to_write_to)

    ## Esther: pas op, gezien je niet met een ExperimentHandler werkt maar gewoon zelf je file op het einde van het script wegschrijft
    ## Esther: moet je hier wel je extensie toevoegen, anders zal het script nooit doorhebben dat de file al in gebruik is.

	## File name
	file_name = directory_to_write_to + '/Test4_subject_' + Subject
	if not os.path.isfile(file_name):
		already_exists = False
	else:
		myDlg2 = gui.Dlg(title = 'Error')
		myDlg2.addText('Probeer een andere participant nummer')
		myDlg2.show()

## Verwijder naar voor anonimiteit maar houden voor begroeting
pp_name = info_details['Naam participant']
info_details.pop('Naam participant')


# Constants

NBLOCK = 12
NTRIALS = 60
DURATION = 2


# Text

Welcome = visual.TextStim(win, text = 'Welkom {}.\n\nDruk spatie om verder te gaan.'.format(pp_name))

Instructions = visual.TextStim (win, text = 'Druk')

BreakText = visual.TextStim(win, text = 'Pauze\n\n'
										+ 'Druk spatie om verder te gaan.')

TheEnd = visual.TextStim(win, text = 'Bedankt voor je deelname!')

FeedbackText = visual.TextStim(win, text = 'OK')

TestText = visual.TextStim(win, text = 'Hoera')

PresPijltje = visual.TextStim(win, text = 'pijltje')


# Possible responses

ConBut = ['space', 'escape']	## continue button
RespBut = ['right', 'left', 'down', 'escape']	## Response and escape buttons


# Trial matrix

## Stimuli
Stimulus = np.array(['>', '<'])
StimLoc = np.array([-0.5, 0, 0.5])

## Determine the number of levels for the factor
Nopties = len(Stimulus)
NposOpties = len(StimLoc)
Nunique = Nopties * NposOpties

Nreps = int(NTRIALS/Nunique)

## Determine the number of unique trials
UniqueTrials = np.array(range(Nunique))

## Factorial design
StimOptie = np.floor(UniqueTrials / NposOpties)
StimPos = np.floor(UniqueTrials / 1) %  NposOpties

## Congruence
Congruence = np.repeat(-1, len(UniqueTrials))

## Correct response
CorResp = np.repeat(-1, len(UniqueTrials))

## Accuracy
Accuracy = np.repeat(-1, len(Congruence))

## Response
Resp = np.repeat(0, len(Congruence))

## Reaction time
RT = np.repeat(-1, len(Congruence))

## Add participant info
Subject = np.repeat(info_details['Participant nummer'], len(Congruence))
Gender = np.repeat(''.join(info_details['Geslacht']), len(Congruence))
Age = np.repeat(info_details['Leeftijd'], len(Congruence))
Hand = np.repeat(''.join(info_details['Handvoorkeur']), len(Congruence))

## Combine arrays in trial matrix
trials = np.column_stack([StimOptie, StimPos, Congruence, CorResp, Resp, Accuracy, RT, Subject, Gender, Age, Hand])
trials = np.tile(trials, (Nreps,1))

## Esther: ziet er goed uit tot hier, maar je moest natuurlijk nog een manier vinden om de blokken samen te voegen

Alles = np.zeros((NTRIALS,3))*np.nan



########################
######### Core #########
########################



if infoDlg.OK:

# Greeting

	text_IWKeys(win, Welcome, ConBut)

	for block in range(NBLOCK):

	# randomiseren per block
		np.random.shuffle(trials)
	# Instructies (1/3 voor plaats, 2/3 voor richting)
		if block % 3 == 0:
			Instructions.text = ('Je moet met de pijltjes op het toetsenbord\n'
								+ 'de plaats van de pijltjes op het scherm aanduiden.\n'
								+ 'Druk <- voor links, -> voor rechts, en ^ voor in het midden.\n'
								+ 'Druk spatie om te beginnen')
		else:
			Instructions.text = ('Je moet met de pijltjes op het toetsenbord\n'
								+ 'de richting van de pijltjes op het scherm aanduiden.\n'
								+ 'Druk <- voor links en -> voor rechts.\n'
								+ 'Druk spatie om te beginnen')
		text_IWKeys(win, Instructions, ConBut)

        # Esther: als ik me niet vergis zal deze manier van indexing wel werken voor het eerste blok, maar niet voor de volgende blokken

		for trial in range(block*NTRIALS,(block+1)*NTRIALS):
			print(StimOptie)
			print(StimPos)

            ## Esther: gezien je door het toevoegen van de participanteninfo strings in je array hebt gestoken,
            ## Esther: is alles nu omgevorm naar strings waardoor je hier alles moet zitten omvormen naar floats en integers
            ## Esther: eenvoudiger is het om de proefpersooninfo pas op het einde van het script toe te voegen of
            ## Esther: een numerische code in te voeren voor de verschillende eigenschappen (0 voor rechtshandig, 1 voor linkshandig, 2 voor ambidexter)

			PresPijltje.text = Stimulus[int(float(trials[trial, 0]))]
			PresPijltje.pos = (StimLoc[int(float(trials[trial, 1]))], 0)

			PresPijltje.draw()

			event.clearEvents(eventType = 'keyboard')
			win.flip()
			my_clock.reset()
			Resp = event.waitKeys(keyList = RespBut)
			RT = my_clock.getTime()

			if Resp[0] == 'escape':
				break
		# Store the response information
			trials[trial,4] = Resp[0]
		# Determine CorResp
			
		# determine accuracy
			#trials[trial,5] = int(trials[trial,3] == trials[trial,4])
		# Store the RT
			trials[trial,5] = RT
				
# End

	text_IWKeys(win, TheEnd, ConBut)

	win.close()

else:
	print('User cancelled')



# Add trial en block number
trials=np.column_stack([trials, range(NTRIALS*NBLOCK)])
blocknr = np.repeat(range(NBLOCK),NTRIALS)
trials= np.column_stack([trials, blocknr])


# Export

np.savetxt(file_name, trials, delimiter = ',', fmt = '%.d')

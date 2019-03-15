from psychopy import visual, event, core, gui, data
import numpy, pandas,os

clock = core.Clock()
nBlocks=12
nTrials=60
win= visual.Window([1000,700])
Instructions= visual.TextStim(win,"text")
Stimulus=visual.TextStim(win,"text")


#create arrays with meaningful data
ArrowOptions=       numpy.array(['<', '>'])
PositionOptions=    numpy.array([-0.5,0,0.5])
InstructionOptions= numpy.array(["In dit blok moet je op de positie van het pijltje reageren. \nStaat het pijltje links op het scherm dan druk je op het linkerpijltje op het toetsenbord, staat het in het midden duw je op het pijltje naar beneden en als het rechts staat duw je op het pijltje naar rechts \nDruk op spatie om te beginnen","In dit blok moet je op de richting van het pijltje reageren. \nWijst het naar links duw je op het linkerpijltje op het toestenbord en als het naar rechts wijst duw je op het rechterpijltje \nDruk op spatie om te beginnen"])

# Esther: misschien wel handig om de tekst op te splitsen over verschillende lijnen, dat maakt het script beter leesbaar

#generate block and trial numbers
TrialNumber=    numpy.array(range(1,nBlocks*nTrials+1))
BlockNumber=    numpy.repeat([range(1,nBlocks+1)],nTrials)
TrialinBlock=   numpy.tile(range(1,nTrials+1),nBlocks)

#create arrays to store data
ParticipantInfo=    numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)
TrialArrow=         numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)
TrialPosition=      numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)
Congruency=         numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)
CorrectResp=        numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)
ResponseMapping=    numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)
RT=                 numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)
ActualResp=         numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)
Accuracy=           numpy.repeat(["XXXXXXXXXXXXXXX"], nBlocks*nTrials)

#generate factorial design
Arrows =    numpy.tile([0,1],nTrials//2)
Positions = numpy.repeat([0,1,2],nTrials//3)

factorial=  numpy.column_stack([Arrows,Positions])


#set the directory
my_directory = os.getcwd()

#dialogbox
info        = {"Participant number": "0", "Name": "", "Age": 0, "Gender":['M', 'V','X'] ,"Hand preference": ['left-handed', 'right-handed','ambidexter']}

## make sure the data file has a novel name
already_exists = True
while already_exists:
    
    ## present the dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title ="Test 4")
    
    ## construct the name of the folder that will hold the data
    directory_to_write_to = my_directory + "/data"
    
    ## if the folder doesn't exist yet, make it
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    ## construct the name of the data file
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"])
    
    # Esther: als je de data rechtstreeks exporteert in plaats van via de ExperimentHandler, is het hier nodig om meteen de extensie aan de filenaam te plakken
    
    ## check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
        
        ## if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        ## if the data file name has already been used, ask the participant to inser a different participant number or session number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Participant number already exists, please try again.")
        myDlg2.show()

# Esther: de manier waarop je hier de participantinfo opslaat heeft niet dezelfde dimensies als de andere arrays die je later zal willen samenvoegen
#Store all participantinfo except  name
ParticipantInfo[0]= info['Participant number']
ParticipantInfo[1]= info['Age']
ParticipantInfo[2]= info['Gender']
ParticipantInfo[3]= info['Hand preference']


#welcome Participant
Welcome=visual.TextStim(win,text= "Welkom, {0}. \n\nDruk op de spatiebalk om aan het experiment te beginnen.".format(info["Name"]))
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

#blockloop
for block in range(nBlocks): 
    numpy.random.shuffle(factorial)
    
    #determine tasktype
    if block%3==0:
        type="Positie"
        Instructions.text= InstructionOptions[0]
        
    else:
        type="Richting"
        Instructions.text= InstructionOptions[1]
    
    Instructions.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    for trial in range (nTrials):
        TrialIndex=block*trial + trial
        
        #determine stimulus characteristics
        TrialArrow[TrialIndex]=    ArrowOptions[factorial[trial,0]]
        TrialPosition[TrialIndex]=  PositionOptions[factorial[trial,1]]
        if (factorial[trial,0]==0 and factorial[trial,1]==0) or (factorial[trial,0]==1 and factorial[trial,1]==2):
            Congruency[TrialIndex]= "Congruent"
        else:
            Congruency[TrialIndex]= "Incongruent"
        
        # Esther: hier hadden we graag ook nog de neutrale trials apart bedoeld gezien
        
        Stimulus.text=ArrowOptions[factorial[trial,0]]
        Stimulus.pos=(PositionOptions[factorial[trial,1]],0)
        
        #draw stimulus and register response and RT
        Stimulus.draw()
        event.clearEvents(eventType = "keyboard")
        
        win.flip()
        clock.reset()
        
        keys = event.waitKeys(keyList = ['left','right','down'])
        ThisRT= clock.getTime()
        
        #store values
        ActualResp[TrialIndex]= keys[0]
        RT[TrialIndex]= ThisRT
        
        #determine  correct response and accuracy
        ResponseMapping[TrialIndex]=type
        
        if type=="Positie":
            if factorial[trial,1]==0:
                CorrectResp[TrialIndex]="left"
            if factorial[trial,1]==1:
                CorrectResp[TrialIndex]="down"
            if factorial[trial,1]==2:
                CorrectResp[TrialIndex]="right"
        if type=="Richting":
            if factorial[trial,0]==0:
                CorrectResp[TrialIndex]='left'
            if factorial[trial,0]==1:
                CorrectResp[TrialIndex]='right'
        
        if CorrectResp[TrialIndex]==keys[0]:
            Accuracy[TrialIndex]=1
        else:
            Accuracy[TrialIndex]=0

#End of the experiment
Bye=visual.TextStim(win,text= "Dit was het einde van het experiment. Bedankt voor je deelname, {0}. \n\nDruk op de spatiebalk om af te sluiten.".format(info["Name"]))
Bye.draw()
win.flip()
event.waitKeys(keyList = "space")

# ESther: vergeet congruency niet mee op te slaan!

#generate data file
data= numpy.column_stack([ParticipantInfo,TrialNumber,BlockNumber,TrialinBlock,TrialArrow,TrialPosition,CorrectResp, ActualResp, RT, Accuracy, ResponseMapping])


"""
# Export as a comma separated file
numpy.savetxt(file_name, data, delimiter = '\t ') 

ERROR: TypeError: Mismatch between array dtype ('<U15') and format specifier ('%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e')
"""
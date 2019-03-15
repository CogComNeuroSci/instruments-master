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
    
    ## check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
        
        ## if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        ## if the data file name has already been used, ask the participant to inser a different participant number or session number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Participant number already exists, please try again.")
        myDlg2.show()

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


#generate random sequence for tasktype
Tasktype = numpy.repeat([0,1,1],nBlocks//3)

print
#check order for repeats
order=False

"""
PSYCHOPY GAAT HIERDOOR STEEDS IN "PYTHON REAGEERT NIET MEER" MAAR JE SNAPT HET IDEE WEL ZEKER?

## Esther: haha, ja, ik snap wat je probeert te doen!
## Esther: het probleem is dat je code enkel zal werken als je shuffling meteen goed zit van aan het begin van de for-loop, niet?
## Esther: dus alle reshufflingen tijdens de for-loop (op de laatste na) zijn overbodig en daardoor werkt je algoritme wat trager
## Esther: het extra stapje vooruit is nu om de vergelijkingen via 1 bewerking te kunnen doen in plaats van via een for-loop
## Esther: het vergt even wat denkwerk, maar het maakt je code een pak vlotter in uitvoering

while order ==False:
    reshuffled=0
    for task in range(nBlocks-1):
        if Tasktype [task]== 0 and Tasktype[task+1]==0:
            numpy.random.shuffle(Tasktype)
            reshuffled+=1
        if task==nBlocks-1 and reshuffled==0:
            order=True
"""

#blockloop
for block in range(nBlocks): 
    numpy.random.shuffle(factorial)
    
    #determine tasktype
    if Tasktype[block]==0:
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

#generate data file
data= numpy.column_stack([ParticipantInfo,TrialNumber,BlockNumber,TrialinBlock,TrialArrow,TrialPosition,CorrectResp, ActualResp, RT, Accuracy, ResponseMapping])

#crosstables -> convert to pandas
dataFrame = pandas.DataFrame.from_records(data)
dataFrame.columns = ["ParticipantInfo","TrialNumber","BlockNumber","TrialinBlock","TrialArrow","TrialPosition","CorrectResp", "ActualResp", "RT", "Accuracy", "ResponseMapping"]

# Esther: het is heel goed dat je hier kruistabellen gebruikt, maar het is wel een beetje vijgen na pasen omdat de trials al allemaal uitgevoerd zijn

# cross the positions, responsemapping and arrowtype
print(pandas.crosstab(dataFrame.TrialPosition, dataFrame.TrialArrow))

print(pandas.crosstab(dataFrame.TrialPosition, dataFrame.ResponseMapping))

print(pandas.crosstab(dataFrame.ResponseMapping, dataFrame.TrialArrow))

"""
# Export as a comma separated file
numpy.savetxt(file_name, data, delimiter = '\t ') 

ERROR: TypeError: Mismatch between array dtype ('<U15') and format specifier ('%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e,%.18e')
"""
from psychopy import visual, event, core,gui
import time, numpy, os, pandas

#dialoog venster invoeren
info = {'Naam':'', 'Proefpersoonnummer': '00', 'Leeftijd':'00', 'Gender':['man', 'vrouw', 'derde gender'],
    'Handvoorkeur':['links', 'rechts', 'ambidexter']}


# determine the current working directory
directory_to_write = os.getcwd()



# keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title='TestExperiment')
    naam= info["Naam"]
    proefpersoonnummer= info["Proefpersoonnummer"]
    leeftijd= info["Leeftijd"]
    gender= info["Gender"]
    handvoorkeur= info["Handvoorkeur"]
    
    # determine the name of the subject directory
    directory  = "data"
    
    # if the directory doesn't exist yet, make it now
    if not os.path.isdir(directory):
        os.mkdir(directory)
    
    # determine the file name
    file_name = "Test4_subject_"+proefpersoonnummer+".csv"
    print(file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False
    else:
        #window maken
        win= visual.Window(size= [1000,700], units='norm')
        Waarschuwing= visual.TextStim(win, text= "Dit proefpersoonnummer bestaat al, kies een ander!")
        Waarschuwing.draw()
        win.flip()
        time.sleep(1)
        win.close()


# we have found a new file name, ready to start
print("OK, let's get started!")


#window maken
win= visual.Window(size= [1000,700], units='norm')

#aantal blokken 
Nblocks= 2

#aantal trials per block
Ntrials= 60

#veranderingen per trial
pijltjesOpties= numpy.array([">", "<"])
positiesOpties= numpy.array([-0.5, 0, 0.5])

#aantal unieke trials berekenen
Nunique= len(positiesOpties)*len(pijltjesOpties)

#juist aantal maken
pijltjes= numpy.repeat(pijltjesOpties, len(positiesOpties))
posities= numpy.tile(positiesOpties, len(pijltjesOpties))

#lege kolom aan matrix toevoegen voor RT,respons en congruentie
RT= numpy.repeat(-99.9, Nunique)
respons= numpy.repeat(" ", Nunique)
congruentie= numpy.repeat(" ", Nunique)

#trialmatrix maken
trials= numpy.column_stack([ pijltjes, posities, RT, respons, congruentie])
print(trials)

#persoonlijke gegevens van proefpersoon in matrix zetten, behalve naam

#aantal keer trial matrix herhalen
Nrep= int(Ntrials/Nunique)

#matrix herhalen  zodat er voldoende trials in een blok zijn
Bloktrials= numpy.tile(trials, (Nrep, 1))
print(len(Bloktrials))

#stimulus aanmaken
stim= visual.TextStim(win)

#Instructies
#richting_instructies= "reageer op de richting van de pijltjes. druk op de linker pijltjestoets als de pijl naar links staat en op de rechterpijltjetoets als de pijl naar rechts wijst.\nDruk spatie om te beginnen"
#plaats_instructies:= "reageer op de plaats van de pijltjes. druk op de linker pijltjestoets als de pijl links staat en op de rechterpijltjetoets als de pijl rechts staat. Als de pijl in het midden staat druk dan op het pijltje naar onder.\nDruk spatie om te beginnen"



#tekst maken
Welkom= visual.TextStim(win, text= "Welkom, {0}!\nDruk op spatie om verder te gaan!".format(info["Naam"]))
#Instructies= visual.TextStim(win)
Einde= visual.TextStim(win, text= "Bedankt voor uw deelname!")

Welkom.draw()
win.flip()
event.waitKeys(keyList= ["space"])

#Instructies.draw()
#win.flip()
#event.waitKeys(keyList= ["space"])

#klok invoegen
klok= core.Clock()

for block in range(Nblocks):
    
    #trials shuffelen, zodat ze random zijn
     numpy.random.shuffle(Bloktrials)
     
     for trial in range (len(Bloktrials)):
        #stimulus invoegen
        stim.text= Bloktrials[trial, 0]
        stim.pos= (Bloktrials[trial,1] ,0)
        
        stim.draw()
        event.clearEvents(eventType= "keyboard")
        
        win.flip()
        
        klok.reset()
        
        respons= event.waitKeys(keyList= ["left", "down", "right"])
        
        RT= klok.getTime()
        
        
        #huidige trials
        huidige_trials= range(Ntrials+(Ntrials*block))
        
        #respons wegschrijven
        #Bloktrials[huidige_trials,3]= respons
        
        #RT wegschrijven
        #Bloktrials[huidige_trials,2]= RT
        
        #congruentie bepalen
#        if Bloktrials[huidige_trials, 0] == pijltjesOpties[1,0] and Bloktrials[huidige_trials,1]== positiesOpties[0,0]:
#            Bloktrials[huidige_trials,4]= "congruent"

#        elif Bloktrials[huidige_trials, 0] == pijltjesOpties[0,0] and Bloktrials[huidige_trials,1]== positiesOpties[2,0]:
#            Bloktrials[huidige_trials,4]= "congruent"
#            
#        elif Bloktrials[huidige_trials,1]== positiesOpties[1,0]:
#            Bloktrials[huidige_trials,4]="neutraal"

#        else:
#            Bloktrials[huidige_trials,4]= "incongruent"

#einde op scherm plaatsen
Einde.draw()
win.flip()
event.waitKeys(keyList= ["space"])


#dataframe maken al weg te schrijven
dataFrame= pandas.DataFrame.from_records(Bloktrials)
dataFrame.columns= ["pijltjes", "posities", "RT", "respons", "congruentie"]

#validation
print(pandas.crosstab([dataFrame.pijltjes], [dataFrame.posities]))

#data wegschrijven
dataFrame.to_csv(path_or_buf= "Test4_subject_"+proefpersoonnummer+".csv", index= False)

#window sluiten
win.close()
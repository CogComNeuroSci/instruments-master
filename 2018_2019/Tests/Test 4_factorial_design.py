# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 09:52:13 2019

@author: esther
"""

import numpy
from psychopy import data


ArrowOptions    = numpy.array(["<",">"])
PositionOptions = numpy.array([-0.5,0.5,0])
RespOptions     = numpy.array(["left","right","down"])

Narrows         = len(ArrowOptions)
Npositions      = len(PositionOptions)
Nunique         = Narrows * Npositions

UniqueTrials    = numpy.array(range(Nunique)) 

## make the 2-by-3 factorial design
Arrow           = numpy.floor(UniqueTrials / Npositions)
Position        = numpy.floor(UniqueTrials / 1) %  Npositions

## combine arrays in trial matrix
trialmatrix     = numpy.column_stack([Arrow, Position])

print(trialmatrix)

####################################################################

## make the 2-by-3 factorial design
Arrow           = numpy.floor(UniqueTrials/Narrows)
Position        = numpy.floor(UniqueTrials/1) % Narrows

## combine arrays in trial matrix
trialmatrix     = numpy.column_stack([Arrow, Position])

print(trialmatrix)

#######################################################################

## make the 2-by-3 factorial design
Arrow           = numpy.repeat(ArrowOptions, Npositions)
Position        = numpy.tile(PositionOptions, Narrows)

## combine arrays in trial matrix
trialmatrix     = numpy.column_stack([Arrow, Position])

print(trialmatrix)

####################################################################

## make the 2-by-3 factorial design
Arrow           = numpy.floor(UniqueTrials/Npositions)
Position        = numpy.floor(UniqueTrials/Narrows)

## combine arrays in trial matrix
trialmatrix     = numpy.column_stack([Arrow, Position])

print(trialmatrix)

####################################################################

## make the 2-by-3 factorial design
Arrow           = numpy.floor(UniqueTrials/Narrows)
Position        = numpy.floor(UniqueTrials/1) % Npositions

## combine arrays in trial matrix
trialmatrix     = numpy.column_stack([Arrow, Position])

print(trialmatrix)

####################################################################

## make the 2-by-3 factorial design
Arrow           = numpy.floor(UniqueTrials/Npositions)
Position        = numpy.floor(UniqueTrials/1) % Narrows

## combine arrays in trial matrix
trialmatrix     = numpy.column_stack([Arrow, Position])

print(trialmatrix)

#####################################################################

ArrowOptions    = numpy.resize(numpy.array(["<",">"]),60)
PositionOptions = numpy.resize(numpy.array([-0.5,0.5,0]),60)

Design = data.createFactorialTrialList({"Arrow": ArrowOptions, "Position": PositionOptions})

## Esther: hier ga je veel te veel combinaties maken

####################################################################

## make the 2-by-3 factorial design
Design = data.createFactorialTrialList({"Arrow": ArrowOptions, "Position": PositionOptions})
ArrowOptions    = numpy.array(["<",">"])
PositionOptions = numpy.array([-0.5,0.5,0])

# Esther: dit was op zich een heel goed idee, maar je spant de kar voor het paard door eerst het design te maken en dan pas de ingrediënten te voorzien

####################################################################

## combine arrays in trial matrix
trialmatrix     = numpy.column_stack([ArrowOptions, PositionOptions])

# Esther: gezien stimuli en positions een andere lengte hebben kan je ze zeker niet combineren in één array

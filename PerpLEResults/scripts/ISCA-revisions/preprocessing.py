#!/usr/bin/env python
#from TKinter import *
import glob
import statistics
import os
import numpy as np
#import matplotlib.pyplot as plt
import argparse

AXIS_FONTSIZE = 44
TICK_FONTSIZE = 40
INPUTS_FONTSIZE = 32
width = 0.80

def create_vp_axis(ax1, ind, yticks, ylabel):
  num_apps = 3
  num_inputs = 3
  ind = np.arange(1, 4)
  app_inds = []
  print(ind)
  seps = []
  for i in ind:
    app_inds = app_inds + [i-width/num_apps, i, i+width/num_apps]
    if i == ind[len(ind)-1]:
      continue
    else:
      seps = seps + [i + 0.5]
  print(app_inds)
  ax2 = ax1.twiny()
  ax3 = ax1.twiny()
  ax4 = ax1.twinx()

  scale = 0.75
  app_labels = ('Out 1', 'Out 2', 'Out 3', 'Out 4','Out 1', 'Out 2', 'Out 3', 'Out 4','Out 1', 'Out 2', 'Out 3', 'Out 4','Out 5', 'Out 6', 'Out 7', 'Out 8')
  xticks = ('sb', 'lb', 'podwr001')

  ax1.set_xlim([0.5, num_inputs+0.5])
  ax1.set_xticks(app_inds)
  ax1.set_xticklabels(app_labels, fontsize=scale*INPUTS_FONTSIZE)
  ax1.set_ylim([0, yticks[len(yticks)-1]])
  ax1.set_yticks(yticks)
  ax1.set_yticklabels(yticks, fontsize=scale*TICK_FONTSIZE)
  ax1.set_ylabel(ylabel, fontsize=scale*AXIS_FONTSIZE)
  ax1.tick_params(direction='inout', length=20, width=1)

  ax2.set_xlim([0.5, num_inputs+0.5])
  ax2.xaxis.set_ticks_position("bottom")
  ax2.xaxis.set_label_position("bottom")
  ax2.spines["bottom"].set_position(("axes", -0.07))
  ax2.spines["bottom"].set_visible(False)
  ax2.set_xticks(ind)
  ax2.set_xticklabels(xticks, fontsize=scale*AXIS_FONTSIZE)
  ax2.tick_params(length=0)

  ax3.set_xlim([0.5, num_apps+0.5])
  ax3.xaxis.set_ticks_position("bottom")
  ax3.set_xticks(seps)
  ax3.set_xticklabels([])
  ax3.tick_params(direction='inout', length=40, width=1)

  ax4.set_ylim([0, yticks[len(yticks)-1]])
  ax4.set_yticks(yticks)
  ax4.set_yticklabels([])
  ax4.tick_params(direction='inout', length=20, width=1, labelleft=False, labelright=True)

def mlp():
    N = 16
    ind = np.arange(1, 4)
    s1a = 1
    s1b = 2
    s1c = 3
    s1d = 4
    s2a = 4
    s2b = 5
    s2c = 6
    s2d = 7
    s3a = 7
    s3b = 8
    s3c = 9
    s3d = 10
    s3e = 11
    s3f = 12
    s3g = 13
    s3h = 14

#    s1a = stats[0][1]
#    s1b = stats[0][4]
#    s1c = stats[0][3]
#    s2a = stats[1][1]
#    s2b = stats[1][4]
#    s2c = stats[1][3]
#    s3a = stats[2][1]
#    s3b = stats[2][4]
#    s3c = stats[2][3]

    fig = plt.figure(figsize=(32.0,24.0))
    fig.subplots_adjust(bottom=0.1)
    ax1 = fig.add_subplot(111)

    dark = 'black'
    medium = 'darkgrey'
    light = 'white'

    psb1a = ax1.bar(ind-8*width/N, s1a, width/N, color=dark, linewidth=1, edgecolor=['black'])
    psb1b = ax1.bar(ind-7*width/N, s1b, width/N, color=medium, linewidth=1, edgecolor=['black'])
    psb1c = ax1.bar(ind-6*width/N, s1c, width/N, color=light, linewidth=1, edgecolor=['black'])
    psb1d = ax1.bar(ind-5*width/N, s1d, width/N, color=dark, linewidth=1, edgecolor=['black'])
    # 2nd
    psb2a = ax1.bar(ind-4*width/N, s2a, width/N, color=dark, linewidth=1, edgecolor=['black'])
    psb2b = ax1.bar(ind-3*width/N, s2b, width/N, color=medium, linewidth=1, edgecolor=['black'])
    psb2c = ax1.bar(ind-2*width/N, s2c, width/N, color=light, linewidth=1, edgecolor=['black'])
    psb2d = ax1.bar(ind-width/N, s2d, width/N, color=dark, linewidth=1, edgecolor=['black'])
   
    psb3a = ax1.bar(ind, s3a, width/N, color=medium, linewidth=1, edgecolor=['black'])
    psb3b = ax1.bar(ind+width/N, s3b, width/N, color=light, linewidth=1, edgecolor=['black'])
    psb3c = ax1.bar(ind+2*width/N, s3c, width/N, color=dark, linewidth=1, edgecolor=['black'])
    psb3d = ax1.bar(ind+3*width/N, s3d, width/N, color=medium, linewidth=1, edgecolor=['black'])
    psb3e = ax1.bar(ind+4*width/N, s3e, width/N, color=light, linewidth=1, edgecolor=['black'])
    psb3f = ax1.bar(ind+5*width/N, s3f, width/N, color=dark, linewidth=1, edgecolor=['black'])
    psb3g = ax1.bar(ind+6*width/N, s3g, width/N, color=medium, linewidth=1, edgecolor=['black'])
    psb3h = ax1.bar(ind+7*width/N, s3h, width/N, color=light, linewidth=1, edgecolor=['black'])


    yticks = np.arange(20)
    ylabel = 'Number of Outcome Occurrences' #'Improvement'
    create_vp_axis(ax1, ind, yticks, ylabel)

    legend = ('1 litmus7', '2 PerpLE')
    plt.legend((psb1a[0], psb1b[0]), legend, loc=2, fontsize=48)
    #plt.show()
    plt.savefig("Outcomes.pdf", bbox_inches='tight')
  
def heuristic_accuracy(perple_data, litmus_data, testnames):
    retstr = ""
    ratios = [list() for x in range(2)]
    retstr += "\tPerpLE Heuristic\n"
    perple_perf = returnSummary(perple_data,2,1)
    litmus_perf = returnSummary(litmus_data,2,2)
    perple_perf.append(litmus_perf[1])
    perple_perf.append(litmus_perf[2])
    perple_perf.append(testnames)
    for i in range(0,len(perple_perf[2])):
        if perple_perf[1][i] > 0:
            ratios[0].append(float(perple_perf[2][i]/perple_perf[1][i]))
            ratios[1].append(perple_perf[12][i])
            print(perple_perf[1][i],perple_perf[2][i],perple_perf[12][i])
    plot_data = returnSorted(ratios,1)
    for i in range(0,len(plot_data[0])):
        retstr += plot_data[1][i]
        retstr += "\t"
        retstr += str(plot_data[0][i]*100) # select 100000 + runtime
        retstr += "\n"
    retstr += "Geomean"
    retstr += "\t"
    geo = statistics.mean(ratios[0])
    geo2 = geo_mean(ratios[0])
    print(geo)
    print(geo2)
    retstr += str(geo*100)
    retstr += "\t"
    retstr += "\n"
    return retstr



def georates(perple_data, litmus_data, testnames):
    # outcomes with 10000 iterations, start from 100
    retstr = ""
    retstr += "\tPerpLE (Checker)\tPerpLE (Heuristic)\tlitmus7 Timebase \tlitmus7 User \tlitmus7 Userfence \tlitmus7 Pthread \tlitmus7 None\n" 
    for i in range(0,7):
        perple_perf = returnSummary(perple_data,i,1)
        # print(perple_perf)
        litmus_perf = returnSummary(litmus_data,i,2)
        perple_perf.append(litmus_perf[1])
        perple_perf.append(litmus_perf[2])
        perple_perf.append(litmus_perf[3])
        perple_perf.append(litmus_perf[5])
        perple_perf.append(litmus_perf[6])
        perple_perf.append(litmus_perf[7])
        perple_perf.append(litmus_perf[9])
        perple_perf.append(litmus_perf[10])
        perple_perf.append(litmus_perf[11])
        perple_perf.append(litmus_perf[13])
        perple_perf.append(litmus_perf[14])
        perple_perf.append(litmus_perf[15])
        perple_perf.append(litmus_perf[17])
        perple_perf.append(litmus_perf[18])
        perple_perf.append(litmus_perf[19])
        perple_perf.append(testnames)
        plot_data = returnSorted(perple_perf,25)
        l1 = list(plot_data[12]) #timebase
        l4 = list(plot_data[15]) #user
        l5 = list(plot_data[18]) #userfence
        l6 = list(plot_data[21]) #pthread
        l7 = list(plot_data[24]) #none
        l2 = list(plot_data[6])
        l3 = list(plot_data[7])
        l1 = [i for i in l1 if i != 0.0]
        l4 = [i for i in l4 if i != 0.0]
        l5 = [i for i in l5 if i != 0.0]
        l6 = [i for i in l6 if i != 0.0]
        l7 = [i for i in l7 if i != 0.0]
        l2 = [i for i in l2 if i != 0.0]
        l3 = [i for i in l3 if i != 0.0]
        #print(l1)
        #print(l2)
        #print(l3)
        if l1:
            geolitmusT = geo_mean(l1)
        else:
            geolitmusT = 0.0
        print(geolitmusT)
        if l2:
            geoChecker = geo_mean(l2)
        else:
            geoChecker = 0.0
        print(geoChecker)
        if l3:
            geoHeuristic = geo_mean(l3)
        else:
            geoHeuristic = 0.0
        print(geoHeuristic)
        if l4:
            geolitmus = geo_mean(l4)
        else:
            geolitmus = 0.0
        if l5:
            geolitmusUf = geo_mean(l5)
        else:
            geolitmusUf = 0.0
        if l6:
            geolitmusP = geo_mean(l6)
        else:
            geolitmusP = 0.0
        if l7:
            geolitmusN = geo_mean(l7)
        else:
            geolitmusN = 0.0

        retstr += str(int(plot_data[0][0]))
        retstr += "\t"
        retstr += str(geoChecker) # select 100000 + runtime
        retstr += "\t"
        retstr += str(geoHeuristic)
        retstr += "\t"
        retstr += str(geolitmus)
        retstr += "\t"
        retstr += str(geolitmusT)
        retstr += "\t"
        retstr += str(geolitmusUf)
        retstr += "\t"
        retstr += str(geolitmusP)
        retstr += "\t"
        retstr += str(geolitmusN)
        #retstr += "\t"
        #if geolitmus>0:
        #    retstr += str(geoHeuristic/geolitmus)
        #else:
        #    retstr += str(0)
        retstr += "\n"
    return retstr


def rates(perple_data, litmus_data, testnames):
    # outcomes with 10000 iterations, start from 100
    retstr = ""
    retstr += "\tPerpLE (Counter)\tPerpLE (Heuristic)\tlitmus7\n"
    perple_perf = returnSummary(perple_data,2,1)
    litmus_perf = returnSummary(litmus_data,2,2)
    perple_perf.append(litmus_perf[1])
    perple_perf.append(litmus_perf[2])
    perple_perf.append(litmus_perf[3])
    perple_perf.append(testnames)
    plot_data = returnSorted(perple_perf,13)
    for i in range(0,len(plot_data[12])):
        if perple_perf[1][i] > 0:
            retstr += plot_data[13][i]
            retstr += "\t"
            retstr += str(plot_data[6][i]) # select 100000 + runtime
            retstr += "\t"
            retstr += str(plot_data[7][i])
            retstr += "\t"
            retstr += str(plot_data[12][i])
            retstr += "\n"
#    retstr += "Geomean\t"
#    geolitmus = geo_mean(plot_data[11])
#    geoChecker = geo_mean(plot_data[8])
#    geoHeuristic = geo_mean(plot_data[9])
#    retstr += str(geolitmus)
#    retstr += "\t"
#    retstr += str(geoChecker)
#    retstr += "\t"
#    retstr += str(geoHeuristic)
#    retstr += "\n"
    return retstr





def single_outcomes(plot_data, perple_data, litmus_data, testnames):
    # outcomes with 10000 iterations, start from 100
    retstr = ""
    retstr += "\tPerpLE (Checker)\tPerpLE (Heuristic)\tlitmus7 Timebase \tlitmus7 User \tlitmus7 Userfence \tlitmus7 Pthread \tlitmus7 None\n" 
#    perple_perf = returnSummary(perple_data,2,1)
#    litmus_perf = returnSummary(litmus_data,2,2)
#    perple_perf.append(litmus_perf[1])
#    perple_perf.append(litmus_perf[2])
#    perple_perf.append(testnames)
#    plot_data = returnSorted(perple_perf,12)
    for i in range(0,len(plot_data[20])):
        retstr += plot_data[20][i]
        retstr += "\t"
        retstr += str(plot_data[1][i]) # select 100000 + runtime
        retstr += "\t"
        retstr += str(plot_data[2][i]) #perple outcomes
        retstr += "\t"
        retstr += str(plot_data[10][i]) #litmus timebase#
        retstr += "\t"
        retstr += str(plot_data[12][i]) #litmus timebase# 
        retstr += "\t"
        retstr += str(plot_data[14][i]) #litmus timebase#
        retstr += "\t"
        retstr += str(plot_data[18][i]) #litmus timebase#
        retstr += "\t"
        retstr += str(plot_data[16][i]) #litmus timebase#
        retstr += "\n"
#    retstr += "Geomean\t"
#    geolitmus = geo_mean(plot_data[11])
#    geoChecker = geo_mean(plot_data[8])
#    geoHeuristic = geo_mean(plot_data[9])
#    retstr += str(geolitmus)
#    retstr += "\t"
#    retstr += str(geoChecker)
#    retstr += "\t"
#    retstr += str(geoHeuristic)
#    retstr += "\n"
    return retstr

def generate_means_breakdown(perple_data,litmus_data,testnames):
    retstr = ""
    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    for i in range(2,7): # size ranges
        perple_perf = returnSummary(perple_data,i,1)
        litmus_perf = returnSummary(litmus_data,i,2)
        perple_perf.append(litmus_perf[1])
        perple_perf.append(litmus_perf[2])
        perple_perf.append(testnames)
        plot_data = returnSorted(perple_perf,12)
        retstr += str(int(plot_data[0][0]))
        retstr += "\t"
        geolitmus = geo_mean(plot_data[11])
        retstr += str(geolitmus)
        retstr += "\t"
        geoChecker = geo_mean(plot_data[8])
        geoHeuristic = geo_mean(plot_data[9])
       # print(geolitmus, geoChecker,geoHeuristic)
        if plot_data[0][0] <= 100000:
            retstr += str(geoChecker)
        else:
            retstr += "?"
        retstr += "\t"
        retstr += str(geoHeuristic)
        retstr += "\n"
    return retstr


def generate_means(perple_data,litmus_data,testnames):
    retstr = ""
    retstr += "\tlitmus7 user\tPerpLE (Checker)\tPerpLE (Heuristic)\tlitmus7 Timebase\tlitmus7 Userfence \tlitmus7 None \tlitmus7 Pthread\n"
    for i in range(2,7): # size ranges
        perple_perf = returnSummary(perple_data,i,1)
        litmus_perf = returnSummary(litmus_data,i,2)
        perple_perf.append(litmus_perf[1])
        perple_perf.append(litmus_perf[2])
        perple_perf.append(testnames)
        plot_data = returnSorted(perple_perf,12)
        retstr += str(int(plot_data[0][0]))
        retstr += "\t"
        retstr += str(1.0)
        retstr += "\t"
        geolitmus = geo_mean(plot_data[11])
        geoChecker = geo_mean(plot_data[8])
        geoHeuristic = geo_mean(plot_data[9])
        #print(geolitmus, geoChecker,geoHeuristic)
        if plot_data[0][0] <= 100000:
            retstr += str(geolitmus/geoChecker)
        else:
            retstr += "?"
        retstr += "\t"
        retstr += str(geolitmus/geoHeuristic)
        retstr += "\n"
    return retstr

def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))

def returnSorted(array,sorter):
    sortArray = list()
    for i in range(0,len(array)):
        temp1,temp2= zip(*sorted(zip(array[sorter],array[i])))
        sortArray.append(list(temp2))
    return sortArray

def returnSummary(array,size,mode):
    sArray = list()
    if mode==1:
        #print(array[0][3][4])
        sArray = [list() for x in range(10)]
    if mode==2:
        sArray = [list() for x in range(20)]  # For all litmus sync options
    if mode == 1: 
        #print(array[0][3][5])
        for i in range(0,len(array[0])):
            for j in range(0,len(sArray)):
                if j < 8:
                    sArray[j].append(array[0][i][size][j])
                elif j == 8:
                    sArray[j].append(sArray[3][i]+sArray[4][i])
                elif j == 9:
                    sArray[j].append(sArray[3][i]+sArray[5][i])
    else:
        for i in range(0,len(array[0])):
            for j in range(0,len(sArray)):
                colIndex = j/4
                sArray[j].append(array[colIndex][i][size][j%4])
                    #sArray[j].append(array[0][i][size][j])
        #print(sArray)
    return sArray

def main():
    fields_perple = {"CheckerCycles":1,"HeurCycles":2,"HarnessT":3,"CheckerT":4,"HeurT":5,"CheckerR":6,"HeurR":7}
    fields_litmus = {"LitmusCycles":1,"LitmusT":2,"LitmusR":3}
    
    # Currently perple is evaluated together with Litmus with -barrier timebase
    folderNames = ["x86tso-2fence-timebase-100M","x86tso-2fence-user-100M","x86tso-2fence-userfence-100M","x86tso-2fence-none-100M","x86tso-2fence-pthread-100M"]
    litmusCnt = 0
    litmuses = []
    perples = []
    perple_data = []
    for folderNum in range(0,len(folderNames)): 
        folderString = "../" + folderNames[folderNum] + "/*"
        folderRPL = "../" + folderNames[folderNum] + "/"
    #	list_of_folders = glob.glob('../x86tso-2fence-timebase-100M/*')
        list_of_folders = glob.glob(folderString)     
        testnames = list()
        litmus_data = []
        perple_data = []
        for folder in list_of_folders:
            name = folder.replace(folderRPL,"")
            testnames.append(name)
            subdirectory = folder + "/*"
            list_of_files = glob.glob(subdirectory)
            latest_file = max(list_of_files, key=os.path.getctime)
            f = open(latest_file, 'r')
            resultcnt = 0 
            perple = []
            litmus = []
            for line in f:
                if litmusCnt >= 1:
                    resultcnt = 2
                if(line == '\n' or line.find("Summary")>=0):
                    continue
                line = line.replace(" ","")
                line = line.replace('\n',"")
                rawdata = line.split('|')
                dataline = []
                if(rawdata and resultcnt == 0 and litmusCnt < 1 and line.find("Iterations") >= 0):
                    resultcnt = 1 #parse perpLE
                elif(rawdata and resultcnt == 1 and line.find("Iterations") >= 0):
                    resultcnt = 2 #parse Litmus
                elif(rawdata and resultcnt == 1 and line.find("Iterations") < 0): 
                    for field in rawdata:
               #     print(field)
                #    print(latest_file)
                        field = dataline.append(float(field))
                    perple.append(dataline)
                elif(rawdata and resultcnt == 2 and line.find("Iterations") < 0):
                    for field in rawdata:
                        field = dataline.append(float(field))
                    litmus.append(dataline)
            if litmusCnt < 1:
                perple_data.append(perple)
            litmus_data.append(litmus)
        #print(latest_file,len(perple),len(litmus))
        retstr =""
        litmuses.append(litmus_data)
        if litmusCnt < 1:
            #print(perple_data)
            perples.append(perple_data)
        litmusCnt += 1
# runtimes with 10000 iterations, start from 100
#    f = open("runtimes-10k.csv","w+")
#    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    #print(perples[0])
#    perple_perf = returnSummary(perples,2,1)
#    litmus_perf = returnSummary(litmuses,2,2)
#    perple_perf.append(litmus_perf[1])
#    perple_perf.append(litmus_perf[2])
#    perple_perf.append(testnames)
#    plot_data = returnSorted(perple_perf,12)
#    for i in range(0,len(plot_data[12])):
#        retstr += plot_data[12][i]
#        retstr += "\t"
#        retstr += str(plot_data[11][i]) # select 100000 + runtime
#        retstr += "\t"
#        retstr += str(plot_data[8][i])
#        retstr += "\t"
#        retstr += str(plot_data[9][i])
#        retstr += "\n"
#    retstr += "Geomean\t"
#    geolitmus = geo_mean(plot_data[11])
#    geoChecker = geo_mean(plot_data[8])
#    geoHeuristic = geo_mean(plot_data[9])
#    retstr += str(geolitmus)
#    retstr += "\t"
#    retstr += str(geoChecker)
#    retstr += "\t"
#    retstr += str(geoHeuristic)
#    retstr += "\n"
#    f.write(retstr)
#    f.close()
#    retstr = ""
    # speedup for 10k 
    # switch sorting below 
    #plot_data = returnSorted(perple_perf,9)
#    f = open("speedup-10k.csv","w+")
#    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
#    for i in range(0,len(plot_data[12])):
#        retstr += plot_data[12][i]
#        retstr += "\t"
#        retstr += str(1.0)
        #retstr += str(plot_data[11][i]) # select 100000 + runtime
#        retstr += "\t"
#        checkerTime = float(plot_data[11][i])/float(plot_data[8][i])
#        retstr += str(checkerTime)
#        retstr += "\t"
#        heuristicTime = float(plot_data[11][i])/float(plot_data[9][i])
#        retstr += str(heuristicTime)
#        retstr += "\n"
#    retstr += "Geomean\t"
#    geolitmus = geo_mean(plot_data[11])
#    geoChecker = geo_mean(plot_data[8])
#    geoHeuristic = geo_mean(plot_data[9])
#    retstr += str(1.0)
#    retstr += "\t"
#    retstr += str(geolitmus/geoChecker)
#    retstr += "\t"
#    retstr += str(geolitmus/geoHeuristic)
#    retstr += "\n"
#    f.write(retstr)
#    f.close()
#    retstr = ""

# runtimes with 100000 iterations, start from 100
#    f = open("runtimes-100k.csv","w+")
#    retstr += "\tlitmus7\tPerpLE (Checker)\tPerpLE (Heuristic)\n"
    perple_perf = returnSummary(perples,2,1)
    litmus_perf = returnSummary(litmuses,2,2)
    #print(litmus_perf)
    perple_perf.append(litmus_perf[1])
    perple_perf.append(litmus_perf[2])
    perple_perf.append(litmus_perf[5])
    perple_perf.append(litmus_perf[6])
    perple_perf.append(litmus_perf[9])
    perple_perf.append(litmus_perf[10])
    perple_perf.append(litmus_perf[13])
    perple_perf.append(litmus_perf[14])
    perple_perf.append(litmus_perf[17])
    perple_perf.append(litmus_perf[18])
    perple_perf.append(testnames)
    print(testnames)
    plot_data = returnSorted(perple_perf,20)
#    for i in range(0,len(plot_data[20])):
#        retstr += plot_data[20][i]
#        retstr += "\t"
#        retstr += str(plot_data[11][i]) # select 100000 + runtime
#        retstr += "\t"
#        retstr += str(plot_data[8][i])
#        retstr += "\t"
#        retstr += str(plot_data[9][i])
#        retstr += "\n"
#    retstr += "Geomean\t"
#    geolitmus = geo_mean(plot_data[11])
#    geoChecker = geo_mean(plot_data[8])
#    geoHeuristic = geo_mean(plot_data[9])
#    retstr += str(geolitmus)
#    retstr += "\t"
#    retstr += str(geoChecker)
#    retstr += "\t"
#    retstr += str(geoHeuristic)
#    retstr += "\n"
#    f.write(retstr)
#    f.close()
#    retstr = ""
    # Speedup plots
    # if necessary switch sorting below
    #plot_data = returnSorted(perple_perf,9)
    f = open("speedup-10k.csv","w+")
    retstr += "\tlitmus7 user\tPerpLE (Checker)\tPerpLE (Heuristic)\tlitmus7 Timebase\tlitmus7 Userfence \tlitmus7 None \tlitmus7 Pthread\n"
    for i in range(0,len(plot_data[20])):
        retstr += plot_data[20][i]
        retstr += "\t"
        retstr += str(1.0)
        #retstr += str(plot_data[11][i]) # select 100000 + runtime
        retstr += "\t"
        checkerTime = 0.0
        if float(plot_data[8][i]) > 0.0:
            checkerTime = float(plot_data[13][i])/float(plot_data[8][i]) # Comparison against user sync
        retstr += str(checkerTime) 
        retstr += "\t"
        heuristicTime = 0.0
        if float(plot_data[9][i]) > 0.0:
            heuristicTime = float(plot_data[13][i])/float(plot_data[9][i]) # Comparison against user sync
        retstr += str(heuristicTime)
        retstr += "\t"
        timebaseTime = float(plot_data[13][i])/float(plot_data[11][i]) # Comparison against user sync
        retstr += str(timebaseTime)
        retstr += "\t"
        userfenceTime = float(plot_data[13][i])/float(plot_data[15][i]) # Comparison against user sync
        retstr += str(userfenceTime)
        retstr += "\t"
#        print("none ")
#        print(plot_data[17][i])
#        print(plot_data[15][i])
#        print(" pthread ")
#        print(plot_data[19][i])
        noneTime = 0.0
        if float(plot_data[17][i]) == 0.0:
            noneTime = float(plot_data[13][i])/float(0.002) # Comparison against user sync
        else:
            noneTime = float(plot_data[13][i])/float(plot_data[17][i]) # Comparison against user sync
        retstr += str(noneTime)
        retstr += "\t"
        pthreadTime = 0.0
        if float(plot_data[19][i]) > 0.0:
            pthreadTime = float(plot_data[13][i])/float(plot_data[19][i]) # Comparison against user sync
        retstr += str(pthreadTime)
        retstr += "\n"
    retstr += "Geomean\t"
    # fix these TODO
    geolitmusTimebase = geo_mean(plot_data[11])
    geolitmusUser = geo_mean(plot_data[13])
    geolitmusUserfence = geo_mean(plot_data[15])
    geolitmusNone = geo_mean(plot_data[17])
    if geolitmusNone == 0.0:
        geolitmusNone = 0.002
    geolitmusPthread = geo_mean(plot_data[19])
    geoChecker = geo_mean(plot_data[8])
    geoHeuristic = geo_mean(plot_data[9])
    retstr += str(1.0)
    retstr += "\t"
    retstr += str(float(geolitmusUser)/float(geoChecker))
    retstr += "\t"
    retstr += str(float(geolitmusUser)/float(geoHeuristic))
    retstr += "\t"
    retstr += str(float(geolitmusUser)/float(geolitmusTimebase))
    retstr += "\t"
    retstr += str(float(geolitmusUser)/float(geolitmusUserfence))
    retstr += "\t"
    retstr += str(float(geolitmusUser)/float(geolitmusNone))
    retstr += "\t"
    if geolitmusPthread == 0.0:
        retstr += str(0.0)
    else:
        retstr += str(float(geolitmusUser)/float(geolitmusPthread))
    retstr += "\n"
    f.write(retstr)
    f.close()
#    perple_perf = returnSummary(perple_data,2,1)
#    litmus_perf = returnSummary(litmus_data,2,2)
#    means_str = generate_means(perples,litmuses,testnames)
#    f = open("averages-scaling.csv","w+")
#    f.write(means_str)
#    f.close()
    accuracy = heuristic_accuracy(perples,litmuses,testnames)
    f = open("accuracy.csv","w+")
    f.write(accuracy)
    f.close()
    sing_outcomes = single_outcomes(plot_data,perple_data,litmus_data,testnames)
    f = open("single-outcomes.csv","w+")
    f.write(sing_outcomes)
    f.close()
    #rate1 = rates(perple_data,litmus_data,testnames)
    #f = open("rates.csv","w+")
    #f.write(rate1)
    #f.close()
    rate2 = georates(perples,litmuses,testnames)
    f = open("georates.csv","w+")
    f.write(rate2)
    f.close()


if __name__=="__main__":
    main()

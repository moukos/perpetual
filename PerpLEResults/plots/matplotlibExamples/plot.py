import argparse
from go import *
import numpy as np
import matplotlib.pyplot as plt
import os
import re

AXIS_FONTSIZE = 44
TICK_FONTSIZE = 40
INPUTS_FONTSIZE = 32

width = 0.80
ind = np.arange(1, 6)
llamas = {"bfs": "6", "sssp": "9", "pagerank": "11", "ewsd": "21", "graph_projections": "9"}
approach = "FAST-LLAMAs Pair"

def create_scaling_axis(ax1, ind, yticks, ylabel):
  num_apps = 3
  N = 9
  input_inds = []
  seps = []
  for i in ind:
    input_inds = input_inds + [i-4.5*width/N, i-3.25*width/N, i-2.25*width/N, i-width/N, i, i+1.25*width/N, i+2.25*width/N, i+3.5*width/N, i+4.5*width/N]
    if i == ind[len(ind)-1]:
      continue
    else:
      seps = seps + [i + 0.5]

  ax2 = ax1.twiny()
  ax3 = ax1.twiny()
  ax4 = ax1.twinx()

  input_labels = ['1 InO', '2 Par', '1 FLPs', '4 Par', '2 FLPs', '8 Par', '4 FLPs', '16 Par', '8 FLPs']
  input_labels = input_labels*3
  xticks = ('BFS', 'SSSP', 'PR')

  ax1.set_xlim([0.5, num_apps+0.5])
  ax1.set_xticks(input_inds)
  ax1.set_xticklabels(input_labels, rotation=270, fontsize=INPUTS_FONTSIZE)
  ax1.set_ylim([0, yticks[len(yticks)-1]])
  ax1.set_yticks(yticks)
  ax1.set_yticklabels(yticks, fontsize=TICK_FONTSIZE)
  ax1.set_ylabel(ylabel, fontsize=AXIS_FONTSIZE)
  ax1.tick_params(direction='inout', length=20, width=1)

  ax2.set_xlim([0.5, num_apps+0.5])
  ax2.xaxis.set_ticks_position("bottom")
  ax2.xaxis.set_label_position("bottom")
  ax2.spines["bottom"].set_position(("axes", -0.2))
  ax2.spines["bottom"].set_visible(False)
  ax2.set_xticks(ind)
  ax2.set_xticklabels(xticks, fontsize=AXIS_FONTSIZE)
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

def create_x_axis(ax1, ind, yticks, ylabel):
  num_apps = 5
  num_inputs = 3
  input_inds = []
  seps = []
  for i in ind:
    input_inds = input_inds + [i-width/num_inputs, i, i+width/num_inputs]
    if i == ind[len(ind)-1]:
      continue
    else:
      seps = seps + [i + 0.5]

  ax2 = ax1.twiny()
  ax3 = ax1.twiny()
  ax4 = ax1.twinx()

  input_labels = ['Kron', 'Uni', 'SW', 'Pow', 'Exp', 'Uni', 'Kron', 'Uni', 'SW', 'Kron', 'Uni', 'SW', 'Kron', 'Uni', 'SW']
  xticks = ('EWSD', 'GP', 'BFS', 'SSSP', 'PR')

  ax1.set_xlim([0.5, num_apps+0.5])
  ax1.set_xticks(input_inds)
  ax1.set_xticklabels(input_labels, fontsize=1.5*INPUTS_FONTSIZE)
  ax1.set_ylim([0, yticks[len(yticks)-1]])
  ax1.set_yticks(yticks)
  ax1.set_yticklabels(yticks, fontsize=1.5*TICK_FONTSIZE)
  ax1.set_ylabel(ylabel, fontsize=1.5*AXIS_FONTSIZE)
  ax1.tick_params(direction='inout', length=20, width=1)

  ax2.set_xlim([0.5, num_apps+0.5])
  ax2.xaxis.set_ticks_position("bottom")
  ax2.xaxis.set_label_position("bottom")
  ax2.spines["bottom"].set_position(("axes", -0.05))
  ax2.spines["bottom"].set_visible(False)
  ax2.set_xticks(ind)
  ax2.set_xticklabels(xticks, fontsize=1.5*AXIS_FONTSIZE)
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

def create_x_axis_avg(ax1, ind, yticks, ylabel):
  num_apps = 5
  num_inputs = 4
  input_inds = []
  seps = []
  for i in ind:
    input_inds = input_inds + [i-3*width/num_inputs/2, i-width/num_inputs/2, i+width/num_inputs/2, i+3*width/num_inputs/2]
    if i == ind[len(ind)-1]:
      continue
    else:
      seps = seps + [i + 0.5]

  ax2 = ax1.twiny()
  ax3 = ax1.twiny()
  ax4 = ax1.twinx()

  scale = 1.25
  input_labels = ['Kron', 'Uni', 'SW', 'GM', 'Pow', 'Exp', 'Uni', 'GM', 'Kron', 'Uni', 'SW', 'GM', 'Kron', 'Uni', 'SW', 'GM', 'Kron', 'Uni', 'SW', 'GM']
  xticks = ('EWSD', 'GP', 'BFS', 'SSSP', 'PR')

  ax1.set_xlim([0.5, num_apps+0.5])
  ax1.set_xticks(input_inds)
  ax1.set_xticklabels(input_labels, fontsize=scale*INPUTS_FONTSIZE)
  ax1.set_ylim([0, yticks[len(yticks)-1]])
  ax1.set_yticks(yticks)
  ax1.set_yticklabels(yticks, fontsize=scale*TICK_FONTSIZE)
  ax1.set_ylabel(ylabel, fontsize=scale*AXIS_FONTSIZE)
  ax1.tick_params(direction='inout', length=20, width=1)

  ax2.set_xlim([0.5, num_apps+0.5])
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

  ax4.set_yticks(yticks)
  ax4.set_ylim([0, yticks[len(yticks)-1]])
  ax4.set_yticklabels([])
  ax4.tick_params(direction='inout', length=20, width=1, labelleft=False, labelright=True)

def create_x_axis_avg_big(ax1, ind, yticks, ylabel, scale):
  num_apps = 5
  num_inputs = 4
  input_inds = []
  seps = []
  for i in ind:
    input_inds = input_inds + [i-3*width/num_inputs/2, i-width/num_inputs/2, i+width/num_inputs/2, i+3*width/num_inputs/2]
    if i == ind[len(ind)-1]:
      continue
    else:
      seps = seps + [i + 0.5]

  ax2 = ax1.twiny()
  ax3 = ax1.twiny()
  ax4 = ax1.twinx()

  input_labels = ['Kron', 'Uni', 'SW', 'GM', 'Pow', 'Exp', 'Uni', 'GM', 'Kron', 'Uni', 'SW', 'GM', 'Kron', 'Uni', 'SW', 'GM', 'Kron', 'Uni', 'SW', 'GM']
  xticks = ('EWSD', 'GP', 'BFS', 'SSSP', 'PR')

  ax1.set_xlim([0.5, num_apps+0.5])
  ax1.set_xticks(input_inds)
  ax1.set_xticklabels(input_labels, fontsize=scale*INPUTS_FONTSIZE)
  ax1.set_ylim([0, yticks[len(yticks)-1]])
  ax1.set_yticks(yticks)
  ax1.set_yticklabels(yticks, fontsize=scale*TICK_FONTSIZE)
  ax1.set_ylabel(ylabel, fontsize=scale*AXIS_FONTSIZE)
  ax1.tick_params(direction='inout', length=20, width=1)

  ax2.set_xlim([0.5, num_apps+0.5])
  ax2.xaxis.set_ticks_position("bottom")
  ax2.xaxis.set_label_position("bottom")
  ax2.spines["bottom"].set_position(("axes", -0.05))
  ax2.spines["bottom"].set_visible(False)
  ax2.set_xticks(ind)
  ax2.set_xticklabels(xticks, fontsize=scale*AXIS_FONTSIZE)
  ax2.tick_params(length=0)

  ax3.set_xlim([0.5, num_apps+0.5])
  ax3.xaxis.set_ticks_position("bottom")
  ax3.set_xticks(seps)
  ax3.set_xticklabels([])
  ax3.tick_params(direction='inout', length=40, width=1)

  ax4.set_yticks(yticks)
  ax4.set_ylim([0, yticks[len(yticks)-1]])
  ax4.set_yticklabels([])
  ax4.tick_params(direction='inout', length=20, width=1, labelleft=False, labelright=True)

def create_vp_axis(ax1, ind, yticks, ylabel):
  num_apps = 3
  num_inputs = 3
  ind = np.arange(1, 4)
  app_inds = []
  seps = []
  for i in ind:
    app_inds = app_inds + [i-width/num_apps, i, i+width/num_apps]
    if i == ind[len(ind)-1]:
      continue
    else:
      seps = seps + [i + 0.5]

  ax2 = ax1.twiny()
  ax3 = ax1.twiny()
  ax4 = ax1.twinx()

  scale = 1.75
  app_labels = ('BFS', 'SSSP', 'PR', 'BFS', 'SSSP', 'PR', 'BFS', 'SSSP', 'PR')
  xticks = ('Kron', 'Uni', 'SW')

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

#Total latency breakdown
def latency_breakdown(y1a, y1b, y2a, y2b, y3a, y3b, y4a, y4b, yticks):
  N = 4

  fig = plt.figure(figsize=(40.0, 18.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  y = [100.0, 100.0, 100.0, 100.0, 100.0]

  dark = 'black'
  medium = 'gray'
  light = 'gainsboro'
  scale = 0.9

  psb1 = ax1.bar(ind-3*width/N/2, y, scale*width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb1a = ax1.bar(ind-3*width/N/2, y1a, scale*width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb1b = ax1.bar(ind-3*width/N/2, y1b, scale*width/N, color=light, linewidth=1, edgecolor=['black'])
  psb2 = ax1.bar(ind-width/N/2, y, scale*width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb2a = ax1.bar(ind-width/N/2, y2a, scale*width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb2b = ax1.bar(ind-width/N/2, y2b, scale*width/N, color=light, linewidth=1, edgecolor=['black'])
  psb3 = ax1.bar(ind+width/N/2, y, scale*width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb3a = ax1.bar(ind+width/N/2, y3a, scale*width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb3b = ax1.bar(ind+width/N/2, y3b, scale*width/N, color=light, linewidth=1, edgecolor=['black'])
  psb4 = ax1.bar(ind+3*width/N/2, y, scale*width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb4a = ax1.bar(ind+3*width/N/2, y4a, scale*width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb4b = ax1.bar(ind+3*width/N/2, y4b, scale*width/N, color=light, hatch='.', linewidth=1, edgecolor=['black'])

  ylabel = 'Percentage of Total Runtime'
  create_x_axis_avg(ax1, ind, yticks, ylabel)

  legend = ('The LLAMA', 'Rest of Memory Accesses', 'Compute')
  chartBox = ax1.get_position()
  ax1.set_position([chartBox.x0, chartBox.y0, chartBox.width, chartBox.height*0.8])
  ax1.legend((psb1b[0], psb1a[0], psb1[0]), legend, bbox_to_anchor=(0.,1.01,1.,0.101), ncol=3, mode="expand", fontsize=1.5*INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/motivation_llama.pdf", bbox_inches='tight')

# Time spent going to main memory
def mm(y1, y2, y3, y4):
  N = 4

  fig = plt.figure(figsize=(40.0, 18.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  c = 'gainsboro'
  c_avg = 'black'
  scale = 0.9

  psb1 = ax1.bar(ind-3*width/N/2, y1, scale*width/N, color=c, linewidth=1, edgecolor=['black'])
  psb2 = ax1.bar(ind-width/N/2, y2, scale*width/N, color=c, linewidth=1, edgecolor=['black'])
  psb3 = ax1.bar(ind+width/N/2, y3, scale*width/N, color=c, linewidth=1, edgecolor=['black'])
  psb4 = ax1.bar(ind+3*width/N/2, y4, scale*width/N, color=c, hatch='.', linewidth=1, edgecolor=['black'])

  yticks  = np.round(np.arange(0, 1.1, 0.1),1)
  ylabel = 'LLC Miss Rate'
  create_x_axis_avg(ax1, ind, yticks, ylabel)

  legend = ('LLC Miss Rate', 'LLC Miss Rate (Avg)')
  chartBox = ax1.get_position()
  ax1.set_position([chartBox.x0, chartBox.y0, chartBox.width, chartBox.height*0.8])
  ax1.legend((psb1[0], psb4[0]), legend, bbox_to_anchor=(0.,1.01,1.,0.101), ncol=3, mode="expand", fontsize=1.5*INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/motivation_dram.pdf", bbox_inches='tight')

def simple(speedups, averages):
  N = 16

  s1a = speedups[0][4]
  s1b = speedups[0][10]
  s1c = speedups[0][6]
  s1d = speedups[0][8]
  s2a = speedups[1][4]
  s2b = speedups[1][10]
  s2c = speedups[1][6]
  s2d = speedups[1][8]
  s3a = speedups[2][4]
  s3b = speedups[2][10]
  s3c = speedups[2][6]
  s3d = speedups[2][8]
  s4a = averages[4]
  s4b = averages[10]
  s4c = averages[6]
  s4d = averages[8]

  fig = plt.figure(figsize=(60.0,15.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  dark = 'black'
  medium = 'darkgrey'
  lightmedium = 'gainsboro'
  light = 'white'
  
  sym = '.'
  psb1a = ax1.bar(ind-7.5*width/N, s1a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb1b = ax1.bar(ind-6.5*width/N, s1b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb1c = ax1.bar(ind-5.5*width/N, s1c, width/N, color=lightmedium, linewidth=1, edgecolor=['black'])
  psb1d = ax1.bar(ind-4.5*width/N, s1d, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb2a = ax1.bar(ind-3.5*width/N, s2a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb2b = ax1.bar(ind-2.5*width/N, s2b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb2c = ax1.bar(ind-1.5*width/N, s2c, width/N, color=lightmedium, linewidth=1, edgecolor=['black'])
  psb2d = ax1.bar(ind-0.5*width/N, s2d, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb3a = ax1.bar(ind+0.5*width/N, s3a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb3b = ax1.bar(ind+1.5*width/N, s3b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb3c = ax1.bar(ind+2.5*width/N, s3c, width/N, color=lightmedium, linewidth=1, edgecolor=['black'])
  psb3d = ax1.bar(ind+3.5*width/N, s3d, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb4a = ax1.bar(ind+4.5*width/N, s4a, width/N, color=dark, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4b = ax1.bar(ind+5.5*width/N, s4b, width/N, color=medium, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4c = ax1.bar(ind+6.5*width/N, s4c, width/N, color=lightmedium, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4d = ax1.bar(ind+7.5*width/N, s4d, width/N, color=light, hatch=sym, linewidth=1, edgecolor=['black'])
  dummy = ax1.plot([0], [0], color="w")

  yticks = np.arange(7)
  ylabel = 'Speedup'
  create_x_axis_avg(ax1, ind, yticks, ylabel)

  legend = ('1 In-Order Core', '', '2 Parallel', '2 Parallel (GeoMean)', '1 DeSC Pair', '1 DeSC Pair (GeoMean)', '1 ' + approach, '1 ' + approach + ' (GeoMean)')
  chartBox = ax1.get_position()
  ax1.set_position([chartBox.x0, chartBox.y0, chartBox.width, chartBox.height*0.8])
  #ax1.legend((psb1a[0], dummy[0], psb1b[0], psb4b[0], psb1c[0], psb4c[0], psb1d[0], psb4d[0]), legend, bbox_to_anchor=(0.,1.015,1.,0.15), ncol=4, mode="expand", fontsize=INPUTS_FONTSIZE)
  plt.legend((psb1a[0], dummy[0], psb1b[0], psb4b[0], psb1c[0], psb4c[0], psb1d[0], psb4d[0]), legend, ncol=4, fontsize=INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/simple.pdf", bbox_inches='tight')

def perfect_cache(speedups):
  N = 9
  ind = np.arange(1, 4)

  s1a = speedups[0][0]
  s1b = speedups[0][8]
  s1c = speedups[0][1]
  s2a = speedups[1][0]
  s2b = speedups[1][8]
  s2c = speedups[1][1]
  s3a = speedups[2][0]
  s3b = speedups[2][8]
  s3c = speedups[2][1]

  fig = plt.figure(figsize=(32.0,24.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  dark = 'black'
  medium = 'grey'
  light = 'white'
  
  psb1a = ax1.bar(ind-4*width/N, s1a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb1b = ax1.bar(ind-3*width/N, s1b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb1c = ax1.bar(ind-2*width/N, s1c, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb2a = ax1.bar(ind-width/N, s2a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb2b = ax1.bar(ind, s2b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb2c = ax1.bar(ind+width/N, s2c, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb3a = ax1.bar(ind+2*width/N, s3a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb3b = ax1.bar(ind+3*width/N, s3b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb3c = ax1.bar(ind+4*width/N, s3c, width/N, color=light, linewidth=1, edgecolor=['black'])

  yticks = np.arange(11)
  ylabel = 'Speedup'
  create_vp_axis(ax1, ind, yticks, ylabel)

  legend = ('1 In-Order Core', '1 ' + approach, '1 In-Order Core w/ Perfect Cache')
  plt.legend((psb1a[0], psb1b[0], psb1c[0]), legend, loc=2, fontsize=1.5*INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/perfect_cache.pdf", bbox_inches='tight')

def receive_latency(stats):
  N = 6
  ind = np.arange(1, 4)

  s1a = stats[0][0]
  s1b = stats[0][2]
  s2a = stats[1][0]
  s2b = stats[1][2]
  s3a = stats[2][0]
  s3b = stats[2][2]

  print(s1b, s2b, s3b)

  fig = plt.figure(figsize=(32.0,24.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  dark = 'black'
  medium = 'gainsboro'
  
  psb1a = ax1.bar(ind-2.5*width/N, s1a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb1b = ax1.bar(ind-1.5*width/N, s1b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb2a = ax1.bar(ind-0.5*width/N, s2a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb2b = ax1.bar(ind+0.5*width/N, s2b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb3a = ax1.bar(ind+1.5*width/N, s3a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb3b = ax1.bar(ind+2.5*width/N, s3b, width/N, color=medium, linewidth=1, edgecolor=['black'])

  yticks = np.arange(10)
  ylabel = 'Speedup'
  create_vp_axis(ax1, ind, yticks, ylabel)

  legend = ('1 In-Order Core', '1 ' + approach)
  plt.legend((psb1a[0], psb1b[0]), legend, fontsize=1.5*INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/receive_latency.pdf", bbox_inches='tight')

def mlp(stats):
  N = 9
  ind = np.arange(1, 4)

  s1a = stats[0][1]
  s1b = stats[0][4]
  s1c = stats[0][3]
  s2a = stats[1][1]
  s2b = stats[1][4]
  s2c = stats[1][3]
  s3a = stats[2][1]
  s3b = stats[2][4]
  s3c = stats[2][3]

  fig = plt.figure(figsize=(32.0,24.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  dark = 'black'
  medium = 'darkgrey'
  light = 'white'
  
  psb1a = ax1.bar(ind-4*width/N, s1a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb1b = ax1.bar(ind-3*width/N, s1b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb1c = ax1.bar(ind-2*width/N, s1c, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb2a = ax1.bar(ind-width/N, s2a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb2b = ax1.bar(ind, s2b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb2c = ax1.bar(ind+width/N, s2c, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb3a = ax1.bar(ind+2*width/N, s3a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb3b = ax1.bar(ind+3*width/N, s3b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb3c = ax1.bar(ind+4*width/N, s3c, width/N, color=light, linewidth=1, edgecolor=['black'])

  yticks = np.arange(12)
  ylabel = 'Number of DRAM Accesses' #'Improvement'
  create_vp_axis(ax1, ind, yticks, ylabel)

  legend = ('1 In-Order Core', '2 Parallel', '1 ' + approach)
  plt.legend((psb1a[0], psb1b[0], psb1c[0]), legend, loc=2, fontsize=1.5*INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/mlp.pdf", bbox_inches='tight')

def eight_one(speedups, averages):
  N = 31

  s1a = speedups[0][4]
  s1b = speedups[0][5]
  s1c = speedups[0][12]
  s1d = speedups[0][16]
  s2a = speedups[1][4]
  s2b = speedups[1][5]
  s2c = speedups[1][12]
  s2d = speedups[1][16]
  s3a = speedups[2][4]
  s3b = speedups[2][5]
  s3c = speedups[2][12]
  s3d = speedups[2][16]
  s4a = averages[4]
  s4b = averages[5]
  s4c = averages[12]
  s4d = averages[16]

  for i in range(len(s3d)):
    print(s1d[i]/s1b[i])
    print(s2d[i]/s2b[i])
    print(s3d[i]/s3b[i])

  fig = plt.figure(figsize=(60.0,15.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  dark = 'black'
  darkmedium = 'darkgrey'
  medium = 'gainsboro'
  light = 'white'

  sym = '.'  
  psb1a = ax1.bar(ind-15*width/N, s1a, 2*width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb1b = ax1.bar(ind-13*width/N, s1b, 2*width/N, color=darkmedium, linewidth=1, edgecolor=['black'])
  psb1c = ax1.bar(ind-11*width/N, s1c, 2*width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb1d = ax1.bar(ind-9*width/N, s1d, 2*width/N, color=light, linewidth=1, edgecolor=['black'])
  psb2a = ax1.bar(ind-7*width/N, s2a, 2*width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb2b = ax1.bar(ind-5*width/N, s2b, 2*width/N, color=darkmedium, linewidth=1, edgecolor=['black'])
  psb2c = ax1.bar(ind-3*width/N, s2c, 2*width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb2d = ax1.bar(ind-width/N, s2d, 2*width/N, color=light, linewidth=1, edgecolor=['black'])
  psb3a = ax1.bar(ind+width/N, s3a, 2*width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb3b = ax1.bar(ind+3*width/N, s3b, 2*width/N, color=darkmedium, linewidth=1, edgecolor=['black'])
  psb3c = ax1.bar(ind+5*width/N, s3c, 2*width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb3d = ax1.bar(ind+7*width/N, s3d, 2*width/N, color=light, linewidth=1, edgecolor=['black'])
  psb4a = ax1.bar(ind+9*width/N, s4a, 2*width/N, color=dark, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4b = ax1.bar(ind+11*width/N, s4b, 2*width/N, color=darkmedium, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4c = ax1.bar(ind+13*width/N, s4c, 2*width/N, color=medium, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4d = ax1.bar(ind+15*width/N, s4d, 2*width/N, color=light, hatch=sym, linewidth=1, edgecolor=['black'])
  dummy = ax1.plot([0], [0], color="w")

  yticks = np.arange(0, 21, 2)
  ylabel = 'Speedup'
  create_x_axis_avg(ax1, ind, yticks, ylabel)

  legend = ('1 In-Order Core', '', '1 Out-of-Order Core', '1 Out-of-Order Core (GeoMean)', '8 Parallel In-Order Cores', '8 Parallel In-Order Cores (GeoMean)', '4 In-Order ' + approach + 's', '4 In-Order ' + approach + 's (GeoMean)')
  chartBox = ax1.get_position()
  ax1.set_position([chartBox.x0, chartBox.y0, chartBox.width, chartBox.height*0.8])
  ax1.legend((psb1a[0], dummy[0], psb1b[0], psb4b[0], psb1c[0], psb4c[0], psb1d[0], psb4d[0]), legend, bbox_to_anchor=(0.,1.018,1.,0.18), ncol=4, mode="expand", fontsize=INPUTS_FONTSIZE)
  #plt.legend((psb1a[0], psb1b[0], psb1c[0], psb1d[0]), legend, fontsize=INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/eight_one.pdf", bbox_inches='tight')

def scaling(speedups, averages):
  N = 9
  ind = np.arange(1, 4)

  s1 = speedups[0][4][2:5]
  s2 = speedups[0][10][2:5]
  s3 = speedups[0][8][2:5]
  s4 = speedups[0][11][2:5]
  s5 = speedups[0][15][2:5]
  s6 = speedups[0][12][2:5]
  s7 = speedups[0][16][2:5]
  s8 = speedups[0][13][2:5]
  s9 = speedups[0][17][2:5]

  print("scaling")
  print(s8)

  fig = plt.figure(figsize=(30.0,15.0))
  fig.subplots_adjust(bottom=0.25)
  ax1 = fig.add_subplot(111)

  c1 = 'black'
  c2 = 'dimgrey'
  c3 = 'darkgrey'
  c4 = 'gainsboro'
  c5 = 'white'
 
  sym = '/'
  psb1 = ax1.bar(ind-4.5*width/N, s1, width/N, color=c1, linewidth=1, edgecolor=['black'])
  psb2 = ax1.bar(ind-3.25*width/N, s2, width/N, color=c2, linewidth=1, edgecolor=['black'])
  psb3 = ax1.bar(ind-2.25*width/N, s3, width/N, color=c2, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4 = ax1.bar(ind-width/N, s4, width/N, color=c3, linewidth=1, edgecolor=['black'])
  psb5 = ax1.bar(ind, s5, width/N, color=c3, hatch=sym, linewidth=1, edgecolor=['black'])
  psb6 = ax1.bar(ind+1.25*width/N, s6, width/N, color=c4, linewidth=1, edgecolor=['black'])
  psb7 = ax1.bar(ind+2.25*width/N, s7, width/N, color=c4, hatch=sym, linewidth=1, edgecolor=['black'])
  psb8 = ax1.bar(ind+3.5*width/N, s8, width/N, color=c5, linewidth=1, edgecolor=['black'])
  psb9 = ax1.bar(ind+4.5*width/N, s9, width/N, color=c5, hatch=sym, linewidth=1, edgecolor=['black'])
  dummy = ax1.plot([0], [0], color="w")

  yticks = np.arange(0, 33, 4)
  ylabel = 'Speedup'
  create_scaling_axis(ax1, ind, yticks, ylabel)

  legend = ['InO = In-Order Core', 'Par = Parallel', 'FLP = FAST-LLAMAs Pair']
  for l in legend:
    ax1.plot(1, 1, label = l, marker = '', ls ='')
  ax1.legend(loc=2, handlelength=0, fontsize=INPUTS_FONTSIZE)
  #legend = ('1 In-Order Core', '', '2 Parallel', '1 ' + approach, '4 Parallel', '2 ' + approach + 's', '8 Parallel', '4 ' + approach + 's', '16 Parallel', '8 ' + approach + 's')
  #chartBox = ax1.get_position()
  #ax1.set_position([chartBox.x0, chartBox.y0, chartBox.width, chartBox.height*0.8])
  #ax1.legend((psb1[0], dummy[0], psb2[0], psb3[0], psb4[0], psb5[0], psb6[0], psb7[0], psb8[0], psb9[0]), legend, bbox_to_anchor=(0.,1.018,1.,0.18), ncol=5, mode="expand", fontsize=1.05*INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/scaling.pdf", bbox_inches='tight')

def parse_mem():
  exp_dir = "/home/ts20/share/results/test1/"
  metrics = ["Percent of Total Latency Spent on Memory", "Percent of Total Latency Spent on Long-Latency Access", "Long-Latency Access L2 Hit Rate"]
  ys = [[[],[],[]], [[],[],[]], [[],[],[]]]

  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      filename = exp_dir + app + "_" + input.split(".")[0] + "_IO/measurements.txt"
      if os.path.isfile(filename):
        measurements = open(filename)
        data = measurements.read()
        measurements.close()
        for m in range(len(metrics)):
          matches = re.findall("^" + metrics[m] + ": .*$", data, re.MULTILINE)
          match = re.match(".+:\s*(\d+\.*\d+)", matches[0])
          if m == 2:
            percent = (1-float(match.group(1)))
          else:
            percent = float(match.group(1))
          ys[i][m].append(percent)
      else:
        for m in range(len(metrics)):
          ys[i][m].append(0)

  y1a = ys[0][0]
  y1b = ys[0][1]
  y1 = ys[0][2]
  y2a = ys[1][0]
  y2b = ys[1][1]
  y2 = ys[1][2]
  y3a = ys[2][0]
  y3b = ys[2][1]
  y3 = ys[2][2]
  yticks  = np.arange(0, 101, 10)

  y4a = []
  y4b = []
  y4 = []
  for i in range(len(y1)):
    y4a.append((y1a[i] + y2a[i] + y3a[i])/3)
    y4b.append((y1b[i] + y2b[i] + y3b[i])/3)
    y4.append((y1[i] + y2[i] + y3[i])/3)

  latency_breakdown(y1a, y1b, y2a, y2b, y3a, y3b, y4a, y4b, yticks)
  mm(y1, y2, y3, y4)
  #latency_breakdown_mm(y1a, y1b, y2a, y2b, y3a, y3b, y1, y2, y3, yticks)

def parse_speedups():
  # 1 IO, 1 IO PC, 1 OOO, 1 OOO PC (test1)
  # 1 IO, 1 OOO, 1 decoupled, 1 OOO decoupled (test2) 
  # 1 IO terminal RMW, 1 OOO terminal RMW (test3)
  # 2 IO, 4 IO, 8 IO, 16 IO, 1 decoupled, 2 decoupled, 4 decoupled, 8 decoupled (test4)

  runtimes = [[], [], []]
  speedups = [[], [], []]
  averages = []

  exp_dir = "/home/ts20/share/results/test1/"
  new_configs = ["", "_PC"]
  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      for c in range(len(configs)):
        config = configs[c]
        for n in range(len(new_configs)):
          new_config = new_configs[n]
          filename = exp_dir + app + "_" + input.split(".")[0] + "_" + config + new_config + "/measurements.txt"
          index = c*2 + n
          if len(runtimes[i]) <= index:
            runtimes[i].append([])
          if os.path.isfile(filename):
            measurements = open(filename)
            data = measurements.read()
            measurements.close()
            matches = re.findall("^cycles : .*$", data, re.MULTILINE)
            match = re.match(".+:\s*(\d+\.*\d+)", matches[0])
            runtime = float(match.group(1))
            runtimes[i][index].append(runtime)
          else:
            fill = runtimes[i][0][len(runtimes[i][index])]
            runtimes[i][index].append(fill)
 
  exp_dir = "/home/ts20/share/results/test2/"
  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      for m in range(len(modes)):
        mode = modes[m]
        for c in range(len(configs)):
          config = configs[c]
          filename = exp_dir + app + "_" + input.split(".")[0] + "_" + config + "_" + mode + "/measurements.txt"
          index = m*2 + c + 4
          if len(runtimes[i]) <= index:
            runtimes[i].append([])
          if os.path.isfile(filename):
            measurements = open(filename)
            data = measurements.read()
            measurements.close()
            matches = re.findall("^cycles : .*$", data, re.MULTILINE)
            match = re.match(".+:\s*(\d+\.*\d+)", matches[0])
            runtime = float(match.group(1))
            runtimes[i][index].append(runtime)
          else:
            fill = runtimes[i][0][len(runtimes[i][index])]
            runtimes[i][index].append(fill)
 
  exp_dir = "/home/ts20/share/results/test3/"
  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      for c in range(len(configs)):
        config = configs[c]
        filename = exp_dir + app + "_" + input.split(".")[0] + "_" + config + "_di/measurements.txt"
        index = c + 8
        if len(runtimes[i]) <= index:
          runtimes[i].append([])
        if os.path.isfile(filename):
          measurements = open(filename)
          data = measurements.read()
          measurements.close()
          matches = re.findall("^cycles : .*$", data, re.MULTILINE)
          match = re.match(".+:\s*(\d+\.*\d+)", matches[0])
          runtime = float(match.group(1))
          runtimes[i][index].append(runtime)
        else:
          fill = runtimes[i][0][len(runtimes[i][index])]
          runtimes[i][index].append(fill)
 
  exp_dir = "/home/ts20/share/results/test4/"
  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      for m in range(len(modes)):
        mode = modes[m]
        for t in range(4):
          if mode == "db":
            num_tiles = str(int(math.pow(2, t+1)))
          else:
            num_tiles = str(int(math.pow(2, t)))
          index = m*4 + t + 10
          filename = exp_dir + app + "_" + input.split(".")[0] + "_IO_" + mode + "_" + num_tiles + "/measurements.txt"
          if len(runtimes[i]) <= index:
            runtimes[i].append([])
          if os.path.isfile(filename):
            measurements = open(filename)
            data = measurements.read()
            measurements.close()
            matches = re.findall("^cycles : .*$", data, re.MULTILINE)
            match = re.match(".+:\s*(\d+\.*\d+)", matches[0])
            runtime = float(match.group(1))
            runtimes[i][index].append(runtime)
          else:
            fill = runtimes[i][0][len(runtimes[i][index])]
            runtimes[i][index].append(fill)
          
  for i in range(len(runtimes)): #inputs
    for c in range(4): #configs
      if len(speedups[i]) <= c:
        speedups[i].append([])
      for a in range(len(runtimes[i][c])): #apps
        speedups[i][c].append(runtimes[i][0][a]/runtimes[i][c][a])
    for c in range(4, len(runtimes[i])): #configs
      if len(speedups[i]) <= c:
        speedups[i].append([])
      for a in range(len(runtimes[i][c])): #apps
        speedups[i][c].append(runtimes[i][4][a]/runtimes[i][c][a])

  for c in range(len(runtimes[0])): #configs
    averages.append([])
    for a in range(len(runtimes[0][c])): #apps
      if len(averages[c]) <= a:
        averages[c].append(1.0)
      for i in range(len(runtimes)): #inputs
        averages[c][a] = averages[c][a] * speedups[i][c][a]
      averages[c][a] = averages[c][a] ** (1./len(runtimes))

  flipped = [[],[],[]]
  for a in range(2, len(speedups[0][0])):
    for c in range(len(speedups[0])):
      for i in range(len(speedups)):
        if (len(flipped[a-2]) <= c):
          flipped[a-2].append([])
        flipped[a-2][c].append(speedups[i][c][a])

  simple(speedups, averages)
  perfect_cache(flipped)
  eight_one(speedups, averages)
  scaling(speedups, averages)

def parse_decoupling_output():
  metrics = ["loads", "terminal loads", "loads removed", "compute exclusive loads"]
  exp_dirs = ["/home/ts20/share/results/test2/", "/home/ts20/share/results/test4/"]
  percentages = [[[],[]],[[],[]],[[],[]]]
  
  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      for e in range(len(exp_dirs)):
        exp_dir = exp_dirs[e]
        if e == 0:
          filename = exp_dir + app + "_" + input.split(".")[0] + "_IO_di/app_output.txt"
        else:
          filename = exp_dir + app + "_" + input.split(".")[0] + "_IO_di_1/app_output.txt"
        if os.path.isfile(filename):
          measurements = open(filename)
          data = measurements.read()
          measurements.close()
          for m in range(len(metrics)):
            matches = re.findall("^.*% " + metrics[m] + "$", data, re.MULTILINE)
            if matches == []:
              percentage = 0
            else:
              match = re.match("(\d+\.*\d+)% " + metrics[m], matches[0])
              percentage = float(match.group(1))
            if (len(percentages[i][e]) <= m):
              percentages[i][e].append([])
            percentages[i][e][m].append(percentage)
          matches = re.findall("^total loads in program: .*$", data, re.MULTILINE)
          match = re.match("^total loads in program: (.*)$", matches[0])
          total = int(match.group(1))
          matches = re.findall("^" + llamas[app] + ": \d+.*$", data, re.MULTILINE)
          if matches == []:
            llama = 0
          else:
            match = re.match("^" + llamas[app] + ": (\d+)$", matches[0])
            llama = float(match.group(1))
          percentage = llama*100/total
          m = len(metrics)
          if (len(percentages[i][e]) <= m):
            percentages[i][e].append([])
          percentages[i][e][m].append(percentage)
        else:
          for m in range(len(metrics)+1):
            if (len(percentages[i][e]) <= m):
              percentages[i][e].append([])
            percentages[i][e][m].append(0)
  
  '''
  for i in range(len(percentages)):
    for t in range(len(percentages[i])):
      for m in range(len(percentages[i][t])):
        if t == 0:
          print(i, t, m, percentages[i][t][m])
  '''

  load_percentages_before(percentages)
  load_percentages_after(percentages)

def parse_mlp():
  metrics = [["Avg Mem Access Latency", "Mean # DRAM Accesses Per 1024-cycle Epoch"], ["Avg Recv Latency", "Mean # DRAM Accesses Per 1024-cycle Epoch"], ["Mean # DRAM Accesses Per 1024-cycle Epoch"]]
  exp_dirs = ["/home/ts20/share/results/test2/", "/home/ts20/share/results/test3/", "/home/ts20/share/results/test4/"]
  stats = [[], [], []]
  ratios = [[], [], []]
  averages = []
  # 1 IO Recv Wait Time, 1 IO MLP, 1 Decoupled Recv Wait Time, 1 Decouple MLP, 2 Parallel MLP

  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      for e in range(len(exp_dirs)):
        exp_dir = exp_dirs[e]
        if e == 0:
          filename = exp_dir + app + "_" + input.split(".")[0] + "_IO_db/measurements.txt"
        elif e == 1:
          filename = exp_dir + app + "_" + input.split(".")[0] + "_IO_di/measurements.txt"
        else:
          filename = exp_dir + app + "_" + input.split(".")[0] + "_IO_db_2/measurements.txt"
        if os.path.isfile(filename):
          measurements = open(filename)
          data = measurements.read()
          measurements.close()
          for m in range(len(metrics[e])):
            index = e*2 + m
            matches = re.findall(metrics[e][m] + ".*$", data, re.MULTILINE)
            match = re.match(metrics[e][m] + ".*\s*:\s*(.*\d+)", matches[0])
            stat = int(match.group(1))
            if (len(stats[i]) <= index):
              stats[i].append([])
            stats[i][index].append(stat)

  for i in range(len(stats)): #inputs
    for c in range(len(stats[i])): #configs
      if len(ratios[i]) <= c:
        ratios[i].append([])
      for a in range(len(stats[i][c])): #apps
        if c == 0 or c == 2:
          ratios[i][c].append(stats[i][0][a]/stats[i][c][a])
        else:
          ratios[i][c].append(stats[i][c][a]/stats[i][1][a])
  
  for i in range(len(stats)):
    for c in range(3,4):
      print(ratios[i][c])
    print()

  for c in range(len(stats[0])): #configs
    averages.append([])
    for a in range(len(stats[0][c])): #apps
      if len(averages[c]) <= a:
        averages[c].append(1.0)
      for i in range(len(stats)): #inputs
        averages[c][a] = averages[c][a] * ratios[i][c][a]
      averages[c][a] = averages[c][a] ** (1./len(stats))

  flipped_stats = [[],[],[]]
  flipped_ratios = [[],[],[]]
  for a in range(2, len(stats[0][0])):
    for c in range(len(stats[0])):
      for i in range(len(stats)):
        if (len(flipped_stats[a-2]) <= c):
          flipped_stats[a-2].append([])
          flipped_ratios[a-2].append([])
        flipped_stats[a-2][c].append(stats[i][c][a])
        flipped_ratios[a-2][c].append(ratios[i][c][a])

  receive_latency(flipped_ratios)
  mlp(flipped_stats)

def runahead():
  exp_dir = "/home/ts20/share/results/test3/"
  runahead_vals = [[]]*9

  fig = plt.figure(figsize=(40.0,22.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)
  ax2 = ax1.twiny()
  ax3 = ax1.twiny()
  ax4 = ax1.twinx()

  num_apps = 3
  num_inputs = 3
  ind = np.arange(1,4)
  app_inds = []
  seps = []
  for i in ind:
    app_inds = app_inds + [i-width/num_apps, i, i+width/num_apps]
    if i == ind[len(ind)-1]:
      continue
    else:
      seps = seps + [i + 0.5]

  for a in range(len(vp)):
    app = vp[a]
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      filename = exp_dir + app + "_" + input.split(".")[0] + "_IO_di/runahead_dists"
      if os.path.isfile(filename):
        with open(filename) as measurements:
          int_vals = [int(x) for x in measurements]
        runahead_vals[i*3 + a] = int_vals
        print(i)

  scale = 1.5
  app_labels = ('BFS', 'SSSP', 'PR', 'BFS', 'SSSP', 'PR', 'BFS', 'SSSP', 'PR')
  xticks = ('Kron', 'Uni', 'SW')
  
  yticks1 = np.arange(0, 7001, 500)
  yticks2 = np.arange(-900, 401, 100)
  ylabel = 'Runahead Distance'
  
  ax1.set_xlim([0.5, num_inputs+0.5])
  ax1.set_xticks(app_inds)
  ax1.set_xticklabels(app_labels, fontsize=scale*INPUTS_FONTSIZE)
  ax1.set_ylim([0, yticks1[len(yticks1)-1]])
  ax1.set_yticks(yticks1)
  ax1.set_yticklabels(yticks1, fontsize=scale*TICK_FONTSIZE)
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

  ax4.set_xticklabels([])
  ax4.set_ylim([0, yticks2[len(yticks2)-1]])
  ax4.set_yticks(yticks2)
  ax4.set_yticklabels(yticks2, fontsize=scale*TICK_FONTSIZE)
  ax4.set_ylabel(ylabel, fontsize=scale*AXIS_FONTSIZE)
  ax4.tick_params(direction='inout', length=20, width=1, labelleft=False, labelright=True)

  bp1 = ax1.boxplot(runahead_vals[0:3], widths=0.15, labels=app_labels[0:3], positions=app_inds[0:3], showfliers=False)
  bp2 = ax4.boxplot(runahead_vals[3:], widths=0.15, labels=app_labels[3:], positions=app_inds[3:], showfliers=False)

  for box in (bp1['boxes'] + bp2['boxes']):
    box.set(linewidth=5) # change box outline width
  for whisker in (bp1['whiskers'] + bp2['whiskers']):
    whisker.set(linewidth=3) # change whisker line width
  for median in (bp1['medians'] + bp2['medians']):
    median.set(color='dimgrey', linewidth=5) # change median line color and width

  ax1.hlines(y=200, xmin=0.0, xmax=1.5, color='black', linewidth=4, linestyle='--')
  ax4.hlines(y=200, xmin=1.5, xmax=3.5, color='black', linewidth=4, linestyle='--')
  plt.axvline(x=1.5, color='black', linewidth=7, linestyle='--')
  #plt.show()
  plt.savefig("../results/runahead.pdf", bbox_inches='tight')

import argparse
from characterize import *
import numpy as np
import matplotlib.pyplot as plt
import os
import re

AXIS_FONTSIZE = 44
TICK_FONTSIZE = 40
INPUTS_FONTSIZE = 32

width = 0.80
ind = np.arange(1,4)

MAX = 3000
hit_rate_data = [[], [], []] # first, second, total
num_accesses = 0
num_accesses1 = 0
num_accesses2 = 0

llama_cache_size = CACHE_SIZE
factors = factorize(llama_cache_size, 4)

def create_apps_axis(ax1, ind, yticks, ylabel):
  num_apps = 3
  ind = np.arange(1, 4)

  ax2 = ax1.twinx()

  scale = 1.5
  app_labels = ('BFS', 'SSSP', 'PR')

  ax1.set_xlim([0.5, num_apps+0.5])
  ax1.set_xticks(ind)
  ax1.set_xticklabels(app_labels, fontsize=scale*AXIS_FONTSIZE)
  ax1.set_ylim([0, yticks[len(yticks)-1]])
  ax1.set_yticks(yticks)
  ax1.set_yticklabels(yticks, fontsize=scale*TICK_FONTSIZE)
  ax1.set_ylabel(ylabel, fontsize=scale*AXIS_FONTSIZE)
  ax1.tick_params(direction='inout', length=20, width=1)

  ax2.set_ylim([0, yticks[len(yticks)-1]])
  ax2.set_yticks(yticks)
  ax2.set_yticklabels([])
  ax2.tick_params(direction='inout', length=20, width=1, labelleft=False, labelright=True)

def parse_reaccess(app_arr, cacheline_size, readdir, appdir):
  global hit_rate_data, num_accesses, num_accesses1, num_accesses2

  exp_dirs = [readdir]
  for app in app_arr:
    for exp_dir in exp_dirs:
      input = inputs[app]
      filename = exp_dir + app + "_" + input.split(".")[0] + "_" + str(cacheline_size) + "b/graph_node_reaccesses.txt"
      neibfilename = "/home/ts20/share/graphs/vp/Neighbors_" + input
      if os.path.isfile(filename):
        print("READING " + str(cacheline_size) + "B")
        with open(filename) as measurements:
          measurements.readline()
          vals = measurements.read().split()
          measurements.close()
        if len(vals) > 0:
          with open(neibfilename) as neib_measurements:
            neibs = neib_measurements.read().split()
            neib_measurements.close()
          degs = [int(neibs[n+1]) for n in range(0, len(neibs), 2)]

          num_cols = 10
          access = sorted([int(vals[i+1]) for i in range(0, len(vals), num_cols)], reverse=True)
          num_accesses = sum(access)
          
          # 0: node ID
          # 1: num misses
          # 2: num accesses
          # 3: degree
          # 4: num evictions 
          # 5: num reaccesses
          # 6: reuse distance 
          # 7: unused space
          info = [(int(vals[i]), int(vals[i+2]), int(vals[i+1]), degs[int(vals[i])], int(vals[i+3]), int(vals[i+4]), float(vals[i+5]), int(vals[i+9])) for i in range(0, len(vals), num_cols)] 
          info = sorted(info, key=lambda x: x[3], reverse=True)
          num_nodes = len(info)
          #MAX = num_nodes
          #print("NODES: " + str(num_nodes))

          x = np.arange(num_nodes)[0:MAX]
          y1 = [i[2] for i in info]
          y2 = [i[2]-i[1] for i in info]
          hit_rate = [(float(i[2]-i[1])/i[2]) for i in info]
          reaccess = [i[5] for i in info]
          reuse = [i[6] for i in info]
          unused = [i[7] for i in info]

          # ----- RECORD # NODES PER ACCESS  -----
          if cacheline_size == 4:
            access_counts = open(appdir + input.split("_")[0] + "_access_counts.txt", "w+")
            curr = access[0]
            count = 1
            count1 = 0
            for i in range(num_nodes):
              if access[i] != curr:
                access_counts.write(str(i) + "\t" + str(curr) + "\t" + str(count) + "\n")
                curr = access[i]
                count = 1
                if access[i] == 1:
                  count1 = 1
              else:
                count = count + 1
                if access[i] <= 1:
                  count1 = count1 + 1
            access_counts.write(str(i) + "\t" + str(curr) + "\t" + str(count) + "\n\n")
            access_counts.write("% of accessed nodes with only one access = " + str(count1*100.0/num_nodes) + "\n") 
            access_counts.close()

          hit50 = 0
          hit90 = 0
          cum_hit_rate1 = 0
          cum_hit_rate2 = 0
          cum_hit_rate = 0
          num_accesses1 = 0
          num_accesses2 = 0
          for i in range(num_nodes):
            # hit rate
            if hit_rate[i] >= 0.9:
              hit90 = hit90 + 1
            elif hit_rate[i] < 0.5:
              hit50 = hit50 + 1
            if i < MAX:
              cum_hit_rate1 = cum_hit_rate1 + access[i]*hit_rate[i]
              num_accesses1 = num_accesses1 + access[i]
            else:
              cum_hit_rate2 = cum_hit_rate2 + access[i]*hit_rate[i]
              num_accesses2 = num_accesses2 + access[i]
            cum_hit_rate = cum_hit_rate + access[i]*hit_rate[i]
          #print(str(cacheline_size) + "B: " + str(cum_hit_rate1) + ", " + str(cum_hit_rate2) + ", " + str(cum_hit_rate))
          #print(str(cacheline_size) + "B: " + str(num_accesses1) + ", " + str(num_accesses2) + ", " + str(num_accesses))
          hit_rate_data[0].append(cum_hit_rate1)
          hit_rate_data[1].append(cum_hit_rate2)
          hit_rate_data[2].append(cum_hit_rate)

          # ----- METRICS -----
          metrics = open(appdir + input.split("_")[0] + "_" + str(cacheline_size) + "b_metrics.txt", "w+")
          metrics.write("% of accessed nodes with at least 90% hit rate = " + str(hit90*100.0/num_nodes) + "\n")
          metrics.write("% of accessed nodes with less than 50% hit rate = " + str(hit50*100.0/num_nodes) + "\n")
          metrics.close()

          # ----- PLOTS -----
          fig = plt.figure(figsize=(20.0,10.0))
          ax1 = fig.add_subplot(111)
          ax1.plot(x, y1[0:MAX], label='Total Number of Accesses')
          ax1.plot(x, y2[0:MAX], label='Number of Accesses That Hit')
          ax1.set_xlabel("Node Degree")
          ax1.set_ylabel("Number of Accesses")
          plt.legend(loc=1)
          #plt.show()
          plt.savefig(appdir + input.split("_")[0] + "_" + str(cacheline_size) + "b_access_counts.pdf", bbox_inches='tight')

          fig = plt.figure(figsize=(20.0,10.0))
          ax1 = fig.add_subplot(111)
          ax1.plot(x, hit_rate[0:MAX])
          ax1.set_xlabel("Node Degree")
          ax1.set_ylabel("Hit Rate")
          #plt.show()
          plt.savefig(appdir + input.split("_")[0] + "_" + str(cacheline_size) + "b_access_hitrate.pdf", bbox_inches='tight')

          fig = plt.figure(figsize=(20.0,10.0))
          ax1 = fig.add_subplot(111)
          ax1.plot(x, reaccess[0:MAX])
          ax1.set_xlabel("Node Degree")
          ax1.set_ylabel("# Reaccesses")
          #plt.show()
          plt.savefig(appdir + input.split("_")[0] + "_" + str(cacheline_size) + "b_reaccess.pdf", bbox_inches='tight')

          fig = plt.figure(figsize=(20.0,10.0))
          ax1 = fig.add_subplot(111)
          ax1.plot(x, reuse[0:MAX])
          ax1.set_xlabel("Node Degree")
          ax1.set_ylabel("Reuse Distance (cycles)")
          #plt.show()
          plt.savefig(appdir + input.split("_")[0] + "_" + str(cacheline_size) + "b_reuse_distance.pdf", bbox_inches='tight')

          fig = plt.figure(figsize=(20.0,10.0))
          ax1 = fig.add_subplot(111)
          ax1.plot(x, unused[0:MAX])
          ax1.set_xlabel("Node Degree")
          ax1.set_ylabel("Unused Space (bytes)")
          #plt.show()
          plt.savefig(appdir + input.split("_")[0] + "_" + str(cacheline_size) + "b_unused_space.pdf", bbox_inches='tight')

          # ----- ACCESS HISTOGRAM -----
          if cacheline_size == 4:
            scale = 0.5
            num_bins = int(num_nodes/100)
            fig = plt.figure(figsize=(20.0,10.0))
            ax1 = fig.add_subplot(111)
            n, bins, patches = ax1.hist(access, bins=num_bins, facecolor='blue', alpha=0.5)
            ax1.set_xlabel("Number of Accesses", fontsize=scale*AXIS_FONTSIZE)
            ax1.set_ylabel("Number of Nodes", fontsize=scale*AXIS_FONTSIZE)
            ax1.tick_params(axis="x", labelsize=scale*TICK_FONTSIZE)
            ax1.tick_params(axis="y", labelsize=scale*TICK_FONTSIZE)
            plt.xscale('log')
            plt.yscale('log')
            #plt.show()
            plt.savefig(appdir + input.split("_")[0] + "_access_histogram.pdf", bbox_inches='tight')
  plt.close('all')

def plot_hit_rate(app, appdir):
  print("\nPLOTTING HIT RATE...\n----------")

  y1 = [i/float(num_accesses1) for i in hit_rate_data[0]]
  y2 = [i/float(num_accesses2) for i in hit_rate_data[1]]
  y = [i/float(num_accesses) for i in hit_rate_data[2]]
  x = np.arange(len(y))
  labels = []
  for i in x:
    #label = str(factors[i])
    label = str(int(math.pow(2, i+2)))
    labels.append(label)

  fig = plt.figure(figsize=(36.0,24.0))
  ax1 = fig.add_subplot(111)
  ax1.plot(x, y1, label='Total Number of Hits for First ' + str(MAX) + ' Nodes')
  ax1.plot(x, y, label='Total Number of Hits')
  ax1.set_xticks(x)
  ax1.set_xticklabels(labels)
  ax1.set_xlabel("Cache Line Size (Bytes)")
  ax1.set_ylabel("Hit Rate")
  plt.legend(loc=2)
  #plt.show()
  plt.savefig(appdir + inputs[app].split('.')[0] + "_num_hits.pdf", bbox_inches='tight')

def cacheline(stats, avgs, outdir):
  #N = len(factors)
  N = int(math.log2(llama_cache_size)-1)
  ind = np.arange(1, 4)

  fig = plt.figure(figsize=(36.0,24.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  colors = ['black', 'dimgrey', 'grey', 'darkgray', 'darkgrey', 'silver', 'lightgrey', 'whitesmoke', 'white'] #NEED TO CHANGE COLORS BASED ON N
  psbs = []
  legend_boxes = []
  legend = []
  for i in range(N):
    if N % 2 == 0:
      pos = i-N/2+0.5
    else:
      pos = i-(N-1)/2
    psbs.append(ax1.bar(ind+pos*width/N, stats[0][i], width/N, linewidth=1, edgecolor=['black']))
    legend_boxes.append(psbs[i][0])
    #legend.append(str(factors[i]) + "B")
    legend.append(str(int(math.pow(2, i+2))) + "B")

  yticks = np.round(np.arange(0, 1.7, 0.1), 2)
  ylabel = 'Speedup'
  create_apps_axis(ax1, ind, yticks, ylabel)

  chartBox = ax1.get_position()
  ax1.set_position([chartBox.x0, chartBox.y0, chartBox.width, chartBox.height*0.8])
  ax1.legend(legend_boxes, legend, bbox_to_anchor=(0.,1.01,1.,0.101), ncol=N, mode="expand", fontsize=INPUTS_FONTSIZE)
  #plt.show()
  input_name = inputs[apps[0]].split('.')[0]
  plt.savefig(outdir + input_name + "_performance.pdf", bbox_inches='tight')
  
def parse_cycles(readdir, outdir):
  print("\nPARSING CYCLES...\n----------")

  runtimes = []
  speedups = []
  averages = []

  exp_dirs = [readdir]
  for a in range(len(apps)):
    app = apps[a]
    input = inputs[app]
    for e in range(len(exp_dirs)):
      exp_dir = exp_dirs[e]
      index = 0
      #for c in factors:
      #  size = str(c)
      for c in range(2, int(math.log2(llama_cache_size)+1)):
        size = str(int(math.pow(2, c)))
        filename = exp_dir + app + "_" + input.split(".")[0] + "_" + size + "b/measurements.txt"
        if len(runtimes) <= e:
          runtimes.append([])
        if (len(runtimes[e])) <= index:
          runtimes[e].append([])
        if os.path.isfile(filename):
          print("READING: " + filename)
          measurements = open(filename)
          data = measurements.read()
          measurements.close()
          matches = re.findall("^cycles : .*$", data, re.MULTILINE)
          match = re.match(".+:\s*(\d+\.*\d+)", matches[0])
          runtime = float(match.group(1))
          runtimes[e][index].append(runtime)
        else:
          fill = 1e20
          runtimes[e][index].append(fill)
        index+=1

  for e in range(len(runtimes)): #exps
    if len(speedups) <= e:
      speedups.append([])
    for c in range(len(runtimes[e])): #cachelines
      if len(speedups[e]) <= c:
        speedups[e].append([])
      for a in range(len(apps)): # apps
        speedups[e][c].append(runtimes[e][0][a]/runtimes[e][c][a])

  print("\nCALCULATING SPEEDUPS...\n----------")
  for e in range(len(runtimes)): #exps
    for c in range(len(runtimes[e])): #cachelines
      print(speedups[e][c])

  for e in range(len(speedups)): #exps
    averages.append([])
    for c in range(len(speedups[e])): #configs
      if len(averages[e]) <= c:
        averages[e].append(1.0)
      for a in range(len(runtimes[e][c])): #apps
        averages[e][c] = averages[e][c] * speedups[e][c][a]
      averages[e][c] = averages[e][c] ** (1./len(speedups[e][c]))

  cacheline(speedups, averages, outdir)

def characterize():
  if len(sys.argv) > 1:
    num_sets = sys.argv[1]
  else:
    num_sets = "1"
  outdir = "../results/characterization/" + str(CACHE_SIZE) + "B/llama_test_" + num_sets + "s/"
 
  if not os.path.isdir(outdir):
    os.mkdir(outdir)

  readdir = "/".join(["", "home", "ts20", "share", "results", "smart_cache"] + outdir.split("/")[2:])
  parse_cycles(readdir, outdir)

  if len(sys.argv) > 2:  
    apps = [sys.argv[2]]
  
  for app in apps:
    appdir = outdir + app + "/"
    if not os.path.isdir(appdir):
      os.mkdir(appdir)
  
    print("\nPARSING GRAPH NODE DATA...\n----------")

    #for c in factors:
    #  size = str(c)
    for c in range(2, int(math.log2(llama_cache_size)+1)):
      size = str(int(math.pow(2, c)))
      parse_reaccess([app], size, readdir, appdir)
    plot_hit_rate(app, appdir)

  print("\nDone!")

if __name__ == "__main__":
  characterize()

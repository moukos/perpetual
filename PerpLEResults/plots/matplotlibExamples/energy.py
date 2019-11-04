from plot import *

IO_POWER = 0.28
OOO_POWER = 2.44
L1_ENERGY = 0.082
L2_ENERGY = 0.194
DRAM_ENERGY = 8.12951
FIFO_ENERGY = 0.00748

metrics = ["cycles", "l1_hits", "l1_misses", "l2_hits", "l2_misses", "dram_accesses", "LD_PROD", "TRM_ATOMIC_CAS", "TRM_ATOMIC_FADD", "TRM_ATOMIC_MIN", "SEND", "STVAL"]

def parse_energy():
  # 1 IO, 1 OOO (test2) 
  # 8 IO, 4 decoupled (test4)

  energies = [[], [], []]
  ratios = [[], [], []]
  averages = []

  exp_dir = "/home/ts20/share/results/test2/"
  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      mode = "db"        
      for c in range(len(configs)):
        config = configs[c]
        filename = exp_dir + app + "_" + input.split(".")[0] + "_" + config + "_" + mode + "/genStats.txt"
        if len(energies[i]) <= c:
          energies[i].append([])
        if os.path.isfile(filename):
          measurements = open(filename)
          data = measurements.read()
          measurements.close()
          for metric in metrics:
            matches = re.findall("^" + metric + " : .*$", data, re.MULTILINE)
            if matches == []:
              stat = 0
            else:
              match = re.match("^" + metric + " : (\d+)$", matches[len(matches)-1])
              stat = int(match.group(1))
            if metric == "cycles":
              cycles = stat
            elif metric == "l1_hits":
              l1_hits = stat
            elif metric == "l1_misses":
              l1_misses = stat
            elif metric == "l2_hits":
              l2_hits = stat
            elif metric == "l2_misses":
              l2_misses = stat
            elif metric == "dram_accesses":
              dram_accesses = stat
            elif metric == "LD_PROD":
              ld_prod = stat
            elif metric == "TRM_ATOMIC_CAS":
              atomic_cas = stat
            elif metric == "TRM_ATOMIC_FADD":
              atomic_fadd = stat
            elif metric == "TRM_ATOMIC_MIN":
              atomic_min = stat
            elif metric == "SEND":
              send = stat
            elif metric == "STVAL":
              stval = stat

          time = 5e-10*cycles

          # core energy
          num_cores = 1
          if config == "IO":
            core_power = IO_POWER
          else:
            core_power = OOO_POWER
          core_energy = num_cores*core_power*time

          # memory energy
          mem_energy = (l1_hits + l1_misses)*L1_ENERGY + (l2_hits + l2_misses)*L2_ENERGY + DRAM_ENERGY*dram_accesses

          # queues energy
          term_ld = ld_prod + atomic_cas + atomic_fadd + atomic_min
          queues_energy = term_ld*7*FIFO_ENERGY + send*4*FIFO_ENERGY + stval*4*FIFO_ENERGY

          energy = (core_energy + 1e-9*mem_energy + 1e-9*queues_energy)*time
          energies[i][c].append(energy)

  exp_dir = "/home/ts20/share/results/test4/"
  for app in apps:
    for i in range(len(inputs[app])):
      input = inputs[app][i]
      t = 2
      for m in range(len(modes)):
        mode = modes[m]
        if mode == "db":
          num_cores = int(math.pow(2, t+1))
        else:
          num_cores = int(math.pow(2, t))
        index = m + 2
        filename = exp_dir + app + "_" + input.split(".")[0] + "_IO_" + mode + "_" + str(num_cores) + "/genStats.txt"
        if len(energies[i]) <= index:
          energies[i].append([])
        if os.path.isfile(filename):
          measurements = open(filename)
          data = measurements.read()
          measurements.close()
          for metric in metrics:
            matches = re.findall("^" + metric + " : .*$", data, re.MULTILINE)
            if matches == []:
              stat = 0
            else:
              match = re.match("^" + metric + " : (\d+)$", matches[len(matches)-1])
              stat = int(match.group(1))
            if metric == "cycles":
              cycles = stat
            elif metric == "l1_hits":
              l1_hits = stat
            elif metric == "l1_misses":
              l1_misses = stat
            elif metric == "l2_hits":
              l2_hits = stat
            elif metric == "l2_misses":
              l2_misses = stat
            elif metric == "dram_accesses":
              dram_accesses = stat
            elif metric == "LD_PROD":
              ld_prod = stat
            elif metric == "TRM_ATOMIC_CAS":
              atomic_cas = stat
            elif metric == "TRM_ATOMIC_FADD":
              atomic_fadd = stat
            elif metric == "TRM_ATOMIC_MIN":
              atomic_min = stat
            elif metric == "SEND":
              send = stat
            elif metric == "STVAL":
              stval = stat

          time = 5e-10*cycles

          # core energy
          core_power = IO_POWER
          core_energy = num_cores*core_power*time

          # memory energy
          mem_energy = (l1_hits + l1_misses)*L1_ENERGY + (l2_hits + l2_misses)*L2_ENERGY + DRAM_ENERGY*dram_accesses

          # queues energy
          term_ld = ld_prod + atomic_cas + atomic_fadd + atomic_min
          queues_energy = term_ld*7*FIFO_ENERGY + send*4*FIFO_ENERGY + stval*4*FIFO_ENERGY

          energy = (core_energy + 1e-9*mem_energy + 1e-9*queues_energy)*time
          energies[i][index].append(energy)

  for i in range(len(energies)): #inputs
    for c in range(len(energies[i])): #configs
      if len(ratios[i]) <= c:
        ratios[i].append([])
      for a in range(len(energies[i][c])): #apps
          ratios[i][c].append(energies[i][1][a]/energies[i][c][a])
  for i in range(len(energies)): #inputs
    for c in range(3, len(energies[i])): #configs    
      print(ratios[i][c])

  for c in range(len(energies[0])): #configs
    averages.append([])
    for a in range(len(energies[0][c])): #apps
      if len(averages[c]) <= a:
        averages[c].append(1.0)
      for i in range(len(energies)): #inputs
        averages[c][a] = averages[c][a] * ratios[i][c][a]
      averages[c][a] = averages[c][a] ** (1./len(energies))

  plot_energy(ratios, averages)

def plot_energy(stats, averages):
  N = 12
  ind = np.arange(1, 6)

  s1a = stats[0][1]
  s1b = stats[0][2]
  s1c = stats[0][3]
  s2a = stats[1][1]
  s2b = stats[1][2]
  s2c = stats[1][3]
  s3a = stats[2][1]
  s3b = stats[2][2]
  s3c = stats[2][3]
  s4a = averages[1]
  s4b = averages[2]
  s4c = averages[3]

  fig = plt.figure(figsize=(60.0,12.0))
  fig.subplots_adjust(bottom=0.1)
  ax1 = fig.add_subplot(111)

  dark = 'black'
  medium = 'darkgrey'
  light = 'white'
  
  sym = '.'
  psb1a = ax1.bar(ind-5.5*width/N, s1a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb1b = ax1.bar(ind-4.5*width/N, s1b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb1c = ax1.bar(ind-3.5*width/N, s1c, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb2a = ax1.bar(ind-2.5*width/N, s2a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb2b = ax1.bar(ind-1.5*width/N, s2b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb2c = ax1.bar(ind-0.5*width/N, s2c, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb3a = ax1.bar(ind+0.5*width/N, s3a, width/N, color=dark, linewidth=1, edgecolor=['black'])
  psb3b = ax1.bar(ind+1.5*width/N, s3b, width/N, color=medium, linewidth=1, edgecolor=['black'])
  psb3c = ax1.bar(ind+2.5*width/N, s3c, width/N, color=light, linewidth=1, edgecolor=['black'])
  psb4a = ax1.bar(ind+3.5*width/N, s4a, width/N, color=dark, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4b = ax1.bar(ind+4.5*width/N, s4b, width/N, color=medium, hatch=sym, linewidth=1, edgecolor=['black'])
  psb4c = ax1.bar(ind+5.5*width/N, s4c, width/N, color=light, hatch=sym, linewidth=1, edgecolor=['black'])

  yticks = np.arange(0, 19, 3)
  ylabel = 'Energy-Delay Improvement'
  create_x_axis_avg(ax1, ind, yticks, ylabel)

  legend = ('1 OoO Core', '8 Parallel In-Order Cores', '8 Parallel In-Order Cores (GeoMean)', '4 ' + approach + 's', '4 ' + approach + 's (GeoMean)')
  plt.legend((psb1a[0], psb1b[0], psb4b[0], psb1c[0], psb4c[0]), legend, loc=2, fontsize=INPUTS_FONTSIZE)
  #plt.show()
  plt.savefig("../results/energy.pdf", bbox_inches='tight')

def main():
  #parse_mem()
  parse_speedups()
  #parse_decoupling_output()
  parse_mlp()
  #runahead()
  parse_energy()

if __name__ == "__main__":
  main()

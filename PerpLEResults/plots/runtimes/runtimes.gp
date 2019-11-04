set terminal postscript enhanced color solid eps size 7,2 font "arial,12" 
set output 'runtimes.eps'
set key inside left top horizontal Left reverse noenhanced autotitle nobox
set datafile missing '-'
set style data linespoints
set xtics border in scale 1,0.5 nomirror rotate by -90  autojustify
set logscale y
set ylabel "Runtime (s)"
set xlabel "Iterations"
set datafile separator "\t"
set style line 1 lt 1 linecolor rgb "#9400D4"
set style line 2 lt 2 linecolor rgb "#049F75"
set style line 3 lt 3 linecolor rgb "#57B5E8"
set style line 5 lt 5 linecolor rgb "#F0E342"
set style line 7 lt 7 linecolor rgb "#E61F0F"
set style line 8 lt 8 linecolor rgb "black"
set style line 4 lt 4 linecolor rgb "#333333"
set style line 6 lt 6 linecolor rgb "violet"
set style line 9 lt 9 linecolor rgb "orange"
set style line 10 lt 10 linecolor rgb "blue"
plot 'runtimes.csv' using 2:xtic(1) title columnheader(2) ls 1, \
  for [i=3:3] '' using i title columnheader(i) ls 3, \
  for [i=4:4] '' using i title columnheader(i) ls 4, \
  for [i=5:5] '' using i title columnheader(i) ls 5, \
  for [i=6:6] '' using i title columnheader(i) ls 6, \
  for [i=7:7] '' using i title columnheader(i) ls 7, \
  for [i=8:8] '' using i title columnheader(i) ls 8, \
  for [i=9:9] '' using i title columnheader(i) ls 9, \

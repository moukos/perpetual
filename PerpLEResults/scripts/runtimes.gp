set terminal postscript enhanced color solid eps size 7,2 font "arial,12" 
set output 'runtimes.eps'
set key inside left top horizontal Left reverse noenhanced autotitle nobox
set datafile missing '-'
set style data linespoints
set xtics border in scale 1,0.5 nomirror rotate by -90  autojustify
set logscale y
set ylabel "Runtime (s)"
set datafile separator "\t"
set style line 1 lt 1 linecolor rgb "#9400D4"
set style line 2 lt 2 linecolor rgb "#049F75"
set style line 3 lt 3 linecolor rgb "#57B5E8"
set style line 5 lt 5 linecolor rgb "#F0E342"
set style line 7 lt 7 linecolor rgb "#E61F0F"
set style line 8 lt 8 linecolor rgb "black"
plot 'runtimes-100k.csv' using 2:xtic(1) title columnheader(2) ls 1, \
  for [i=3:3] '' using i title columnheader(i) ls 2, \
  for [i=4:4] '' using i title columnheader(i) ls 3

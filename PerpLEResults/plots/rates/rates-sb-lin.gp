set terminal postscript enhanced color solid eps size 7,2 font "arial,12" 
set output 'rates-sb-lin.eps'
set key inside left top horizontal Left reverse noenhanced autotitle nobox
set datafile missing '-'
set style data linespoints
set xtics border in scale 1,0.5 nomirror rotate by -90  autojustify
set ylabel "Testing rate (Cycles/time)"
set xlabel "Iterations"
set datafile separator ","
set style line 1 lt 1 linecolor rgb "#9400D4"
set style line 2 lt 2 linecolor rgb "#049F75"
set style line 3 lt 3 linecolor rgb "#57B5E8"
plot 'rates-sb.csv' using 2:xtic(1) title columnheader(2) ls 2, \
  for [i=3:3] '' using i title columnheader(i) ls 3, \
  for [i=4:4] '' using i title columnheader(i) ls 4

set terminal postscript enhanced color solid eps size 10,3 font "Garamond,18" 
set output 'georates.eps'
set key inside left top horizontal Left reverse noenhanced autotitle nobox
set datafile missing '-'
set style data linespoints
set xtics border in scale 1,0.5 nomirror rotate by -90  autojustify
set logscale y
set ylabel "Outcome detection rate\n(outcomes/s)"
set datafile separator "\t"
set style line 1 lt 1 linecolor rgb "#9400D4"
set style line 2 lt 2 linecolor rgb "#049F75"
set style line 3 lt 3 linecolor rgb "brown"
set style line 5 lt 5 linecolor rgb "gray"
set style line 7 lt 7 linecolor rgb "#e56b5d"
set style line 8 lt 8 linecolor rgb "black"
set style line 4 lt 4 linecolor rgb "blue"
plot 'georates.csv' using 3:xtic(1) title columnheader(3) ls 1, \
for [i=4:4] '' using i title columnheader(i) ls 2, \
      '' u 2 ti col lt rgb "#049F75", \
      '' u 4 ti col lt rgb "brown", \
      '' u 7 ti col lt rgb "gray", \
      '' u 6 ti col lt rgb "#e56b5d",\
      '' u 5 ti col lt rgb "blue", \
      '' u 8 ti col lt rgb "black"

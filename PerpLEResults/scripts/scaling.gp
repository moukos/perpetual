set terminal postscript eps enhanced color font "Garamond-Bold,18pt" size 4in,2in
set output 'averages-scaling.eps'
set boxwidth 0.7 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 1
set style histogram clustered gap 0.4 title textcolor lt -1
set datafile missing '?'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set datafile separator "\t"
set xtics   ()
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set yrange [ 0 : 4 ] noreverse nowriteback
set ylabel "Geomean speedup"
set xlabel "Iterations"
x = 0.0
i = 22
plot 'averages-scaling.csv' using 4:xtic(1) ti col lt rgb "#4b03a1"

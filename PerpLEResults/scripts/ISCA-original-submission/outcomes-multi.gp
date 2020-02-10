set terminal postscript eps enhanced color font "Garamond-Bold,18pt" size 7in,2.6in
set output 'Outcomes-multi.eps'
set datafile separator ","
set boxwidth 0.95 absolute
set style fill   solid border lt -1
set key inside top right vertical Right noreverse noenhanced autotitle nobox maxrows 2
set key samplen 3
set key font ",15"
set style histogram clustered gap 0.4 title textcolor lt -1
set datafile missing '-'
set style data histograms
set tics font "Garamond-Bold,15"
set tics font "Garamond-Bold,15"
set xtics border in scale 0,0 nomirror rotate by -90  autojustify
set xtics  norangelimit
set xtics   ()
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set grid xtics lc rgb "#bbbbbb" lw 4 lt 0
set logscale y
set yrange [ 1. :10000000000. ] noreverse nowriteback
set ylabel "Outcome Occurrences" offset 0,-1.6,0
x = 0
i = 16
plot 'outcomes-multi.csv' using 2:xtic(1) ti col lt rgb "#4b03a1", \
   '' u 3 ti col lt rgb "#e56b5d" 

set terminal postscript eps enhanced color font "Garamond-Bold,20pt" size 7in,2.8in
set output 'Outcomes-multi-10k.eps'
set datafile separator ","
set boxwidth 0.98 absolute
set bmargin 3
set style fill   solid border lt -1
set key inside top left vertical Right noreverse noenhanced autotitle nobox maxrows 1
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by 0  autojustify
set xtics  norangelimit
set xtics   ()
set arrow 1 from 3.45,1 to 3.45,10000000000000. nohead ls 0 lw 10 front
set arrow 2 from 7.4,1 to 7.45,10000000000000. nohead ls 0 lw 10 front
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set grid xtics lc rgb "#bbbbbb" lw 4 lt 0
set logscale y
set yrange [ 1. :100000000000000. ] noreverse nowriteback
set ylabel "Outcome Count" offset 0,-1.6,0 font "Garamond-Bold,20pt"
x = 0
i = 16
plot 'outcomes-multi-10k.csv' using 2:xtic(1) ti col lt rgb "#4b03a1", \
   '' u 3 ti col lt rgb "#e56b5d"

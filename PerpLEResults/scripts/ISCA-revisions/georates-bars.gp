set terminal postscript eps enhanced color font "Garamond-Bold,18pt" size 7in,2.2in
set output 'georates-10k-bars.eps'
set boxwidth 0.9 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 3
set tics font "Garamond-Bold,20"
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '?'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set datafile separator "\t"
set xtics   ()
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set logscale y
set yrange [ 100 : 100000000 ] noreverse nowriteback
set ylabel "Detection rate \n(Outcomes/s)" font "Garamond-Bold,20pt"
set xlabel "Test iterations"
x = 0.0
i = 22
plot 'georates.csv' using 3:xtic(1) ti col lt rgb "#049F75", \
    '' u 2 ti col lt rgb "#4b03a1", \
    '' u 4 ti col lt rgb "brown", \
    '' u 6 ti col lt rgb "#e56b5d",\
    '' u 5 ti col lt rgb "blue", \
    '' u 7 ti col lt rgb "gray", \
    '' u 8 ti col lt rgb "black"

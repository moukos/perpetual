set terminal posts eps enhanced color font "Garamond-Bold,18pt" size 7in,2in
set output 'single-outcomes-10k.eps'
set boxwidth 0.9 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 2
set tics font "Garamond-Bold,13"
set style histogram clustered gap 2 title textcolor lt -1
set datafile missing '?'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set datafile separator "\t"
set xtics   ()
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set logscale y
set yrange [ 0.01 : 100000000 ] noreverse nowriteback
set ylabel "Outcome Occurrences"
x = 0.0
i = 22
plot 'single-outcomes-10k.csv' using 2:xtic(1) ti col lt rgb "#4b03a1", \
    '' u 3 ti col lt rgb "#049F75", \
    '' u 4 ti col lt rgb "brown", \
    '' u 7 ti col lt rgb "gray", \
    '' u 6 ti col lt rgb "#e56b5d",\
    '' u 5 ti col lt rgb "blue", \
    '' u 8 ti col lt rgb "black"


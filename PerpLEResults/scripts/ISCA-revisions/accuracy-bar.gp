set terminal postscript eps enhanced color font "Garamond-Bold,18pt" size 7in,2.5in
set output 'accuracy-bar.eps'
set boxwidth 0.95 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 2
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '-'
set datafile separator "\t"
set tics font "Garamond-Bold,13"
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set xtics   ()
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set yrange [ 0 : 115. ] noreverse nowriteback
set ylabel "Heuristic Accuracy (%)"
x = 0.0
i = 22
plot 'accuracy.csv' using 2:xtic(1) ti col lt rgb "#049F75"

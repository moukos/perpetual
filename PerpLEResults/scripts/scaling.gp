set terminal postscript eps enhanced color font "Garamond-Bold,16pt" size 7in,1.5in
set output 'averages-scaling.eps'
set boxwidth 0.8 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 1
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '?'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set datafile separator "\t"
set xtics   ()
set yrange [ 0 : 5 ] noreverse nowriteback
set ylabel "Geomean speedup"
set xlabel "Iterations"
x = 0.0
i = 22
plot 'averages-scaling.csv' using 2:xtic(1) ti col lt rgb "#B0624A", \
    '' u 3 ti col lt rgb "#B09940", \
    '' u 4 ti col lt rgb "#7FD282"

set terminal postscript eps enhanced color font "Garamond-Bold,16pt" size 7in,1.5in
set output 'runtimes-bars.eps'
set boxwidth 0.8 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 3
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set xtics   ()
set logscale y
set yrange [ 0.001 : 1000. ] noreverse nowriteback
set ylabel "Runtime (s)"
set xlabel "Iterations"
x = 0.0
i = 3
plot 'runtimes.csv' using 2:xtic(1) ti col lt rgb "#B0624A", \
    '' u 3 ti col lt rgb "#B09940", \
    '' u 4 ti col lt rgb "#7FD282", \
    '' u 5 ti col lt rgb "#55FCFE",  \
    '' u 6 ti col lt rgb "red", \
    '' u 7 ti col lt rgb "black", \
    '' u 8 ti col lt rgb "orange", \
    '' u 9 ti col lt rgb "green", \
    '' u 10 ti col lt rgb "blue"





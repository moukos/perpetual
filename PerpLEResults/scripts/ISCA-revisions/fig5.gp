set terminal postscript eps enhanced color font "Garamond-Bold,16pt" size 7in,1.5in
set output 'fig5.eps'
set boxwidth 0.8 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 2
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set xtics   ()
set logscale y
set yrange [ 0.001 : 100. ] noreverse nowriteback
set ylabel "Runtime (s)"
x = 0.0
i = 22
plot 'fig5.dat' using 2:xtic(1) ti col lt rgb "#B0624A", \
    '' u 3 ti col lt rgb "#B09940", \
    '' u 4 ti col lt rgb "#7FD282", \
    '' u 5 ti col lt rgb "#55FCFE"


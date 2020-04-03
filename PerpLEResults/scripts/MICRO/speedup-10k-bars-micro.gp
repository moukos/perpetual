set terminal postscript eps enhanced color font "Garamond-Bold,20pt" size 14in,2.5in
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 1
set output 'speedup-10k-micro.eps'
set bmargin 5
set multiplot layout 1,2 \
              spacing 0.08,0.08
set boxwidth 0.95 absolute
set lmargin 6
set style fill   solid border lt -1
set tics font "Garamond-Bold,17"
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '?'
set style data histograms
set logscale y
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set datafile separator "\t"
set xtics   ()
set arrow 1 from -1,1 to 34,1 nohead ls 0 lw 3 front
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set yrange [ 0.005 : 100 ] noreverse nowriteback
set ylabel "Runtime speedup" offset 3
x = 0.0
i = 22
plot 'speedup-10k.csv' using 4:xtic(1) ti col lt rgb "#049F75",\
    '' u 3 ti col lt rgb "#4b03a1"
set lmargin 3
set boxwidth 0.95 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 2
set tics font "Garamond-Bold,17"
set style histogram clustered gap 0.7 title textcolor lt -1
set datafile missing '?'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -45  autojustify
set xtics  norangelimit
set datafile separator "\t"
set xtics   ()
set grid ytics lc rgb "#bbbbbb" lw 2 lt 0
set yrange [ 0.02 : 100 ] noreverse nowriteback
set ylabel "Runtime speedup" offset 0.75
set arrow 1 from -1,1 to 34,1 nohead ls 0 lw 3 front
x = 0.0
i = 22
plot 'speedup-10k.csv' using 4:xtic(1) ti col lt rgb "#049F75", \
     '' u 7 ti col lt rgb "black",\
     '' u 6 ti col lt rgb "#e56b5d",\
     '' u 5 ti col lt rgb "brown",\
     '' u 8 ti col lt rgb "gray"
unset multiplot

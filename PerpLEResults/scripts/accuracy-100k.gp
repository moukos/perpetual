set terminal postscript enhanced color solid eps size 7,2 font "arial,12" 
set output 'accuracy-100k.eps'
set key inside left top horizontal Left reverse noenhanced autotitle nobox
set datafile missing '-'
set style data linespoints
set xtics border in scale 1,0.5 nomirror rotate by -90  autojustify
set yrange [ 0 : 100] noreverse nowriteback
set ylabel "Heuristic Accuracy (%)"
set datafile separator "\t"
set style line 1 lt 1 linecolor rgb "#9400D4"
set style line 2 lt 2 linecolor rgb "#049F75"
set style line 3 lt 3 linecolor rgb "#57B5E8"
set style line 5 lt 5 linecolor rgb "#F0E342"
set style line 7 lt 7 linecolor rgb "#E61F0F"
set style line 8 lt 8 linecolor rgb "black"
plot 'accuracy.csv' using 2:xtic(1) title columnheader(2) ls 1

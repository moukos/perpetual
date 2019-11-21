set terminal postscript eps enhanced color font "Garamond-Bold,16pt" size 7in,1.8in
set output 'accuracy-bar.eps'
set boxwidth 0.8 absolute
set style fill   solid border lt -1
set key inside left top vertical Right noreverse noenhanced autotitle nobox maxrows 2
set style histogram clustered gap 1 title textcolor lt -1
set datafile missing '-'
set style data histograms
set xtics border in scale 0,0 nomirror rotate by -90  autojustify
set xtics  norangelimit
set xtics   ()
set yrange [ 0 : 102. ] noreverse nowriteback
set ylabel "Heuristic Accuracy (%)"
x = 0.0
i = 22
plot 'accuracy.csv' using 2:xtic(1) ti col lt rgb "#B0624A"

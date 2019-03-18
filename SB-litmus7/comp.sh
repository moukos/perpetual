GCC=gcc
GCCOPTS="-Wall -std=gnu99 -fomit-frame-pointer -O2 -pthread"
LINKOPTS=""
/bin/rm -f *.exe *.s
$GCC $GCCOPTS -O2 -c outs.c
$GCC $GCCOPTS -O2 -c utils.c
$GCC $GCCOPTS -O2 -c litmus_rand.c
$GCC $GCCOPTS $LINKOPTS -o SB.exe outs.o utils.o litmus_rand.o SB.c
$GCC $GCCOPTS -S SB.c && awk -f show.awk SB.s > SB.t && /bin/rm SB.s

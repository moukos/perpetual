GCC=gcc
GCCOPTS="-Wall -std=gnu99 -fomit-frame-pointer -O2 -pthread"
LINKOPTS=""
/bin/rm -f *.exe *.s
$GCC $GCCOPTS -O2 -c outs.c
$GCC $GCCOPTS -O2 -c utils.c
$GCC $GCCOPTS -O2 -c litmus_rand.c
$GCC $GCCOPTS $LINKOPTS -o sb.exe outs.o utils.o litmus_rand.o sb.c
$GCC $GCCOPTS -S sb.c && awk -f show.awk sb.s > sb.t && /bin/rm sb.s

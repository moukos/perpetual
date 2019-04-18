GCC=gcc
GCCOPTS="-Wall -std=gnu99 -fomit-frame-pointer -O2 -pthread"
LINKOPTS=""
/bin/rm -f *.exe *.s
$GCC $GCCOPTS -O2 -c outs.c
$GCC $GCCOPTS -O2 -c utils.c
$GCC $GCCOPTS $LINKOPTS -o MP.exe outs.o utils.o MP.c
$GCC $GCCOPTS -S MP.c && awk -f show.awk MP.s > MP.t && /bin/rm MP.s

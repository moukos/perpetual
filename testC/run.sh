date
LITMUSOPTS="${@:-$LITMUSOPTS}"
SLEEP=0
if [ ! -f MP.no ]; then
cat <<'EOF'
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Results for litmus/MP.litmus %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
X86 MP
"Fre PodWR Fre PodWR"

{x=0; y=0;}

 P0         | P1          ;
 MOV [x],$1 | MOV ECX,[y] ;
 MOV [y],$1 | MOV EAX,[x] ;

locations [x; y; ]
exists (1:ECX=1 /\ 1:EAX=0)
Generated assembler
EOF
cat MP.t
./MP.exe -q $LITMUSOPTS
fi
sleep $SLEEP

cat <<'EOF'
Revision exported, version 5.99-D
Command line: litmus litmus/MP.litmus -o testC
Parameters
#define SIZE_OF_TEST 100000
#define NUMBER_OF_RUN 10
#define AVAIL 1
#define STRIDE (-1)
#define MAX_LOOP 0
/* gcc options: -Wall -std=gnu99 -fomit-frame-pointer -O2 -pthread */
/* barrier: user */
/* launch: changing */
/* affinity: none */
/* prealloc: false */
/* memory: direct */
/* safer: write */
/* preload: random */
/* speedcheck: no */
EOF
head -1 comp.sh
echo "LITMUSOPTS=$LITMUSOPTS"
date

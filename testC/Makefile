GCC=gcc
GCCOPTS=-Wall -std=gnu99 -fomit-frame-pointer -O2 -pthread
LINKOPTS=
SRC=\
 MP.c\

EXE=$(SRC:.c=.exe)
T=$(SRC:.c=.t)

all: $(EXE) $(T)

clean:
	/bin/rm -f *.o *.s *.t *.exe *~

cleansource:
	/bin/rm -f *.o *.c *.h *.s *~

outs.o: outs.c
	$(GCC) $(GCCOPTS) -O2 -c outs.c

utils.o: utils.c
	$(GCC) $(GCCOPTS) -O2 -c utils.c

UTILS=outs.o utils.o

%.exe:%.s $(UTILS)
	$(GCC) $(GCCOPTS) $(LINKOPTS) -o $@ $(UTILS) $<

%.s:%.c
	$(GCC) $(GCCOPTS) -S $<

%.t:%.s
	awk -f show.awk $< > $@


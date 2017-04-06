#compiler and linker
CC := gcc

#compile options (Standard, Warning, Optimizer, and gdb debugger)
CCOPTS := -std=c99 -O2 -Wall -g

#object file and source file
MYSRC := C_extract_min_energy.c
MYOBJ := C_extract_min_energy.o
EXEC := op_getter


$(EXEC): $(MYOBJ)
	$(CC) $(CCOPTS) -o $(EXEC) $(MYOBJ)

$(MYOBJ): $(MYSRC)
	$(CC) $(CCOPTS) -c $(MYSRC)
	

clean:
	rm -f *.o *~ $(EXEC)

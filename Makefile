# Compiler

CC := g++

# Compiler Options

CCOPTS := -Wall -std=c++11 -O2 -g

# Object File and Source File
STRUCTUREC := Structure.cpp
STRUCTURE := Structure

# Run
run: build
		./$(STRUCTURE) -i structure.out -o new3.xyz -n molybdinum-disulfide


# Build all files
build: $(STRUCTURERC)
		$(CC) $(CCOPTS) -o $(STRUCTURE) $(STRUCTUREC)

# Debugging
memcheck:
		Valgrind --leak-check=full ./$(STRUCTURE) -i structure.out -o new3.xyz

# Clean Up
clean:
	rm -rf core a.out $(STRUCTURE) *~ *.o
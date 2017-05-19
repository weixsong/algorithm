all: CPU

CPU: CPU.o CPUtils.o
	g++ CPU.o CPUtils.o -o cpu

CPU.o: CPU.c
	g++ -c CPU.c

CPUtils.o: CPUtils.c
	g++ -c CPUtils.c

clean:
	rm -rf *o hello

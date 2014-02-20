clap: clap.cpp
	g++ -o build/clap clap.cpp

sconv: sconv.c
	gcc -O3 -o build/sconv sconv.c

pa: clap
	./pastream.sh | ./build/clap

clean:
	rm build/*

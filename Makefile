clap: src/clap.cpp
	g++ -O3 -o build/clap src/clap.cpp

sconv: src/sconv.c
	gcc -O3 -o build/sconv src/sconv.c

clean:
	rm build/*

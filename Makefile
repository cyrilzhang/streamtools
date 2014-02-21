sconv: src/sconv.c
	gcc -O3 -o build/sconv src/sconv.c

clean:
	rm build/*

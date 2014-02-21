/*
sconv: convert audio stream to decimal stream
flush rate is 256 by default, can be specified by -r flag
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char** argv) {
	char buf[2];
	int count = 0;
	int FLUSH_RATE = 256;

	if(argc == 3) {
		if(!strcmp(argv[1], "-r")) FLUSH_RATE = strtol(argv[2], NULL, 10);
	}

	fprintf(stderr, "sconv: streaming with flush rate %d\n", FLUSH_RATE);

	while( fread(buf, 4, 1, stdin) ) {
		printf("%d\n", (int)*(short*)buf + (int)*(short*)(buf+2));
		
		++count;
		if(count == FLUSH_RATE) {
			fflush(stdin);
			count = 0;
		}
	}
	return 0;
}

/*
Usage:
pacat -r --latency-msec=1 -d alsa_input.pci-0000_00_1b.0.analog-stereo | ./clap
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <ctime>

using namespace std;

const int BLOCK_SIZE = 1024;
const int DEBOUNCE_RATE = 10;
const double CLAP_THRESHOLD = 1000;

double tick() {
	static double last_tick = 0;
	
	struct timespec next_tick_ts={0,0};
	clock_gettime(CLOCK_MONOTONIC, &next_tick_ts);
	double next_tick = (double)next_tick_ts.tv_sec + 1.0e-9*next_tick_ts.tv_nsec;

	double dur = next_tick - last_tick;
	last_tick = next_tick;

	return dur;
}

void clap() {
	static int count = 0;
	static int consec_clap;
	++count;
	if(tick() < 0.5) ++consec_clap;
	else consec_clap = 1;

	if(consec_clap == 2) {
		cout << "dblclap " << count << '\n';
		system("spotify-dbus PlayPause");
		consec_clap = 0;
	}
	else {
		cout << "clap " << count << '\n';
	}
}

short read_short() {
	static char buf[2];
	if(!cin.read(buf, 2)) exit(0);
	return *(short*)buf;
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int debounce = 0;

	while(1) {
		double block_mean = 0;
		for(int i=0; i<BLOCK_SIZE; ++i) {
			block_mean += abs( read_short() );
		}
		block_mean /= BLOCK_SIZE;

		if(block_mean > CLAP_THRESHOLD) {
			if(debounce >= DEBOUNCE_RATE){
				clap();
				debounce = 0;
			}
			else {
				cout << "debounce\n";
			}
		}
		else ++debounce;
	}
	return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <unistd.h>

#include "CPUtils.h"

const int CPU_KERNEL_ID = 0x0003;

const int SAMPLE_COUNT = 200;
const int TIME_SLICE = 200; // ms in second
const int TIME_TRANFORM = 1000; // change ms to us
long * busy_span;

// init the busy span, this is used to control the cpu busy time for each sample point
int init_busySpan(int sample_count)
{
	busy_span = (long *)malloc(sample_count * sizeof(long));
	if(busy_span == NULL)
	{
		return -1;
	}
	double radian = 0.0;
	double radianIncrement = 2.0 / (double)sample_count;
	int amplitude = (int)(TIME_SLICE / 2); // amplitude of sin curves, it means half of the time slice because sin() has negative value

	int i;
	for(i = 0; i < sample_count; i++)
	{
		busy_span[i] = (long)(amplitude + sin(radian * PI) * amplitude);
		radian = radian + radianIncrement;
	}
	return 1;
}

int main(void)
{
	if(set_cpu(CPU_KERNEL_ID) == 0)
	{
		printf("cpu affinity set failed\n");
	}
	else
	{
		printf("cpu affinity set succeeded\n");
	}

	printf("clock per second:%ld \n", CLOCKS_PER_SEC);
	fflush(stdout);

	if(!(init_busySpan(SAMPLE_COUNT)))
	{
		printf("init error \n");
		return 0;
	}

	int i = 0;
	long busy_time; // us
	long sleep_time; // us
	clock_t begin;
	for(i = 0; ; i = (i + 1) % SAMPLE_COUNT)
	{
		busy_time = busy_span[i] * TIME_TRANFORM;
		begin = clock();
		while((clock() - begin) < busy_time)
		{
			// loop
		}
		sleep_time = (long)((TIME_SLICE - busy_span[i])) * TIME_TRANFORM;
		usleep(sleep_time);
	}

	return 1;
}

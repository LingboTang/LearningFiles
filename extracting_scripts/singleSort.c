#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <sys/time.h>
#include <time.h>
#include <unistd.h>

int cmpfunc(const void*a, const void*b)
{
	return (*(long int*)a - *(long int*)b);
}

void printArr(long int* arr, int size)
{

	for (int i = 0; i< size; i++)
        {
            if (i == 0)
            {
                printf("[ ");
            }
            printf("%ld ",arr[i]);
            if (i == size -1)
            {
                printf("]\n");
	    }
	}
}

int main(int argc, char**argv) {


	struct timeval start;
    	struct timeval end;

    	char * fileName;
    	FILE * outFile;
	if (argc != 3)
	{
		fprintf(stderr, "error: Not enough info!\n");
		exit(EXIT_FAILURE);
	}
	int numbers = atoi(argv[1]);
    	fileName = argv[2];
    	outFile = fopen(fileName,"a+"); 
	int i;

	long int * array = (long int *) malloc(sizeof(long int)*numbers);

	srandom(time(NULL));

	for (i = 0; i < numbers; i++)
	{
        	array[i] = random();
        }	

	gettimeofday(&start, NULL);
	qsort(array,numbers,sizeof(long int),cmpfunc);
	gettimeofday(&end, NULL);
    	double time_spent = (double)(end.tv_sec - start.tv_sec) * 1.0e6 + (double) (end.tv_usec - start.tv_usec);
	time_spent = time_spent / 1000000;
	//printArr(array,numbers);
	fprintf(outFile, "%d, %f\n",numbers,time_spent);
	free((void *) array);
	fclose(outFile);	
	return 0;        		    	
}

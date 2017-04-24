/*
 * Lib included
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <regex.h>

/*
 * Global Values
 */
#define BUFF_SIZE 256
#define MAX_THREADS 8 
regex_t regex;
regex_t regex2;
int reti;
int reti2;

/*
 * From https://cboard.cprogramming.com/c-programming/117525-regex-h-extracting-matches.html
 * Author: MK27
 * Time:  07-11-2009
 */
char *regexp (char *string, char *patrn, int *begin, int *end) {
        int i, w=0, len;
        char *word = NULL;
        regex_t rgT;
        regmatch_t match;
        // Set the comparison
        regcomp(&rgT,patrn,REG_EXTENDED);
        if ((regexec(&rgT,string,1,&match,0)) == 0) {
                //looping the matched part by two pointers
                *begin = (int)match.rm_so;
                *end = (int)match.rm_eo;
                len = *end-*begin;
                word=malloc(len+1);
                for (i=*begin; i<*end; i++) {
                        word[w] = string[i];
                        w++; }
                word[w]=0;
        }
        regfree(&rgT);
        return word;
}

int main(int argc, char** argv) {


	FILE * inputf, * outputf;
	char line[BUFF_SIZE];
	char * FileName, * OutFileName;
	double energy;

    /*Set Regex for Key word*/
	reti = regcomp(&regex, "energy: ", 0);
	if (reti) {
		fprintf(stderr, "Could not compile regex\n");
		fflush(stderr);
		exit(1);
	}

    /*Set Regex for real literals*/
	reti2 = regcomp(&regex2, "[+-]?([0-9]*[.])?[0-9]+", REG_EXTENDED);
	if (reti2) {
		fprintf(stderr, "Could not compile regex of floating literals\n");
		fflush(stderr);
		exit(1);
	}

    /*If command line is not correct, then do not execute this file*/
	if (argc != 3) {
		fprintf(stderr, "Usage: ./lingbo_op_getter <inputfile>\n");
		fflush(stderr);
		exit(0);
	}

    /*Open Input file*/
	FileName = argv[1];
	inputf = fopen(FileName, "r");

	if (!inputf) {
		fprintf(stderr, "Error: Can't open the file to read: %s\n", FileName);
		fflush(stderr);
		exit(2);
	}

    /*Open Output file 'a+' is for accumunate lines in one file*/
	OutFileName = argv[2];
    outputf = fopen(OutFileName,"a+");

    if (!inputf) {
    	fprintf(stderr, "Error: Can't open the file to write: %s\n", OutFileName);
    	fflush(stderr);
    	exit(2);
    }

    /* Parsing and grab the energy in the file */
	while (!feof(inputf)) {
		fgets(line, BUFF_SIZE, inputf);
		//if keyword matched
		reti = regexec(&regex, line, 0, NULL, 0);
        if (!reti) {
                reti2 = regexec(&regex2, line, 0, NULL, 0);
                //if number matched
                if (!reti2) {
                    int b,e;
                    char *match=regexp(line,"[+-]?([0-9]*[.])?[0-9]+",&b,&e);
                    energy = atof(match);
                    fprintf(outputf, "%f\n", energy);
                }
        }
        else if (reti == REG_NOMATCH) {

        }
        else {
                regerror(reti, &regex, line, sizeof(line));
                fprintf(stderr, "Regex match failed: %s\n", line);
                exit(1);
        }
	}

	regfree(&regex);
	regfree(&regex2);
	fclose(inputf);
	fclose(outputf);

	return 0;
}
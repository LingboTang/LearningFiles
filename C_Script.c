#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <regex.h>

#define BUFF_SIZE 256
regex_t regex;
regex_t regex2;
int reti;
int reti2;

int main(int argc, char** argv) {

	FILE * inputf;
	char line[BUFF_SIZE];	
	char * FileName;
	double energy;

	reti = regcomp(&regex, "energy: ", 0);
	if (reti) {
		fprintf(stderr, "Could not compile regex\n");
		exit(1);
	}

	reti2 = regcomp(&regex2, "[+-]?([0-9]*[.])?[0-9]+", 0);
	if (reti2) {
		fprintf(stderr, "Could not compile regex of real literal\n");
		exit(1);
	}

	char * testString = "-87.21";
	reti2 = regexec(&regex, testString, 0, NULL, 0);
	if (!reti2) {
		printf("%s \n", testString);
	}

	if (argc != 2) {
		fprintf(stderr, "Usage: ./lingbo_op_getter <inputfile>\n");
		fflush(stderr);
	}

	FileName = argv[1];
	inputf = fopen(FileName, "r");

	if (!inputf) {
		fprintf(stderr, "Error: Can't open the file %s", FileName);
		fflush(stderr);
	}

	while (!feof(inputf)) {
		fgets(line, BUFF_SIZE, inputf);
		reti = regexec(&regex, line, 0, NULL, 0);
        	if (!reti) {
			/*reti2 = regexec(&regex2, line, 0, NULL, 0);
			if (!reti2) {
				printf("energy is : %s",line);
			}*/
                	//energy =
                	printf("%s",line); 
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

	return 0;
}

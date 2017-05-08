#include <unistd.h>
#include "Structure.hpp"
#include <boost/algorithm/string.hpp>
#include <typeinfo>
#include <regex>

using namespace std;

int main(int argc, char ** argv) {
	int opt;
	string in_f_name;
	string out_f_name;
	ifstream inFile;
	ofstream outFile;
	vector<string> filedata;
	string lineString;
	regex name_regex("Atoms");
	smatch name_match;

	if (argc != 5) {
		cerr << "Error: Invalid number of arguments" << endl;
		cout << "Usage: ./Structure -i <inputfile> -o <outfile>" << endl;
		exit(EXIT_FAILURE);
	}

	while ((opt = getopt(argc, argv, "i:o:")) != EOF) {
		switch(opt) {
			case 'i':
				in_f_name = optarg;
				break;
			case 'o':
				out_f_name = optarg;
				break;
			default:
				break;
		}
	}

	inFile.open(in_f_name);
	if (!inFile) {
		cerr << "Error: Given file " << in_f_name << " does not exist!" << endl;
		exit(EXIT_FAILURE);
	}

	outFile.open(out_f_name);
	if (!outFile) {
		cerr << "Error: Given file " << out_f_name << " does not exist!" << endl;
		exit(EXIT_FAILURE);
	}

	while(getline(inFile,lineString))
	{
		boost::algorithm::trim(lineString);
		outFile << lineString << endl;
		filedata.push_back(lineString);
		//cout << regex_search(lineString,name_match,name_regex) << endl;
	}

	cout << filedata.size() << endl;
	for (int i = 0; i< (int) filedata.size(); ++i) {
		//cout << filedata[i] << endl;
	}

	for (const auto& line : filedata) {
		regex_match(line,name_match,name_regex);
		cout << name_match.size() << endl;
	}

	/*for(vector<string>::iterator it(filedata.begin()), end(filedata.end()); it!=end; it++) {
		cout << *it << endl;
	}*/

	inFile.close();
	outFile.close();


	return 0;
}
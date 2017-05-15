#include <unistd.h>
#include "Structure.hpp"
#include <boost/algorithm/string.hpp>
#include <typeinfo>
#include <cstdio>
//#include <regex>

using namespace std;

unitCell::unitCell(string S1, string S2, string Mo, vector<Coord> Unit_Coords) :
S1(S1), S2(S2), Mo(Mo), Unit_Coords(Unit_Coords) {
	this -> S1 = "S";
	this -> S2 = "S";
	this -> Mo = "Mo";
	this -> Unit_Coords = Unit_Coords;
}

unitCell::~unitCell() {

}

unitCell::unitCell(const unitCell &rhs) {
	this -> S1 = rhs.S1;
	this -> S2 = rhs.S2;
	this -> Mo = rhs.Mo;
	this -> Unit_Coords = rhs.Unit_Coords;
}

unitCell & unitCell::operator= (const unitCell &rhs) {
	if (this != &rhs) {
		S1 = rhs.S1;
		S2 = rhs.S2;
		Mo = rhs.Mo;
		Unit_Coords = rhs.Unit_Coords;
	}
	return *this; 
}

string unitCell::getS1() const {
	return S1;
}

string unitCell::getS2() const {
	return S2;
}

string unitCell::getMo() const {
	return Mo;
}

vector<Coord> unitCell::getCoords() const {
	return Unit_Coords;
}

void unitCell::setS1(string new_S) {
	this-> S1 = new_S;
}

void unitCell::setS2(string new_S) {
	this-> S2 = new_S;
}

void unitCell::setMo(string new_Mo) {
	this-> Mo = new_Mo;
}

void unitCell::setCoords(vector<Coord> new_Coords) {
	this-> Unit_Coords = new_Coords;
}

template <class T>
void Cells<T>::push(T const & unitCell) {
	this->unitCells.push_back(unitCell);
}

template <class T>
void Cells<T>::pop() {
	if (this->unitCells.empty()) {

	} else {
		this->unitCells.pop_back();
	}
}

template <class T>
T Cells<T>::top() {
	if (this->unitCells.empty()) {

	} else {
		return this->unitCells.back();
	}
}

template <class T>
bool Cells<T>::empty() {
	return this->unitCells.empty();
}

int main(int argc, char ** argv) {
	int opt;
	string in_f_name;
	string out_f_name;
	ifstream inFile;
	ofstream outFile;
	vector<string> filedata;
	string lineString;
	string chemical;
	//regex name_regex("Atoms");
	//smatch name_match;

	if (argc != 7) {
		cerr << "Error: Invalid number of arguments" << endl;
		cout << "Usage: ./Structure -i <inputfile> -o <outfile> -n <name_of_chemical>" << endl;
		exit(EXIT_FAILURE);
	}

	while ((opt = getopt(argc, argv, "i:o:n:")) != EOF) {
		switch(opt) {
			case 'i':
				in_f_name = optarg;
				break;
			case 'o':
				out_f_name = optarg;
				break;
			case 'n':
				chemical = optarg;
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
		//outFile << lineString << endl;
		if ( (int)lineString.length()  > 0 ){
			filedata.push_back(lineString);
		} 
		//cout << regex_search(lineString,name_match,name_regex) << endl;
	}

	//for (int i = 0; i< (int) filedata.size(); ++i) {
	//	if ( (int) filedata[i].length() == 0) {
			//cout << filedata[i].length << endl;
		//}
	//}

	for (const auto& line : filedata) {
		//regex_match(line,name_match,name_regex);
		if (line.find("atoms") <  line.length()) {
			outFile << line.substr(0, line.find("atoms")-1) << endl;
			outFile << chemical << endl;
			break;
		} else {
			continue;
		}
	}


	string section = "Atoms";
	string bonds = "Bonds";
	size_t apos = 0;
	size_t bpos = 0;
	for(vector<string>::iterator it(filedata.begin()), end(filedata.end()); it!=end; it++) {
		//cout << *it << endl;
		if (*it == "Atoms") {
			size_t pos = find(filedata.begin(), filedata.end(), section) -filedata.begin();
			if (pos >= filedata.size()) {
				break;
			} else {
				apos = pos;
			}
		}
		if (*it == "Bonds") {
			size_t pos = find(filedata.begin(), filedata.end(), bonds) -filedata.begin();
			if (pos >= filedata.size()) {
				break;
			} else {
				bpos = pos;
			}
		}
	}

	auto it = filedata.begin(), end = filedata.end();
	int atomIndex, atomIndicator, knot, knot2;
	double x,y,z;
	string Mo = "Mo";
	string S = "S";
	vector<Coord> myCoords;
	unitCell myCell = unitCell("S","S","Mo",myCoords);
	for (; it != end; ++it) {
		if (distance(filedata.begin(), it) > (ptrdiff_t) apos &&
			distance(filedata.begin(), it) < (ptrdiff_t) bpos) {
			const char* thisline = (*it).c_str();
			sscanf(thisline, "%d %d %lf %lf %lf %d %d", &atomIndex, &atomIndicator, &x,&y,&z, &knot, &knot2);
			if (atomIndicator == 1) {
				cout << myCell.getMo() << endl;
				outFile << Mo << " " << x << " " << y << " " << z << " " << endl;
			} else {
				outFile << S << " " << x << " " << y << " " << z << " " << endl;
			}
		}
	}

	inFile.close();
	outFile.close();


	return 0;
}
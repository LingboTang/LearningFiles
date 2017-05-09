#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

typedef struct Coord {
	int X;
	int Y;
	int Z;
} Coord;

class unitCell {

private:
	string S1;
	string S2;
	string Mo;
	vector<Coord> Unit_Coords; 
public:
	// Constructor
	unitCell(string S1, string S2, string Mo, vector<Coord> my_Coords);
	// Destructor
	~unitCell();
	// Copy Constructor
	unitCell(const unitCell &rhs);
	// Assignment Operator
	unitCell &operator= (const unitCell &rhs);
	// Getters
	string getS1() const;
	string getS2() const;
	string getMo() const;
	vector<Coord> getCoords() const;
	// Setters
	void setS1(string new_S);
	void setS2(string new_S);
	void setMo(string new_Mo);
	void setCoords(vector<Coord> new_Coords);
};

/*template <class T>
class Cells
{

private:
	vector<T> unitCells;
public:
	push

}*/
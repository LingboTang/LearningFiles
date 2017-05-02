#ifndef LList_h
#define LList_h

#include <iostream>
#include <string>
using namespace std;

struct node
{
	string value;
	node * next;
}

class LList
{
private:
	node *head;
	int length;
	
public:
	LList()

	void insertNode(node *newNode, int position)
	
	void removeNode(int position);

	void printList();
	
	~LList();
	
}

#endif

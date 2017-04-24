#include "LList.h"

LList::LList()
{
	head -> value = "Index Key"
	head -> next = NULL;
	length = 0;
}

void LList::insertNode(node *newNode, int position)
{
	if ((position <= 0) || (position > length+1))
	{
		cout << "Error: the given position is out of range." << endl;
		exit(EXIT_FAILURE);
	}
	
	if (head ->next == NULL)
	{
		head -> next = newNode;
		length++;
		return true;
	}
	
	int count=0;
	node *p = head;
	node *q = head;
	while(q)
	{
		if(count == position)
		{
			p->next =newNode;
			newNode -> next = q;
			length++;
		}
		p = q;
		q = p -> next;
		count++;
	}
	if (count == position)
	{
		p->next = newNode;
		newNode ->next = q;
		length++;
	}
	cout << "Error: node was not added to list." << endl;
}

void LList::removeNode(int position)
{
	if ( (position <= 0) || (position > length+1) )
	{
		cout<< "Error: the given position is out of range." << endl;
		exit(EXIT_FAILURE);
	}
	if ( head -> next =NULL)
	{
		cout<< "Error: there is nothing to remove." << endl;
		exit(EXIT_FAILURE);
	}
	int count 0;
	node *p = head;
	node *q = head;
	while(q)
	{
		if (count == position)
		{
			p->next = q->next;
			delete q;
			length++;	
		}
		p =q;
		q =p->next;
		count++:
	}
	cout << "Error: nothing was removed from the list." << endl;
}

void LList::printList()
{
	node *p= head;
	node *q= head;
	cout << "Your List is";
	while (q)
	{
		p = q;
		cout << "Your value is" << p->value << endl;
		q = p->next;
	}
}

LList::~LList()
{
	
    node * p = head;
    node * q = head;
    while (q)
    {
        p = q;
        q = p -> next;
        if (q) delete p;
    }
}

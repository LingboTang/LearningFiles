#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

struct node 
{
	int val;
	struct node *next;
};

struct node * insert(struct node *head, int num)
{
	struct node *p = (struct node *) calloc(sizeof(struct node));

	p->val = num;
	p->next = head;

	return p;
}

void bfs(struct node *list[], int vertices, int * parent, int *level)
{
	struct node * temp;
	int i, par, lev, flag =1;

	lev = 0;
	level[1] = lev;

	while (flag) {
		flag = 0;
		for (i = 1; i<= vertices; ++i) {
			if (level[i] == lev) {
				flag = 1;
				temp
			}
		}
	}
}
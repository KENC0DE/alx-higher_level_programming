#include "lists.h"

/**
 * check_cycle - check for loop in a single linked list.
 * @list: the linked list.
 *
 * Return: 0 for loop no cycle 1 for cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *flash = list;
	listint_t *snail = list;

	while (flash && flash->next)
	{
		flash = flash->next->next;
		snail = snail->next;

		if (flash == snail)
			return (1);		
	}
	return (0);
}


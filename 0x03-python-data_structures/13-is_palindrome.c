#include "lists.h"

/**
 * is_palindrome - check weather is palindrom or not
 * @head: passed linked list head.
 *
 * Return: 0 for not palindrom. and 1 for palindrom.
*/
int is_palindrome(listint_t **head)
{
	listint_t *back, *front;

	if (!head)
		return (-1);
	else if (!(*head))
		return (1);

	back = *head;
	front = *head;
	while (front)
	{
		if (front->next->next == NULL)
		{
			if (back->n == front->next->n)
			{
				front->next = NULL;
				back = back->next;
				front = back;
			}
			else
				return (0);
		}
		front = front->next;
	}
	return (1);
}


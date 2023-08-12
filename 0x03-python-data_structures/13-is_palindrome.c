#include "lists.h"

/**
 * count - counts list length
 * @lis: the list.
 *
 * Return: the lenght.
*/
int count(listint_t *lis)
{
	listint_t *tp = lis;
	int len = 0;

	while (tp)
	{
		tp = tp->next;
		len++;
	}
	return (len);
}

/**
 * dp_half - for half use
 * @head: the head of a linked list.
 * @len: the length.
 *
 * Return: double pointer.
*/
listint_t **dp_half(listint_t *head, int len)
{
	listint_t *tp, **front;
	int i;

	front = malloc(sizeof(listint_t *) * len);
	tp = head;
	i = 0;
	while (tp)
	{
		front[i] = tp;
		tp = tp->next;
		i++;
	}
	front[len] = NULL;
	return (front);
}
/**
 * is_palindrome - check weather is palindrom or not
 * @head: passed linked list head.
 *
 * Return: 0 for not palindrom. and 1 for palindrom.
*/
int is_palindrome(listint_t **head)
{
	listint_t *back, **front;
	int len = 0, half, i;

	if (!head)
		return (-1);
	else if (!(*head))
		return (1);

	len = count(*head);
	front = dp_half(*head, len);

	if (len % 2 != 0)
		half = (len / 2) + 1;
	else
		half = len / 2;
	back = *head;
	for (i = len - 1; i >= half; i--)
	{
		if (back->n != front[i]->n)
		{
			free(front);
			return (0);
		}
		back = back->next;
	}
	free(front);
	return (1);
}


#include "lists.h"

/**
 * check_pali - check for palindrom.
 * @head: head of list.
 * @len: the lenght.
 * Return: 0 or 1.
*/
int check_pali(listint_t *head, int len)
{
	listint_t *tp;
	int *nums = malloc(sizeof(int) * (len / 2));
	int i, half, st_check = 0;

	half = len / 2;
	i = 0, tp = head;
	while (tp)
	{
		if (i < half && !st_check)
		{
			nums[i] = tp->n;
			i++;
		}
		if (i == half)
		{
			st_check = 1;
			if (len % 2 == 0)
				tp = tp->next;
			else
				tp = tp->next->next;
			i--;
		}

		if (st_check)
		{
			if (nums[i] != tp->n)
			{
				free(nums);
				return (0);
			}
			i--;
		}
		tp = tp->next;
	}
	free(nums);
	return (1);
}

/**
 * is_palindrome - check weather is palindrom or not
 * @head: passed linked list head.
 *
 * Return: 0 for not palindrom. and 1 for palindrom.
*/
int is_palindrome(listint_t **head)
{
	listint_t *tp, *pre = *head;
	int len = 0;

	if (!head)
		return (-1);
	else if (!(*head))
		return (1);
	else if (pre->next == NULL)
		return (1);

	tp = *head;
	while (tp)
	{
		tp = tp->next;
		len++;
	}

	return (check_pali(*head, len));
}


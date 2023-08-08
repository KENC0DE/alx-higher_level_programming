#include "lists.h"

/**
 * check_cycle - check for loop in a single linked list.
 * @list: the linked list.
 *
 * Return: 0 for loop no cycle 1 for cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *tp = list;
	p_s *cnst, *prs;
	p_s *check = malloc(sizeof(p_s));

	if (!check)
		return (-1);

	cnst = check;
	check->p = (void *)tp;
	check->next = NULL;

	while (tp->next)
	{
		prs = cnst;
		while (prs)
		{
			if (prs->p == tp->next)
			{
				free_p(cnst);
				return (1);
			}
			prs = prs->next;
		}
		tp = tp->next;
		check->next = malloc(sizeof(p_s));
		if (!check->next)
			return (-1);

		check = check->next;
		check->p = tp;
		check->next = NULL;
	}
	free_p(cnst);
	return (0);
}

/**
 * free_p - frees a p_s list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_p(p_s *head)
{
	p_s *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}


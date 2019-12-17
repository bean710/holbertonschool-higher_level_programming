#include "lists.h"

int is_palindrome(listint_t **head)
{
	int len = 0, i, j;
	listint_t *tmp, *cmp;

	if (!head || !*head)
		return (1);

	for (tmp = *head; tmp; tmp = tmp->next, ++len)
		;

	for (i = 0, tmp = *head; i < len / 2; ++i, tmp = tmp->next)
	{
		for (cmp = tmp, j = 0; j < len - (i * 2) - 1; j++, cmp = cmp->next)
			;

		if (cmp->n != tmp->n)
			return (0);
	}

	return (1);
}

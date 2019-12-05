#include "lists.h"

/**
 * check_cycle - Detect a loped linked list
 * @list: list head
 *
 * Return: 0 false, 1 true
 */
int check_cycle(listint_t *list)
{
listint_t *current, *verify;

	current = list;
	verify = list;
	while (current != NULL && verify != NULL && verify->next != NULL)
	{
		current = current->next;
		verify = verify->next->next;
		if (current == verify)
			return (1);
	}

	return (0);
}

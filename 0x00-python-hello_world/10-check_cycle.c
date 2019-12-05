#include "lists.h"

int check_cycle(listint_t *list)
{
listint_t *current, *verify;

	current = list;
	while (current != NULL)
	{
		if (current->next != NULL)
		{
			verify = current->next;
			do {
				if (verify == current)
					return (1);
				verify = verify->next;
			} while (verify != NULL);
		}

		current = current->next;
	}

	return (0);
}

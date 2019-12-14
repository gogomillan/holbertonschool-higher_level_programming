#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
int *list;
long go = 1, i;
listint_t *forw;

	if (head == NULL)
		return (1);
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);

	forw = *head;
	while (forw->next != NULL)
		forw = forw->next, go++;
	list = malloc(go * sizeof(int));
	if (!list)
		return (0);
	forw = *head, go = 0;
	while (forw != NULL)
		list[go] = forw->n, forw = forw->next, go++;

	for (i = 0; i < (go / 2); i++)
	{
		if (list[i] != list[go - i - 1])
		{	free(list);
			return (0);
		}
	}
	free(list);

	return (1);
}

#include "lists.h"

/**
 * insert_node - adds a new node in ordered way in listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current, *prev, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	current = *head;
	prev = current;
	new->n = number;

	if (*head == NULL || current->n > number)
	{
		new->next = *head, *head = new;
		return (new);
	}

	while (current != NULL)
	{
		if (current->n > number)
		{
			prev->next = new, new->next = current;
			return (new);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new, new->next = NULL;

	return (new);
}

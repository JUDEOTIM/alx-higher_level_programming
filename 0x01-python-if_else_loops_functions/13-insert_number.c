#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *next, *new;

	curr = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (!curr || curr->n >= number)
	{
		new->next = curr;
		*head = new;
		return (new);
	}
	next = curr->next;
	while (next && next->n < number)
	{
		curr = curr->next;
		next = next->next;
	}
	new->next = next;
	curr->next = new;

	return (new);
}

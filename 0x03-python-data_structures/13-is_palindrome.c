#include "lists.h"

/**
 * rev_listint - Reverses a singly linked list.
 * @head: A pointer to the head of a linked list.
 *
 * Return: A pointer to the head of the reversed list
 *	   O/w - NULL.
 */
listint_t *rev_listint(listint_t **head)
{
	listint_t *prev = NULL, *next;

	if (!head || !(*head))
		return (NULL);

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;

	}
	*head = prev;

	return (*head);
}
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *rev_copy;
	int len = 0, i, mid;

	if (!(*head) || !(*head)->next)
		return (1);

	tmp = *head;
	while (tmp)
	{
		len++;
		tmp = tmp->next;
	}

	mid = len/2;
	tmp = *head;
	for (i = 1; i < mid; i++)
		tmp = tmp->next;
	if (tmp->n != tmp->next->n && (len % 2 == 0))
		return (0);

	tmp = tmp->next->next;
	rev = rev_listint(&tmp);
	rev_copy = rev;

	tmp = *head;
 	while (rev)
	{
		if (rev->n != tmp->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	rev_listint(&rev_copy);

	return (1);	
}

#include "lists.h"
#include <stdlib.h>

/**
 *insert_node - Inserts number to a sorted linked list.
 *@head: A ptr to the head of the sorted linked list.
 *@number: The value to insert into the list.
 *
 *Description:
 *This function inserts a new node with the specified value into a sorted
 *singly-linked list while maintaining the list's sorted order.
 *
 *Return: If memory allocation fails or if head is NULL - returns NULL.
 *Otherwise - returns a pointer to the newly inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current && current->next && current->next->n < number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}

#include "lists.h"
/*
 * check_cycle - check if list contains cycle
 * @list: lists to check
 * Return: 1 if list has cycle and 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *runner = list;

	while(current && runner && runner ->next)
	{
		current = current->next;
		runner = runner->next->next;

		if (current == runner)
			return (1);
	}
	return(0);
}

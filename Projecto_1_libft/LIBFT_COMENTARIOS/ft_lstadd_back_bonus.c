/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back_bonus.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/14 12:32:15 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:52:12 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*last;

	if (*lst == NULL)
	{
		*lst = new;
	}
	else
	{
		last = *lst;
		while (last->next != NULL)
			last = last->next;
		last->next = new;
	}
}

/* int main()
{
	t_list *node1 = malloc(sizeof(t_list));
	t_list *node2 = malloc(sizeof(t_list));
	t_list *node3 = malloc(sizeof(t_list));

	int content1 = 10;
	int content2 = 20;
	int content3 = 30;

	node1->content = &content1;
	node1->next = NULL;

	node2->content = &content2;
	node2->next = NULL;

	node3->content = &content3;
	node3->next = NULL;

	t_list *list = NULL;

	ft_lstadd_back(&list, node1);
	ft_lstadd_back(&list, node2);
	ft_lstadd_back(&list, node3);

	printf("Contenido de la lista:\n");
	t_list *current = list;
	while (current != NULL)
	{
		printf("%d\n", *(int *)current->content);
		current = current->next;
	}
	free(node1);
	free(node2);
	free(node3);

	return (0);
}
 */

//DESCRIPCION. Añade el nodo ’new’ al final de la lista ’lst’.
//PARAMETROS
//lst: el puntero al primer nodo de una lista.
//new: el puntero a un nodo que añadir a la lista.

/* void ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list *last;

	// Si la lista está vacía, el nuevo elemento se convierte en el primer 
	y único elemento de la lista
	if (*lst == NULL)
	{
		*lst = new;  // Asigna el nuevo elemento como la cabeza de la lista
	}
	else
	{
		last = *lst;  // Inicializa last al primer elemento de la lista
		
		// Recorre la lista hasta encontrar el último elemento
		while (last->next != NULL)
			last = last->next;
		
		// Una vez encontrado el último elemento, enlaza el nuevo elemento 
		como el siguiente
		last->next = new;
	}
} */
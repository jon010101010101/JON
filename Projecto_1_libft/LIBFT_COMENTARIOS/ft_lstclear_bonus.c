/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/14 12:55:08 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:54:00 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void*))
{
	t_list	*current;
	t_list	*next;

	if (!lst || !*lst || !del)
		return ;
	current = *lst;
	while (current)
	{
		next = current->next;
		del(current->content);
		free(current);
		current = next;
	}
	*lst = NULL;
}
/* void	del_string(void *content)
{
	free(content);
}

int main(void)
{
	char *content;
	
	t_list *node = malloc(sizeof(t_list));
	
	content = strdup("Hello, Maryann!");
	node->content = content;
	node->next = NULL;

	ft_lstdelone(node, &del_string);

	printf("Node and its content have been successfully deleted.\n");

	return (0);
} */
/*
DESCRIPCION: Elimina y libera el nodo ’lst’ dado y todos los
consecutivos de ese nodo, utilizando la función
’del’ y free(3). Al final, el puntero a la lista debe ser NULL.

PARAMETROS:
lst: la dirección de un puntero a un nodo.
del: un puntero a función utilizado para eliminar
el contenido de un nodo.
*/

/* // Función que elimina todos los elementos de una lista enlazada
void ft_lstclear(t_list **lst, void (*del)(void*))
{
	t_list *current; // Puntero para recorrer la lista
	t_list *next;    // Puntero para guardar el siguiente nodo

	// Si la lista, el primer elemento o la función 'del' son NULL, no se
	 hace nada y se retorna
	if (!lst || !*lst || !del)
		return;

	// Inicializa 'current' apuntando al primer elemento de la lista
	current = *lst;

	// Recorre la lista mientras 'current' no sea NULL
	while (current)
	{
		// Guarda el siguiente nodo
		next = current->next;

		// Llama a la función 'del' para liberar el contenido del nodo actual
		del(current->content);

		// Libera la memoria del nodo actual
		free(current);

		// Avanza al siguiente nodo
		current = next;
	}

	// Finalmente, establece el puntero de inicio de la lista a NULL
	*lst = NULL;
} */
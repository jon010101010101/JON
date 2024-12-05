/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/14 12:39:52 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 16:36:17 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdelone(t_list *lst, void (*del)(void*))
{
	if (lst != NULL)
	{
		if (del != NULL)
			del(lst->content);
		free(lst);
	}
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
DESCRIPCION. Toma como parámetro un nodo ’lst’ y libera la
memoria del contenido utilizando la función ’del’
dada como parámetro, además de liberar el nodo. La
memoria de ’next’ no debe liberarse.

PARAMETROS. 
lst: el nodo a liberar.
del: un puntero a la función utilizada para liberar
el contenido del nodo.
*/

/* // Función que elimina un nodo de una lista enlazada
void ft_lstdelone(t_list *lst, void (*del)(void*))
{
	// Comprueba si el nodo 'lst' no es NULL
	if (lst != NULL)
	{
		// Comprueba si la función 'del' no es NULL
		if (del != NULL)
			// Llama a la función 'del' para liberar el contenido del nodo
			del(lst->content);

		// Libera la memoria del nodo
		free(lst);
	}
} */
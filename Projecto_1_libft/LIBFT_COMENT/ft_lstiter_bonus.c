/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/14 12:57:23 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:42:22 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	t_list	*current;

	if (!lst || !f)
		return ;
	current = lst;
	while (current)
	{
		f(current->content);
		current = current->next;
	}
}

/* void	print_content(void *content)
{
	printf("%s\n", (char *)content);
}

int	main(void)
{
	t_list list1 = {"content1", NULL};
	t_list list2 = {"content2", NULL};
	t_list list3 = {"content3", NULL};
	t_list list4 = {"content4", NULL};

	list1.next = &list2;
	list2.next = &list3;
	list3.next = &list4;

	t_list *lst = &list1;

	ft_lstiter(lst, print_content);

	return (0);
} */
/*
DESCRIPCION.Itera la lista ’lst’ y aplica la función ’f’ en el
contenido de cada nodo.

PARAMETROS.
lst: un puntero al primer nodo.
f: un puntero a la función que utilizará cada nodo.
*/

/* // Función que aplica una función dada a cada elemento de una lista enlazada
void ft_lstiter(t_list *lst, void (*f)(void *))
{
	t_list *current; // Declaración de un puntero para recorrer la lista

	// Comprueba si el puntero a la lista 'lst' o la función 'f' son NULL
	if (!lst || !f)
		return; // Si 'lst' o 'f' son NULL, no se hace nada y se retorna de la 
		función

	// Inicializa 'current' apuntando al primer elemento de la lista
	current = lst;

	// Recorre la lista mientras 'current' no sea NULL
	while (current)
	{
		// Aplica la función 'f' al contenido del nodo actual
		f(current->content);

		// Avanza al siguiente nodo de la lista
		current = current->next;
	}
} */
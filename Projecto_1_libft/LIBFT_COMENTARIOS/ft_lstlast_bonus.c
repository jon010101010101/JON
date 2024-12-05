/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 19:07:12 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 11:09:55 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (lst == NULL)
		return (NULL);
	while (lst->next != NULL)
		lst = lst->next;
	return (lst);
}
/* 
int main()
{
	// Creación de las cuatro listas
	t_list *list1 = (t_list *)malloc(sizeof(t_list));
	t_list *list2 = (t_list *)malloc(sizeof(t_list));
	t_list *list3 = (t_list *)malloc(sizeof(t_list));
	t_list *list4 = (t_list *)malloc(sizeof(t_list));
	t_list *fortydos = (t_list *)malloc(sizeof(t_list));
	// Asignación de contenido para las cuatro listas (para demostración)
	list1->content = "Lista 1";
	list2->content = "Lista 2";
	list3->content = "Lista 3";
	list4->content = "Lista 4";
	fortydos->content = "Forty Dos";

	t_list *last = fortydos;

	last->next = list1;
	last = ft_lstlast(fortydos);
	last->next = list2;
	last = ft_lstlast(fortydos);
	last->next = list3;
	last = ft_lstlast(fortydos);
	last->next = list4;

	printf("El ultimo de la lista es: ");
	t_list *current = fortydos;
	while (current != NULL)
	{
		printf("%s \n ", (char *)current->content);
		current = current->next;
	}
	return (0);
}
 */

/* // Función que devuelve el último nodo de una lista enlazada
t_list *ft_lstlast(t_list *lst)
{
	// Comprueba si la lista está vacía
	if (lst == NULL)
		return (NULL); // Si la lista está vacía, retorna NULL

	// Recorre la lista hasta encontrar el último nodo
	while (lst->next != NULL)
		lst = lst->next; // Avanza al siguiente nodo de la lista

	// Retorna el último nodo encontrado
	return (lst);
} */
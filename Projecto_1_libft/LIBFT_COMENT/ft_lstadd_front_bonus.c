/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 17:59:48 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:42:09 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (new == NULL)
		return ;
	new->next = *lst;
	*lst = new;
}

/* int main()
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

	t_list *first = fortydos;

	ft_lstadd_front(&fortydos, list1);
	ft_lstadd_front(&fortydos, list2);
	ft_lstadd_front(&fortydos, list3);
	ft_lstadd_front(&fortydos, list4);

	// Imprimir la lista fortydos
	printf("La lista fortydos es: ");
	t_list *current = first;
	while (current != NULL)
	{
		printf("%s \n ", (char *)current->content);
		current = current->next;
	}
	return (0);
} */

/* void ft_lstadd_front(t_list **lst, t_list *new)
{
	// Comprueba si el nuevo elemento es NULL
	if (new == NULL)
		return ; // Si 'new' es NULL, no se hace nada y se retorna de la función

	// Establece el puntero 'next' del nuevo elemento para que apunte al primer 
	elemento actual de la lista new->next = *lst;

	// Actualiza el puntero de inicio de la lista para que apunte al nuevo 
	elemento *lst = new;
} */
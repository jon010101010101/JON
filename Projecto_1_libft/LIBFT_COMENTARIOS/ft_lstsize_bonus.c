/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 18:29:55 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 11:13:46 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	int	count;

	count = 0;
	while (lst)
	{
		lst = lst->next;
		count++;
	}
	return (count);
}
/* 
int main()
{
	t_list *list1 = (t_list *)malloc(sizeof(t_list));
	t_list *list2 = (t_list *)malloc(sizeof(t_list));
	t_list *list3 = (t_list *)malloc(sizeof(t_list));
	t_list *list4 = (t_list *)malloc(sizeof(t_list));

	list1->next = list2;
	list2->next = list3;
	list3->next = list4;
	list4->next = NULL;
	int	prueba = ft_lstsize(list2);

	printf("El numero de nodos es: %d\n", prueba);
	return (0);
	
} 
*/

/* // Función que cuenta el número de nodos en una lista enlazada
int ft_lstsize(t_list *lst)
{
	int count; // Variable para almacenar el número de nodos

	// Inicializa el contador en 0
	count = 0;

	// Recorre la lista mientras 'lst' no sea NULL
	while (lst)
	{
		// Avanza al siguiente nodo de la lista
		lst = lst->next;

		// Incrementa el contador en 1
		count++;
	}
 */
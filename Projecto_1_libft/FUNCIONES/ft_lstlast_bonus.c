/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 19:07:12 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 18:45:14 by jurrutia         ###   ########.fr       */
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
	t_list *list1 = (t_list *)malloc(sizeof(t_list));
	t_list *list2 = (t_list *)malloc(sizeof(t_list));
	t_list *list3 = (t_list *)malloc(sizeof(t_list));
	t_list *list4 = (t_list *)malloc(sizeof(t_list));
	t_list *fortytwo = (t_list *)malloc(sizeof(t_list));

	list1->content = "Lista 1";
	list2->content = "Lista 2";
	list3->content = "Lista 3";
	list4->content = "Lista 4";
	ffortytwo->content = "Fortytwo";

	t_list *last = fortytwo;

	last->next = list1;
	last = ft_lstlast(fortytwo);
	last->next = list2;
	last = ft_lstlast(fortytwo);
	last->next = list3;
	last = ft_lstlast(fortytwo);
	last->next = list4;

	printf("El ultimo de la lista es: ");
	t_list *current = fortytwo;
	while (current != NULL)
	{
		printf("%s \n ", (char *)current->content);
		current = current->next;
	}
	return (0);
}
 */

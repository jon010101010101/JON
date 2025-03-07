/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 19:07:12 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 12:01:04 by jurrutia         ###   ########.fr       */
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

/* int main(void)
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
	fortytwo->content = "Fortytwo";

	t_list *last = fortytwo;

	last->next = list1;
	last = ft_lstlast(fortytwo);
	last->next = list2;
	last = ft_lstlast(fortytwo);
	last->next = list3;
	last = ft_lstlast(fortytwo);
	last->next = list4;

	printf("The last one on the list is: ");
	t_list *current = fortytwo;
	while (current != NULL)
	{
		printf("%s \n ", (char *)current->content);
		current = current->next;
	}
	return (0);
} */

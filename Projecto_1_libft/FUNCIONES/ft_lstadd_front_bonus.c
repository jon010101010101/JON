/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front_bonus.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 17:59:48 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/17 18:48:26 by jurrutia         ###   ########.fr       */
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
	t_list *first;
	
	t_list *list1 = (t_list *)malloc(sizeof(t_list));
	t_list *list2 = (t_list *)malloc(sizeof(t_list));
	t_list *list3 = (t_list *)malloc(sizeof(t_list));
	t_list *list4 = (t_list *)malloc(sizeof(t_list));
	t_list *fortytwo = (t_list *)malloc(sizeof(t_list));
	
	list1->content = "Lista 1";
	list2->content = "Lista 2";
	list3->content = "Lista 3";
	list4->content = "Lista 4";
	fortytwo->content = "firstfortytwo";

	first = fortytwo;

	ft_lstadd_front(&fortytwo, list1);
	ft_lstadd_front(&fortytwo, list2);
	ft_lstadd_front(&fortytwo, list3);
	ft_lstadd_front(&fortytwo, list4);

	printf("fortytwo list is: ");
	t_list *current = first;
	while (current != NULL)
	{
		printf("%s \n ", (char *)current->content);
		current = current->next;
	}
	return (0);
} */

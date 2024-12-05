/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear_bonus.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/14 12:55:08 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/17 18:53:04 by jurrutia         ###   ########.fr       */
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

/* void delete_string(void *content)
{
	
}

int main()
{
	t_list *node1 = (t_list *)malloc(sizeof(t_list));
	t_list *node2 = (t_list *)malloc(sizeof(t_list));
	t_list *node3 = (t_list *)malloc(sizeof(t_list));

	node1->content = "Hello";
	node2->content = "Maryann";
	node3->content = "!";

	node1->next = node2;
	node2->next = node3;
	node3->next = NULL;

	t_list *list = node1;

	ft_lstclear(&list, delete_string);

	if (list == NULL)
	{
		printf("The list has been released successfully.\n");
	}
	else
	{
		printf("Error: The list was not released correctly.\n");
	}

	return 0;
} */
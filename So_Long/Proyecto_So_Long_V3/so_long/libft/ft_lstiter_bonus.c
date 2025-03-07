/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/14 12:57:23 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 11:24:06 by jurrutia         ###   ########.fr       */
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
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 17:06:10 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 11:29:51 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list	*lst;

	lst = malloc(sizeof(t_list));
	if (!lst)
		return (NULL);
	lst->content = content;
	lst->next = NULL;
	return (lst);
}

/* int main(void)
{
	char	*content = "abcdefg";

	t_list	*printc = ft_lstnew(content);
		
	if (printc != NULL)
	{
		printf("The list is: %s\n", (char *)printc->content);
		free(printc);
	}
	else
	{
		printf("Error: Unable to create a new list node.\n");
	}
	return (0);
} */

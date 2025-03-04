/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone_bonus.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/14 12:39:52 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/20 11:23:01 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstdelone(t_list *lst, void (*del)(void*))
{
	if (lst != NULL)
	{
		if (del != NULL)
			del(lst->content);
		free(lst);
	}
}

/* void	del_string(void *content)
{
	free(content);
}

int main(void)
{
	char *content;
	
	t_list *node = malloc(sizeof(t_list));
	
	content = strdup("Hello, Maryann!");
	node->content = content;
	node->next = NULL;

	ft_lstdelone(node, &del_string);

	printf("Node and its content have been successfully deleted.\n");

	return (0);
} */
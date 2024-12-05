/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize_bonus.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 18:29:55 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 18:52:26 by jurrutia         ###   ########.fr       */
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

	printf("the number of nodes is: %d\n", prueba);
	return (0);
	
} 
*/

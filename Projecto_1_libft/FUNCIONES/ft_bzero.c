/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/15 13:07:51 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/16 18:25:48 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	char	*p;
	size_t	i;

	p = (char *)s;
	i = 0;
	while (i < n)
	{
		*p = '\0';
		p++;
		i++;
	}
}
/* 
int main(void)
{
	char str[10] = "pepe";

	ft_bzero(str, sizeof(str)); 
	printf("string size: %lu\n", sizeof(str));
	printf("string content: %s\n", str);

	return (0);
}
 */

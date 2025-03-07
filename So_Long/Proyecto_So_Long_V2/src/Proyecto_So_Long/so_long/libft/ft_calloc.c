/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 20:14:04 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/27 19:02:36 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	size_t	total_size;
	void	*ptr;

	total_size = count * size;
	ptr = malloc(total_size);
	if (ptr == NULL)
		return (NULL);
	ft_bzero(ptr, total_size);
	return (ptr);
}

/* int main(void)
{
	int *array;
	int length = 15;	
	int i;

	array = (int *)ft_calloc(length, sizeof(int));

	if (array == NULL)
	{
		printf("Memory allocation has failed.\n");
		return (1);
	}
	i = 0;
	 while (i < length)
	{
		printf("%d ", array[i]);
		i++;
	}
	printf("\n");

	free(array);

	return (0);
} */

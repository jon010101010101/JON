/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/19 12:07:34 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/22 10:20:18 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*handle_zero_case(void)
{
	char	*result_zero;

	result_zero = (char *)malloc(2 * sizeof(char));
	if (result_zero == 0)
		return (NULL);
	result_zero[0] = '0';
	result_zero[1] = '\0';
	return (result_zero);
}

void	extract_sign_and_number(int n, int *sign, long long *num)
{
	if (n < 0)
	{
		*sign = -1;
		*num = -(long long)n;
	}
	else
	{
		*sign = 1;
		*num = n;
	}
}

char	*convert_number_to_str(long long num, int size, int sign)
{
	char	*result;

	result = (char *)malloc((size + 1) * sizeof(char));
	if (result == NULL)
		return (NULL);
	result[size] = '\0';
	while (size > 0)
	{
		result[size - 1] = num % 10 + '0';
		num = num / 10;
		size--;
	}
	if (sign == -1)
		result[0] = '-';
	return (result);
}

char	*ft_itoa(int n)
{
	int			sign;
	long long	num;
	int			size;
	long long	temp;

	if (n == 0)
		return (handle_zero_case());
	extract_sign_and_number(n, &sign, &num);
	size = 0;
	temp = num;
	while (temp > 0)
	{
		temp = temp / 10;
		size++;
	}
	if (sign == -1)
		size++;
	return (convert_number_to_str(num, size, sign));
}

/* int	main(void)
{
	int		num;
	char	*str;

	num = 2147483647;
	str = ft_itoa(num);
	if (str != NULL)
	{
		printf("Number: %d, String: %s\n", num, str);
		free(str);
	}
	num = -2147483648;
	str = ft_itoa(num);
	if (str != NULL)
	{
		printf("Number: %d, String: %s\n", num, str);
		free(str);
	}
	return (0);
} */

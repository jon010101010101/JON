/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 10:03:48 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/27 18:54:22 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	count_words(char const *s, char c)
{
	int	count;
	int	in_word;

	count = 0;
	in_word = 0;
	while (*s)
	{
		if (*s != c && !in_word)
		{
			count++;
			in_word = 1;
		}
		else if (*s == c)
		{
			in_word = 0;
		}
		s++;
	}
	return (count);
}

static char	*next_word(char const **s, char c)
{
	const char	*word_start;
	const char	*word_end;
	char		*new_word;

	word_start = *s;
	while (*word_start == c)
		word_start++;
	if (*word_start == '\0')
		return (NULL);
	word_end = word_start;
	while (*word_end != c)
		word_end++;
	if (word_end == word_start)
		return (NULL);
	new_word = ft_substr(word_start, 0, word_end - word_start);
	if (!new_word)
		return (NULL);
	*s = word_end;
	return (new_word);
}

char	**ft_split(char const *s, char c)
{
	char	**result;
	int		num_words;
	int		i;

	if (!s)
		return (NULL);
	num_words = count_words(s, c);
	result = (char **)malloc((num_words + 1) * sizeof(char *));
	if (!result)
		return (NULL);
	i = 0;
	while (i < num_words)
	{
		result[i] = next_word(&s, c);
		if (!result[i])
		{
			while (i--)
				free(result[i]);
			free(result);
			return (NULL);
		}
		i++;
	}
	result[i] = NULL;
	return (result);
}

/* int	main(void)
{
	char const	*s = "Hello Maryann this is a test again";
	char		c;
	char		**result;
	int			i;

	i = 0;
	c = ' ';
	result = ft_split(s, c);
	if (result != NULL)
	{
		while (result[i] != NULL)
		{
			printf("Word %d: %s\n", i + 1, result[i]);
			free(result[i]);
			i++;
		}
		free(result);
	}
	else
		printf("Error: Could not split string.\n");
	return (0);
} */

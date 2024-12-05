/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/28 18:04:50 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/12 17:36:05 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_free(char **str)
{
	free(*str);
	*str = NULL;
	return (NULL);
}

char	*clean_box(char *box)
{
	char	*new_box;
	char	*ptr;
	int		len;

	ptr = ft_strchr(box, '\n');
	if (!ptr)
	{
		new_box = NULL;
		return (ft_free(&box));
	}
	else
		len = (ptr - box) + 1;
	if (!box[len])
		return (ft_free(&box));
	new_box = ft_substr(box, len, ft_strlen(box) - len);
	ft_free(&box);
	if (!new_box)
		return (NULL);
	return (new_box);
}

char	*new_line(char *box)
{
	char	*line;
	char	*ptr;
	int		len;

	ptr = ft_strchr(box, '\n');
	len = (ptr - box) + 1;
	line = ft_substr(box, 0, len);
	if (!line)
		return (NULL);
	return (line);
}

char	*read_box(int fd, char *new_box)
{
	int		read_it;
	char	*temp_box;

	read_it = 1;
	temp_box = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!temp_box)
		return (ft_free(&new_box));
	temp_box[0] = '\0';
	while (read_it > 0 && !ft_strchr(temp_box, '\n'))
	{
		read_it = read(fd, temp_box, BUFFER_SIZE);
		if (read_it > 0)
		{
			temp_box[read_it] = '\0';
			new_box = ft_strjoin(new_box, temp_box);
		}
	}
	free(temp_box);
	if (read_it == -1)
		return (ft_free(&new_box));
	return (new_box);
}

char	*get_next_line(int fd)
{
	static char	*new_box = NULL;
	char		*line;

	if (fd < 0)
		return (NULL);
	if ((new_box && !ft_strchr(new_box, '\n')) || !new_box)
		new_box = read_box(fd, new_box);
	if (!new_box)
		return (NULL);
	line = new_line(new_box);
	if (!line)
		return (ft_free(&new_box));
	new_box = clean_box(new_box);
	return (line);
}

#define GREEN "\033[0;32m"
#define YELLOW "\033[0;33m"
#define YELLOW_BRIGHT "\033[0;93m"
#define YELLOW_LIGHT "\033[0;93m"
#define BLUE_INTENSE "\033[0;94m"
#define RED "\033[0;31m"
#define RESET "\033[0m"

int	main(int argc, char **argv)
{
	int		fd;
	char	*line;

	if (argc != 2)
	{
		printf("Uso: %s <archivo>\n", argv[0]);
		return (1);
	}
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
	{
		perror("Error al abrir el archivo");
		return (1);
	}
	printf("\n---------------SIZE OF BUFFER IS--%d\n", BUFFER_SIZE);
	printf("\n-----------------START OF FILES -------------------\n");

	line = get_next_line(fd);
	while (line != NULL)
	{
		printf(GREEN "%s\n", line);
		printf(RESET);
		free(line);
		line = get_next_line(fd);
	}
	printf("\n-----------------END OF ALL FILES ------------------\n");
	close(fd);
	return (0);
}
/* 
#define GREEN "\033[0;32m"
#define YELLOW "\033[0;33m"
#define YELLOW_BRIGHT "\033[0;93m"
#define YELLOW_LIGHT "\033[0;93m"
#define BLUE_INTENSE "\033[0;94m"
#define RED "\033[0;31m"
#define RESET "\033[0m"

int main(int argc, char *argv[])
{
	int fd;
	char *line;
	
	if (argc == 2)
	{
		fd = open(argv[1], O_RDONLY);
		if (fd < 0)
		{
			perror("Error opening file");
			return (1);
		}
	}
	else
	{
		fd = 1;
		printf(BLUE_INTENSE "Please enter some text (Press Ctrl+D to 
		end input):\n");
		printf(RESET);
	}
	while ((line = get_next_line(fd)) != NULL)
	{
		printf(GREEN "You entered:\n%s", line);
		printf(RESET);

		printf(RED "Is correct!\n");
		printf(RESET);
	}
		free(line);
	   	if (argc == 2)
		close(fd);
	return (0);
} */

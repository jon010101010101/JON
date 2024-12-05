/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/28 17:37:29 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/13 17:01:26 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_free(char **str)
{
	if (str && *str)
	{
		free(*str);
		*str = NULL;
	}
	return (NULL);
}

char	*clean_box(char *box)
{
	char	*new_box;
	char	*ptr;
	int		len;

	if (!box)
		return (NULL);
	ptr = ft_strchr(box, '\n');
	if (!ptr)
		return (ft_free(&box));
	len = (ptr - box) + 1;
	if (!box[len])
		return (ft_free(&box));
	new_box = ft_substr(box, len, ft_strlen(box) - len);
	ft_free(&box);
	return (new_box);
}

char	*new_line(char *box)
{
	char	*line;
	char	*ptr;
	int		len;

	if (!box)
		return (NULL);
	ptr = ft_strchr(box, '\n');
	len = (ptr - box) + 1;
	line = ft_substr(box, 0, len);
	if (!line)
		return (NULL);
	return (line);
}

char	*read_box(int fd, char *new_box)
{
	char	*temp_box;
	int		read_it;

	read_it = 1;
	temp_box = malloc(sizeof(char) * BUFFER_SIZE + 1);
	if (!temp_box)
		return (ft_free(&new_box));
	while (read_it > 0 && (!new_box || !ft_strchr(new_box, '\n')))
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
	if (!new_box || !ft_strchr(new_box, '\n'))
		new_box = read_box(fd, new_box);
	if (!new_box)
		return (NULL);
	line = new_line(new_box);
	if (!line)
		return (ft_free(&new_box));
	new_box = clean_box(new_box);
	return (line);
}

#include "get_next_line.h"

int	main(int argc, char **argv)
{
	int		fd;
	char	*line;

	if (argc < 2)
	{
		printf("Uso: %s <archivo>\n", argv[0]);
		return (1);
	}
	/* fd = 42; */
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
	{
		perror("Error al abrir el archivo");
		return (1);
	}

	printf("---------------SIZE OF BUFFER IS--%d\n", BUFFER_SIZE);
	printf("-----------------START OF FILES -----------------\n");
	
	line = get_next_line(fd);
	while (line != NULL)
	{
		printf("%s", line);
		free(line);
		line = get_next_line(fd);
	}

	/* printf("-----------------END OF ALL FILES ------------------\n"); */
	
	close(fd);
	return (0);
}

/* int main(int argc, char *argv[])
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
		printf("Please enter some text:\n");
		printf("(Press Ctrl+D to end input):\n");
	}

	while ((line = get_next_line(fd)) != NULL)
	{
		printf("You write:\n%s", line);
        printf("Returned line:\n%s", line);
        free(line);
	}
	   	if (argc == 2)
		close(fd);
	return (0);
} */
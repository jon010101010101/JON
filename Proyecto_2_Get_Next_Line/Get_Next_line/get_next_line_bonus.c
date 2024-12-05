/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/10 19:29:03 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/12 19:10:24 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

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

char	*read_buffer(int fd, char *new_box)
{
	int		readit;
	char	*buffer;

	readit = 1;
	buffer = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!buffer)
		return (ft_free(&new_box));
	buffer[0] = '\0';
	while (readit > 0 && !ft_strchr(buffer, '\n'))
	{
		readit = read(fd, buffer, BUFFER_SIZE);
		if (readit > 0)
		{
			buffer[readit] = '\0';
			new_box = ft_strjoin(new_box, buffer);
		}
	}
	free(buffer);
	if (readit == -1)
		return (ft_free(&new_box));
	return (new_box);
}

char	*get_next_line(int fd)
{
	static char	*new_box[4096];
	char		*line;

	if (fd < 0)
		return (NULL);
	if ((new_box[fd] && !ft_strchr(new_box[fd], '\n')) || !new_box[fd])
		new_box[fd] = read_buffer(fd, new_box[fd]);
	if (!new_box[fd])
		return (NULL);
	line = new_line(new_box[fd]);
	if (!line)
		return (ft_free(&new_box[fd]));
	new_box[fd] = clean_box(new_box[fd]);
	return (line);
}
/* 
#define GREEN "\033[0;32m"
#define YELLOW "\033[0;33m"
#define YELLOW_BRIGHT "\033[0;93m"
#define YELLOW_LIGHT "\033[0;93m"
#define BLUE_INTENSE "\033[0;94m"
#define RED "\033[0;31m"
#define RESET "\033[0m"

int main(int argc, char **argv)
{
	int fd1, fd2, fd3;
	char *line;

	if (argc != 4)
	{
		printf("Uso: %s <archivo1> <archivo2> <archivo3>\n", argv[0]);
		return (1);
	}

	fd1 = open(argv[1], O_RDONLY);
	fd2 = open(argv[2], O_RDONLY);
	fd3 = open(argv[3], O_RDONLY);

	if (fd1 == -1 || fd2 == -1 || fd3 == -1)
	{
		perror("Error al abrir el archivo");
		return (1);
	}

	printf("\n---------------SIZE OF BUFFER IS--%d\n", BUFFER_SIZE);
	printf("\n-----------------START OF FILES -------------------\n");

	printf("\n----CONTENIDO DE %s----\n", argv[1]);
	
	while ((line = get_next_line(fd1)) != NULL)
	{
		printf(GREEN "%s\n", line);
        printf(RESET);
        free(line);
	}
	close(fd1);

	printf("\n----CONTENIDO DE %s----\n", argv[2]);
	
	while ((line = get_next_line(fd2)) != NULL)
	{
		printf(BLUE_INTENSE "%s\n", line);
        printf(RESET);
        free(line);
	}
	close(fd2);

	printf("\n----CONTENIDO DE %s----\n", argv[3]);
	
	while ((line = get_next_line(fd3)) != NULL)
	{
		printf(RED "%s\n", line);
        printf(RESET);
        free(line);;
	}
	close(fd3);

	printf("\n-----------------END OF ALL FILES -------------------\n");

	return (0);
} */

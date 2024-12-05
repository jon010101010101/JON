/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main_bonus.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/17 10:22:26 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/17 11:12:21 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

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

	printf(YELLOW_BRIGHT"\n------SIZE OF BUFFER IS-%d-------\n", BUFFER_SIZE);
	printf(YELLOW_BRIGHT"\n-------START OF FILES -------------------\n");
	printf(RESET);
	
	printf("\n----CONTENIDO DE %s----\n", argv[1]);
	
	while ((line = get_next_line(fd1)) != NULL)
	{
		printf(GREEN "%s", line);
        printf(RESET);
        free(line);
	}
	close(fd1);

	printf("\n----CONTENIDO DE %s----\n", argv[2]);
	
	while ((line = get_next_line(fd2)) != NULL)
	{
		printf(BLUE_INTENSE "%s", line);
        printf(RESET);
        free(line);
	}
	close(fd2);

	printf("\n----CONTENIDO DE %s----\n", argv[3]);
	
	while ((line = get_next_line(fd3)) != NULL)
	{
		printf(RED "%s", line);
        printf(RESET);
        free(line);;
	}
	close(fd3);

	return (0);
}

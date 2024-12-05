/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main_bonus_alt.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/17 10:50:06 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/18 09:56:19 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

#define GREEN "\033[0;32m"
#define YELLOW "\033[0;33m"
#define YELLOW_BRIGHT "\033[1;33m"
#define BLUE_INTENSE "\033[0;34m"
#define RED "\033[0;31m"
#define RESET "\033[0m"

int main(int argc, char **argv)
{
	int fd1, fd2, fd3;
	char *line;

	if (argc != 4)
	{
		printf("Uso: %s <archivo1> <archivo2> <archivo3>\n", argv[0]);
		return 1;
	}
	fd1 = open(argv[1], O_RDONLY);
	fd2 = open(argv[2], O_RDONLY);
	fd3 = open(argv[3], O_RDONLY);
	if (fd1 == -1 || fd2 == -1 || fd3 == -1)
	{
		perror("Error al abrir el archivo");
		return 1;
	}
	printf(YELLOW_BRIGHT"\n------SIZE OF BUFFER IS-%d-------\n", BUFFER_SIZE);
	printf(YELLOW_BRIGHT"\n-------START OF FILES -------------------\n");
	printf(RESET);

	int count1 = 0, count2 = 0, count3 = 0;
	int max_count = 0;

	if (fd1 > max_count) max_count = fd1;
	if (fd2 > max_count) max_count = fd2;
	if (fd3 > max_count) max_count = fd3;

	for (int i = 0; i < max_count; i++)
	{
		if (count1 != max_count)
		{
			while ((line = get_next_line(fd1)) != NULL)
			{
				printf(GREEN "%s", line);
				printf(RESET);
				free(line);
				count1++;
				break;
			}
		}
		if (count2 != max_count)
		{
			while ((line = get_next_line(fd2)) != NULL)
			{
				printf(BLUE_INTENSE "%s", line);
				printf(RESET);
				free(line);
				count2++;
				break;
			}
		}
		if (count3 != max_count)
		{
			while ((line = get_next_line(fd3)) != NULL)
			{
				printf(RED "%s", line);
				printf(RESET);
				free(line);
				count3++;
				break ;
			}
		}
	}
	close(fd1);
	close(fd2);
	close(fd3);
	return (0);
}

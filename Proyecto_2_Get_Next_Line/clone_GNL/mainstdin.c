/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mainstdin.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/17 10:22:46 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/17 11:12:05 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

#define GREEN "\033[0;32m"
#define YELLOW "\033[0;33m"
#define YELLOW_BRIGHT "\033[0;93m"
#define YELLOW_LIGHT "\033[0;93m"
#define BLUE_INTENSE "\033[0;94m"
#define RED "\033[0;31m"
#define BRIGHT_RED "\033[1;31m"
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
		printf(YELLOW_BRIGHT "Please enter some text:\n");
		printf(YELLOW_BRIGHT "(Press Ctrl+D to end input):\n");
		printf(RESET);
	}

	while ((line = get_next_line(fd)) != NULL)
	{
		printf(BLUE_INTENSE "You write:\n%s", line);
        printf(BRIGHT_RED "Returned line:\n%s", line);
        printf(RESET);
		free(line);
	}
	   	if (argc == 2)
		close(fd);
	return (0);
}

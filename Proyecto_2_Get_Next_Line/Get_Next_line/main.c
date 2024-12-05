/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/05 17:01:02 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/10 19:34:15 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

/* int	main(int argc, char **argv)
{
	int		fd;
	char	*line;

	if (argc != 2)
	{
		printf("Uso: %s <archivo>\n", argv[0]);
		return (1);
	}
	printf("\n---------------SIZE OF BUFFER IS--%d\n", BUFFER_SIZE);
	printf("\n-----------------START OF FILE -------------------\n");
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
	{
		perror("Error al abrir el archivo");
		return (1);
	}
	while (1)
	{
		line = get_next_line(fd);
		if (!line)
			break ;
		printf("%s\n", line);
		free(line);
	}
	printf("\n-----------------END OF FILE -------------------\n");
	close(fd);
	return (0);
} */

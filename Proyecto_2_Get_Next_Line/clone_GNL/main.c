/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/06/17 10:22:35 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/17 11:19:15 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

#define GREEN "\033[0;32m"
#define YELLOW "\033[0;33m"
#define YELLOW_BRIGHT "\033[1;33m"
#define BLUE_INTENSE "\033[0;34m"
#define RED "\033[0;31m"
#define BRIGHT_RED "\033[1;31m"
#define RESET "\033[0m"

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char **argv)
{
    int fd;
    char *line;

    if (argc < 2)
    {
        printf("Uso: %s <archivo>\n", argv[0]);
        return 1;
    }
    fd = open(argv[1], O_RDONLY);
    if (fd == -1)
    {
        perror("Error al abrir el archivo");
        return (1);
    }
    printf("\n--------------- TAMAÑO DEL BUFFER ES: %d ---------------\n", BUFFER_SIZE);
    printf("\n----------------- COMIENZO DE ARCHIVOS -------------------\n");
    line = get_next_line(fd);
    while (line != NULL)
    {
        printf(YELLOW_BRIGHT "%s", line);
        printf(RESET);
        free(line);
        line = get_next_line(fd);
    }
    close(fd);
    return (0);
}

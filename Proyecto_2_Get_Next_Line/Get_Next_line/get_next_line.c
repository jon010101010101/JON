/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/28 17:37:29 by jurrutia          #+#    #+#             */
/*   Updated: 2024/06/13 11:04:32 by jurrutia         ###   ########.fr       */
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
/* 
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
} */

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
		printf(BLUE_INTENSE "Please enter some text:\n");
		printf(BLUE_INTENSE "(Press Ctrl+D to end input):\n");
		printf(RESET);
	}

	while ((line = get_next_line(fd)) != NULL)
	{
		printf(GREEN "You write:\n%s", line);
        printf(RED "Returned line:\n%s", line);
        printf(RESET);
		free(line);
	}
	   	if (argc == 2)
		close(fd);
	return (0);
}

Función: ft_free

char *ft_free(char **str)
{
    // Verifica si el puntero `str` y el puntero al que apunta `*str` no
	// son nulos. Doble puntero para poder liberar la memoria del puntero
	// original
    if (str && *str)
    {
        // Libera la memoria apuntada por `*str`
        free(*str);
        // Asigna `NULL` al puntero para evitar el uso de memoria ya 
		// liberada
        *str = NULL;
    }
    // Retorna `NULL`
    return (NULL);
}
Función: clean_box

char *clean_box(char *box)
{
    char *new_box;
    char *ptr;
    int len;

    // Encuentra el primer carácter de nueva línea en `box`
    ptr = ft_strchr(box, '\n');
    if (!ptr)
    {
        // Si no encuentra un carácter de nueva línea, libera `box` y 
		// retorna `NULL`
        new_box = NULL;// Esta línea establece explícitamente new_box a 
						// NULL, porque no hay ninguna línea completa 
						// para extraer. 
        return (ft_free(&box));// Libera la memoria de box y retorna NULL
    }
    else
        // Calcula la longitud hasta el carácter de nueva línea (inclusive)
        len = (ptr - box) + 1;

    // Si `box` termina justo después del carácter de nueva línea, libera
	// `box` y retorna `NULL`
    if (!box[len])
        return (ft_free(&box));

    // Crea una subcadena desde `len` hasta el final de `box`.

	//ft_substr es una función que crea una nueva cadena, extrayendo una
	// subcadena de box que comienza en el índice len y tiene una 
	// longitud de ft_strlen(box) - len
	// || !new_box Verifica si new_box es NULL. Si es NULL, significa 
	// que no se han leído datos aún.

	// La condición if ((new_box && !ft_strchr(new_box, '\n')) || !new_box)
	// verifica si se necesita leer más datos del archivo para encontrar 
	// una nueva línea. Si new_box no contiene una nueva línea completa o 
	// está vacío, se llama a read_box para leer más datos y añadirlos a 
	// new_box. Esto permite que get_next_line continúe procesando datos 
	// del archivo de manera eficiente, leyendo solo lo necesario y 
	// extrayendo líneas completas una por una.
	
    new_box = ft_substr(box, len, ft_strlen(box) - len);
    // Libera la memoria de `box`
    ft_free(&box);

    // Si no pudo crear `new_box`, retorna `NULL`
    if (!new_box)
        return (NULL);
	
    // Retorna la nueva subcadena `new_box`
    return (new_box);
}

Función: new_line

char *new_line(char *box)
{
    char *line;
    char *ptr;
    int len;

    // Encuentra el primer carácter de nueva línea en `box`
    ptr = ft_strchr(box, '\n');
    // Calcula la longitud hasta el carácter de nueva línea (inclusive)
	// ptr es un puntero a char que se utiliza para almacenar la 
	//posición de la primera ocurrencia del carácter '\n' en la cadena box.
    len = (ptr - box) + 1;
    // Crea una subcadena desde el inicio de `box` (por eso esta el 0) 
	// hasta `len`(es la longitud de la línea que incluye el carácter 
	// de nueva línea '\n'.)
    line = ft_substr(box, 0, len);

    // Si no pudo crear `line`, retorna `NULL`
    if (!line)
        return (NULL);

    // Retorna la nueva línea `line`
    return (line);
}
Función: read_box

char *read_box(int fd, char *new_box)
{
    int read_it;
    char *temp_box;

    // Inicializa `read_it` para leer al menos una vez. Para iniciar 
	// la variable
    read_it = 1;
    // Reserva memoria para `temp_box` con el tamaño del buffer
    temp_box = malloc(sizeof(char) * (BUFFER_SIZE + 1));
    if (!temp_box)
        // Si la reserva de memoria falla, libera `new_box` y retorna 
	//`NULL`
        return (ft_free(&new_box));

    // Inicializa `temp_box` con una cadena vacía antes de que se 
	// comience a usar en el bucle de lectura, asi se convierte en una
	// cadena valida aunque este vacia.
    temp_box[0] = '\0';

    // Mientras haya datos para leer y no se haya encontrado un carácter 
	//de nueva línea
    while (read_it > 0 && !ft_strchr(temp_box, '\n'))
    {
        // Lee hasta `BUFFER_SIZE` bytes del archivo descriptor `fd` y
		// los almacena en `temp_box`
        read_it = read(fd, temp_box, BUFFER_SIZE);
		
	// if (read_it > 0) en la función read_box verifica si la lectura de 
	// datos fue exitosa. Si se leyeron bytes, esos bytes se procesan y 
	//se añaden a new_box
		
        if (read_it > 0)
        {
            // Asegura que `temp_box` termine en `'\0'`
            temp_box[read_it] = '\0';
            // Une `new_box` con `temp_box` y almacena el resultado en
			// `new_box`
            new_box = ft_strjoin(new_box, temp_box);
        }
    }
    // Libera la memoria de `temp_box`
    free(temp_box);

    // Si la lectura falla, libera `new_box` y retorna `NULL`
    if (read_it == -1)
        return (ft_free(&new_box));

    // Retorna `new_box` con los datos leídos
    return (new_box);
}
Función: get_next_line

char *get_next_line(int fd)
{

	// La declaración static char *new_box = NULL; dentro de la función
	// get_next_line se utiliza para mantener el estado entre múltiples 
	// llamadas a la función. Se usa para declarar una variable con duración
	// de almacenamiento estática, es decir, la variable conserva su valor
	// entre las invocaciones de la función.
	
	// Que sea = NULL, asegura que se establece un estado inicial seguro
	// y conocido y no apunta a ninguna ubicacion de memoria
	
    static char *new_box = NULL;
    char *line;

    // Verifica si el descriptor de archivo es válido
    if (fd < 0)
        return (NULL);

    // Si no hay nueva línea en `new_box` o `new_box` es nulo, 
	// lee más datos
	// La combinación new_box && !ft_strchr(new_box, '\n') es true si
	// new_box no es NULL pero no contiene una nueva línea (\n). Esto 
	//indica que hay datos en new_box, pero no contienen una línea completa.
	
    if ((new_box && !ft_strchr(new_box, '\n')) || !new_box)

// La asignación new_box = read_box(fd, new_box); en get_next_line maneja 
// la lectura de datos del archivo, asegurando que new_box contenga 
// suficientes datos para extraer líneas completas. Esta asignación es 
// esencial para mantener el flujo de lectura de líneas continuo y 
// eficiente, gestionando adecuadamente el contenido de new_box y 
// garantizando que el proceso de extracción de líneas se realice de 
// manera adecuada y sin errores.
	
        new_box = read_box(fd, new_box);

    // Si no hay datos leídos, retorna `NULL`
    if (!new_box)
        return (NULL);

    // Extrae una línea de `new_box`
    line = new_line(new_box);
    if (!line)
        // Si no pudo extraer la línea, libera `new_box` y retorna `NULL`
        return (ft_free(&new_box));

    // Limpia `new_box` dejando solo los datos después de la nueva línea
    new_box = clean_box(new_box);

    // Retorna la línea extraída
    return (line);
}
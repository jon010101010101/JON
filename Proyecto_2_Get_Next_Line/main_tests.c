
#include <stdio.h>
#include <fcntl.h>	
#include "get_next_line.h"

#define GREEN "\033[0;32m"
#define RESET "\033[0m"

void use_test(int fd, int num_lineas)
{
	int i;
	char *line;


	if (fd < 0)
    {
        write(2, "Error al abrir archivo\n", 19);
        //return (1);
    }

	i = 1;

	printf("El valor del file descriptor es %d \n\n", fd);
	
	while (i <= num_lineas)
	{
		line = get_next_line(fd);
		printf("linea (%d)  \n", i);
	    printf("%s", line);
		i++;
	} 
	printf("\n\n");
}

int main(void)
{
    int fd;
	int	num_lineas;// para mostrar, si hay mas muestra (null)

	fd = 42;
	num_lineas = 1;
	printf( GREEN "file descriptor no valido\n" RESET);
	use_test(fd, num_lineas);

	//4 lineas de longitud 6
	printf( GREEN "4 lineas de longitud 6\n" RESET);
   	fd = open("cuatro_lineas_long_6.txt", O_RDONLY);
	num_lineas = 4;
	use_test(fd, num_lineas);

	//una sola linea de 50.000 'a'
	printf( GREEN "una sola linea con 50.000 a\n" RESET);
	fd = open("una_linea_50000_a.txt", O_RDONLY);
	num_lineas = 1;
	use_test(fd, num_lineas);


	//varias lineas cortas
	fd = open("lineas_cortas.txt", O_RDONLY);
	printf( GREEN "varias lineas cortas\n" RESET);
	num_lineas = 6;
	use_test(fd, num_lineas);

	//archivo vacio
	printf( GREEN "archivo vacio\n" RESET);
	fd = open("vacio.txt", O_RDONLY);
	num_lineas = 1;
	use_test(fd, num_lineas);

	//solo un salto de linea
	printf( GREEN "archivo que solo contiene un salto de linea y nada mas\n" RESET);
	fd = open("solo_1_salto_linea.txt", O_RDONLY);
	num_lineas = 1;
	use_test(fd, num_lineas);

	//Sherlock Holmes
	printf( GREEN "Sherlock Holmes entero\n" RESET);
	fd = open("sherlock.txt", O_RDONLY);
	num_lineas = 4;
	use_test(fd, num_lineas);
   
    return (0);
}

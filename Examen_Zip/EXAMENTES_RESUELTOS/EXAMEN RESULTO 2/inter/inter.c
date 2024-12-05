/*Escribe un programa que tome dos cadenas y muestre, sin dobles, el
caracteres que aparecen en ambas cadenas, en el orden en que aparecen en la primera
uno.
La pantalla será seguida por un \n.
Si el número de argumentos no es 2, el programa muestra \n.

Examples:
$>./inter "padinton" "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
padinto$
$>./inter ddf6vewg64f gtwthgdwthdwfteewhrtag6h4ffdhsd | cat -e
df6ewg4$
$>./inter "rien" "cette phrase ne cache rien" | cat -e
rien$
$>./inter | cat -e
$
*/


/* ANA OK*/

#include <unistd.h>

int ft_not_seen_before(char *str, char c, int max_pos)
{
	int	i;

	i = 0;
	while (str[i] && (i < max_pos || max_pos == -1))
	{
		if (str[i] == c)
			return (0);
		else 
			i++;	
	}
	return (1);
}

int main (int argc, char **argv)
{
	int i;

	i = 0;
	if (argc == 3)
	{
		while (argv[1][i])
		{
			if (ft_not_seen_before(argv[1], argv[1][i], i) && !ft_not_seen_before(argv[2], argv[1][i], -1))
				write(1, &argv[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}

/* COMENTARIOS */

/* #include <unistd.h>  // Incluimos la biblioteca unistd.h para usar la función write

// Función que verifica si un carácter 'c' ya ha aparecido antes en la cadena 'str'
// hasta el índice 'i'
int ft_single_in_param(char *str, char c, int i)
{
    int j;

    j = 0;  // Inicializamos el índice j en 0
    while (str[j] != '\0' && j < i)  // Recorremos la cadena hasta llegar al índice 'i'
    {
        if (str[j] == c)  // Si encontramos el carácter 'c' en la cadena antes del índice 'i'
            return (1);  // Retornamos 1 para indicar que el carácter ya apareció antes
        j++;  // Incrementamos j para seguir recorriendo la cadena
    }
    return (0);  // Si no encontramos el carácter antes del índice 'i', retornamos 0
}

// Función que verifica si un carácter 'c' está presente en la cadena 'str'
int ft_in_other_param(char *str, char c)
{
    int i;

    i = 0;  // Inicializamos el índice i en 0
    while (str[i] != '\0')  // Recorremos la cadena hasta llegar al final
    {
        if (str[i] == c)  // Si encontramos el carácter 'c' en la cadena
            return (1);  // Retornamos 1 para indicar que el carácter está presente
        i++;  // Incrementamos i para seguir recorriendo la cadena
    }
    return (0);  // Si no encontramos el carácter, retornamos 0
}

// Función principal del programa
int main(int argc, char **argv)
{
    int i;

    i = 0;  // Inicializamos el índice i en 0
    if (argc == 3)  // Verificamos que se hayan pasado exactamente 2 argumentos (además del nombre del programa)
    {
        while (argv[1][i] != '\0')  // Recorremos la primera cadena carácter por carácter
        {
            // Verificamos que el carácter en argv[1][i] no haya aparecido antes
            // y que esté presente en la segunda cadena argv[2]
            if ((ft_single_in_param(argv[1], argv[1][i], i) == 0)   
                && (ft_in_other_param(argv[2], argv[1][i]) == 1))  
                write(1, &argv[1][i], 1);  // Si ambas condiciones se cumplen, escribimos el carácter en la salida estándar
            i++;  // Incrementamos i para seguir recorriendo la cadena
        }
    }
    write(1, "\n", 1);  // Escribimos un salto de línea al final de la salida
    return (0);  // Retornamos 0 para indicar que el programa terminó con éxito
} */

/* tiene fallo */

/* include <unistd.h>

int ft_single_in_param(char *str, char c, int i)
{
    int j;
             
    j = 0;                              
    while (str[j] != '\0' && j < i)     
    {
        if (str[j] == c)                
            return (1);             
        j++;                             
    }
    return (0);
}

int ft_in_other_param(char *str, char c)
{
    int i;

    i = 0;                  
    while (str[i] != '\0')  
    {
        if (str[i] == c)    
            return (1);
        i++;                
    }
    return (0);
}

int main(int argc, char **argv)
{
    int i;

    i = 0;
    if (argc == 3)                                                 
    {
        while (argv[1][i] != '\0')                                  
        {
            if ((ft_single_in_param(argv[1], argv[1][i], i) == 0)   
                && (ft_in_other_param(argv[2], argv[1][i]) == 1))  
                write(1, &argv[1][i], 1);                          
            i++;                  
        }           
    }
    write(1, "\n", 1);                                              
    return (0);
}
 */
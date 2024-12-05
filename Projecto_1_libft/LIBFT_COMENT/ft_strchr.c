/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 11:25:36 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:55:00 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	int	i;

	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] == (char)c)
			return ((char *)&s[i]);
		i++;
	}
	if (s[i] == (char)c)
		return ((char *)&s[i]);
	return (NULL);
}
/*
int main()
{
	const char cadena[] = "Hola, Manola!";
	char caracter = 'o';

	char *resultado = ft_strchr(cadena, caracter);

	if (resultado != NULL)
	{
	printf("El primer \"%c\" encontrado es: %s\n", caracter, resultado);
	} 
	else
	{
	printf("El caracter \"%c\" no se encontró en la cadena. %s\n", caracter,
	 resultado);
	}
	return 0;
}
*/
// Localiza la primera c en la cadena apuntada por s

/*
Función ft_strchr
La función ft_strchr busca la primera aparición de un carácter específico en una
 cadena. Si encuentra el carácter, devuelve un puntero a su posición en la 
 cadena. Si no lo encuentra, devuelve NULL.

* Declaración de la función

char *ft_strchr(const char *s, int c)
const char *s: Es un puntero a la cadena en la que se va a buscar el carácter.
int c: Es el carácter que se busca en la cadena. Aunque se pasa como un int, 
se convierte a char dentro de la función.

* Variables

int i;
i: Es un índice que se usa para recorrer la cadena.
Implementación paso a paso

* Inicialización del índice

i = 0;
Se inicializa el índice i a 0 para empezar desde el principio de la cadena.

* Bucle while

while (s[i] != '\0')
{
    if (s[i] == (char)c)		
        return ((char *)&s[i]);
    i++;

s[i] es el valor del carácter en la posición i de la cadena s.
&s[i] es la dirección de memoria de ese carácter, es decir, un puntero al 
carácter en la posición i

(char *) es una conversión de tipo (cast) a puntero a char.
En este caso, s es originalmente un puntero a const char, y al hacer 
(char *)&s[i],  se está eliminando la cualidad const para devolver un puntero
 que no es constante.

La conversión (char *) es necesaria para convertir el tipo const char * a 
char *. Esto permite que la función devuelva un puntero que concuerde con su 
tipo de retorno, aunque en el uso práctico no se debería modificar la cadena 
original a través de este puntero si la entrada era const.
	
}
while (s[i] != '\0'): Este bucle recorre la cadena hasta que encuentra el 
carácter  nulo ('\0'), que indica el final de la cadena.

if (s[i] == (char)c): Dentro del bucle, se verifica si el carácter actual 
s[i] es  igual al carácter c convertido a char.

return ((char *)&s[i]): Si s[i] es igual a c, se devuelve un puntero a la 
posición  de s[i] en la cadena. Se hace un cast a char * porque la función
 devuelve un puntero a char.

i++: Si s[i] no es igual a c, se incrementa i para seguir con el siguiente 
carácter.

* Comprobación final fuera del bucle

if (s[i] == (char)c)
    return ((char *)&s[i]);
Después de salir del bucle, se verifica si el carácter en la posición actual
 s[i] (que podría ser '\0') es igual a c.

Esta verificación es necesaria porque c podría ser el carácter nulo ('\0'), 
y si es así, debemos devolver un puntero a ese carácter en la cadena.
 
* Retorno en caso de no encontrar el carácter

return (NULL);
Si el carácter c no se encuentra en la cadena, la función devuelve NULL.

EJEMPLO
Supongamos que llamamos a la función así:

const char *str = "Hello, world!";
char *result = ft_strchr(str, 'w');
La cadena es "Hello, world!".
Queremos encontrar la primera aparición del carácter 'w'.
La función recorrerá la cadena hasta llegar al carácter 'w' y devolverá un 
puntero a 'w' dentro de la cadena. Si el carácter no existiera en la cadena,
 devolvería NULL.

Código completo de la función

char *ft_strchr(const char *s, int c)
{
    int i;

    i = 0;
    while (s[i] != '\0')
    {
        if (s[i] == (char)c)
            return ((char *)&s[i]);
        i++;
    }
    if (s[i] == (char)c)
        return ((char *)&s[i]);
    return (NULL);
}
Esta implementación es simple y eficiente para buscar la primera aparición de un 
carácter en una cadena en C.

Ejemplo de iteración
Supongamos que tenemos la cadena "Hello, world!" y buscamos el carácter 'o'.

Inicialización

i = 0
Cadena: "Hello, world!"
Primera iteración

s[0] es 'H'
'H' no es igual a 'o'
Incrementar i: i = 1
Segunda iteración

s[1] es 'e'
'e' no es igual a 'o'
Incrementar i: i = 2
Tercera iteración

s[2] es 'l'
'l' no es igual a 'o'
Incrementar i: i = 3
Cuarta iteración

s[3] es 'l'
'l' no es igual a 'o'
Incrementar i: i = 4
Quinta iteración

s[4] es 'o'
'o' es igual a 'o'
La función devuelve un puntero a s[4]
Si el carácter 'o' no existiera en la cadena, el bucle continuaría hasta llegar 
al final de la cadena ('\0').

* Comprobación final fuera del bucle
Si no se encontró el carácter en el bucle, hay una última comprobación fuera del
 bucle:


if (s[i] == (char)c)
    return ((char *)&s[i]);
Esto se debe a que el carácter que estamos buscando podría ser '\0', y en 
ese caso,  debemos devolver un puntero al carácter nulo al final de la cadena.
Retorno en caso de no encontrar el carácter
Si el carácter c no se encuentra en la cadena, la función devuelve NULL.

return (NULL);
Esta iteración asegura que se revisa cada carácter de la cadena s hasta 
encontrar el carácter c o llegar al final de la cadena
*/
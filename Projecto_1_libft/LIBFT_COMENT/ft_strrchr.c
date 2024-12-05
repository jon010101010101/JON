/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 16:46:55 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:46:01 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	int		i;
	char	*ptr;

	i = 0;
	ptr = 0;
	while (s[i])
	{
		if (s[i] == (char)c)
			ptr = (char *)(s + i);
		i++;
	}
	if (s[i] == (char)c)
		ptr = (char *)(s + i);
	return (ptr);
}

/* int main()
{
	const char cadena[] = "Hello, world!";
	int caracter = 'o';

	char *resultado = ft_strrchr(cadena, caracter);

	if (resultado != NULL)
	{
	printf("El último \"%c\" encontrado es: %s\n", caracter, resultado);
	} 
	else
	{
	printf("El caracter \"%c\" no se encontró en la cadena.\n", caracter);
	}
	return 0;
} */

/* Busca la última aparición del carácter c en la cadena s. Retorna un puntero
 a la posición de la última ocurrencia del carácter, o NULL si el carácter no 
 se encuentra en la cadena. */

/* char *ft_strrchr(const char *s, int c)
{
	int i;
	char *ptr;

	// Inicializamos 'i' para iterar desde el principio de la cadena 's'
	i = 0;

	// Inicializamos 'ptr' como NULL (0), indicando que no se ha encontrado 'c'
		 aún
	ptr = 0;

	// Iteramos sobre la cadena 's' hasta encontrar el carácter nulo '\0'
	while (s[i]) es igual que  while (*s != '\0') y luego s++;
	{
		// Si el carácter actual es igual a 'c', actualizamos 'ptr'
		Si s[i] es igual a c, se actualiza ptr para que apunte a la posición 
		actual (s + i) en la cadena.
		(char)c asegura que c se trate como un carácter, ya que c es de tipo 
		int por el prototipo de la función.
		
		if (s[i] == (char)c)
			ptr = (char *)(s + i);
		// Avanzamos al siguiente carácter de la cadena
		i++;
	}

	// Verificamos si el carácter nulo '\0' al final de la cadena es igual a 'c'
	if (s[i] == (char)c)
		ptr = (char *)(s + i);

	// Retornamos 'ptr', que apunta a la última ocurrencia de 'c' o es NULL si 
	no se encontró
	return (ptr);
} */

/* Declaración e inicialización:

s = "Hello, world!"
c = 'o'
i = 0
ptr = NULL
Bucle while principal:

Iteración 1:
s[i] = 'H', c = 'o'
'H' != 'o', no se actualiza ptr
Incrementar i (i = 1)
Iteración 2:
s[i] = 'e', c = 'o'
'e' != 'o', no se actualiza ptr
Incrementar i (i = 2)
Iteración 3:
s[i] = 'l', c = 'o'
'l' != 'o', no se actualiza ptr
Incrementar i (i = 3)
Iteración 4:
s[i] = 'l', c = 'o'
'l' != 'o', no se actualiza ptr
Incrementar i (i = 4)
Iteración 5:
s[i] = 'o', c = 'o'
'o' == 'o', actualizar ptr a s + i (ptr = s + 4)
Incrementar i (i = 5)
Iteración 6:
s[i] = ',', c = 'o'
',' != 'o', no se actualiza ptr
Incrementar i (i = 6)
Iteración 7:
s[i] = ' ', c = 'o'
' ' != 'o', no se actualiza ptr
Incrementar i (i = 7)
Iteración 8:
s[i] = 'w', c = 'o'
'w' != 'o', no se actualiza ptr
Incrementar i (i = 8)
Iteración 9:
s[i] = 'o', c = 'o'
'o' == 'o', actualizar ptr a s + i (ptr = s + 8)
Incrementar i (i = 9)
Iteración 10:
s[i] = 'r', c = 'o'
'r' != 'o', no se actualiza ptr
Incrementar i (i = 10)
Iteración 11:
s[i] = 'l', c = 'o'
'l' != 'o', no se actualiza ptr
Incrementar i (i = 11)
Iteración 12:
s[i] = 'd', c = 'o'
'd' != 'o', no se actualiza ptr
Incrementar i (i = 12)
Iteración 13:
s[i] = '!', c = 'o'
'!' != 'o', no se actualiza ptr
Incrementar i (i = 13)
Verificación final fuera del bucle:

s[i] = '\0', no coincide con c
ptr sigue apuntando a s + 8
Retorno del resultado:

La función retorna ptr, que apunta a la última ocurrencia de 'o' en 
"Hello, world!".
Resultado
En nuestro ejemplo, result apuntará a "orld!" dentro de "Hello, world!".
 */
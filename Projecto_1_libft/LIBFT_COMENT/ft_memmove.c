/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/16 18:46:08 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:47:38 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dst, const void *src, size_t len)
{
	size_t		i;
	char		*dst_ptr;
	const char	*src_ptr;

	dst_ptr = (char *)dst;
	src_ptr = (const char *)src;
	if (src == NULL && dst == NULL)
		return (NULL);
	if (dst_ptr < src_ptr || dst_ptr >= src_ptr + len)
		ft_memcpy (dst, src, len);
	else
	{
		i = len;
		while (i > 0)
		{
			dst_ptr[i - 1] = src_ptr[i - 1];
			i--;
		}
	}
	return (dst);
}

/* int main()
{
	char str[] = "Hola, Manola!";
	ft_memmove(str + 2, "1234", 1);

	printf("Después de ft_memmove: %s\n", str);

	return (0);
} */

/* ft_memmove(str + 2, "1234", 1); 

str + 2. Apunta a direccion de memoria dos lugares despues de str
1234. 	Un punteroa una cadena de caracteres que tiene 1234
1. 		Este es el numero de bytes que se moverán.
 */

/* Se utiliza para copiar un bloque de memoria desde una ubicación a otra, 
incluso si las áreas de memoria se superponen */

/*
void	*ft_memmove(void *dst, const void *src, size_t len)
{
	size_t		i;
	char		*dst_ptr;	// Puntero a char para recorrer el destino
	const char	*src_ptr;	// Puntero constante a char para recorrer el origen

	dst_ptr = (char *)dst;			// Convertir el puntero destino a char
	src_ptr = (const char *)src;	// Convertir el puntero origen a char 
									// constante

	Los punteros void* son punteros genéricos y no pueden ser desreferenciados
	directamente. Convertirlos a char* y const char* permite manipular los datos
	a nivel de bytes, ya que un char tiene un tamaño de 1 byte.

	char* y const char* permiten realizar operaciones de comparación, acceso e
	incremento de manera sencilla y directa, que son esenciales para implementar
	la lógica de ft_memmove.
	
	
// Verificar si src y dst son NULL. Comprobación de seguridad.
	if (src == NULL && dst == NULL)
		return (NULL);

// Verificar si se superponen las regiones de memoria

	Si dst está antes de src o no hay solapamiento (dst_ptr >= src_ptr + len),
	la función simplemente usa ft_memcpy, que copia bytes desde el principio de 
	rc hacia dst.
	Si hay solapamiento y dst está dentro del rango de src (dst_ptr >= src_ptr 
	y dst_ptr < src_ptr + len), es necesario copiar los bytes en orden inverso 
	(de atrás hacia adelante) para evitar sobrescribir los datos de src que aún
	no han sido copiados.
	
	if (dst_ptr < src_ptr || dst_ptr >= src_ptr + len)
		ft_memcpy (dst, src, len);  // Si no se superponen, usamos ft_memcpy 
									// para copiar byte a byte
	else
	{
		i = len;   // Si se superponen, copiamos byte a byte en orden inverso
					Esta lógica asegura que incluso si dst y src se solapan, 
					cada byte de src se copia a dst sin que los datos aún no 
					copiados sean sobrescritos por los datos ya copiados.
		
		while (i > 0)
		{
			dst_ptr[i - 1] = src_ptr[i - 1]; // Copiar byte desde src a dst en
											 // orden inverso
			i--;
		}
	}
	return (dst); // Devolvemos el puntero a dst
}
*/

/* EJEMPLO
Supongamos que tenemos un arreglo src de 10 bytes y un arreglo dst que apunta
 a una parte del mismo arreglo src. Queremos mover 5 bytes dentro del arreglo:

char src[] = "1234567890";
char *dst = src + 4; // dst apunta al '5'
size_t len = 5;
La llamada a ft_memmove sería:

ft_memmove(dst, src, len);
Veamos cómo se ejecuta la función paso a paso:

Paso 1: Declaración de variables

size_t      i;
char        *dst_ptr;
const char  *src_ptr;
Paso 2: Inicialización de punteros

dst_ptr = (char *)dst;  // dst_ptr apunta a '5' en src
src_ptr = (const char *)src;  // src_ptr apunta al inicio de src
Paso 3: Verificación de punteros nulos

if (src == NULL && dst == NULL)
    return (NULL);
Ambos punteros no son nulos, así que se continúa.

Paso 4: Verificación de solapamiento de memoria

if (dst_ptr < src_ptr || dst_ptr >= src_ptr + len)
    ft_memcpy(dst, src, len);
else
En este caso, dst_ptr (src + 4) no es menor que src_ptr (src) pero está 
dentro del rango src_ptr + len (src + 5), así que hay solapamiento. La función 
no usa ft_memcpy y entra en el else.

Paso 5: Copia de bytes en caso de solapamiento

else
{
    i = len;  // i = 5
    while (i > 0)
    {
        dst_ptr[i - 1] = src_ptr[i - 1];
        i--;
    }
}
Ahora, se copia byte a byte desde el final hacia el principio.

Iteración del bucle:
i = 5: dst_ptr[4] = src_ptr[4] -> '5' = '5' (sin cambio visible)
i = 4: dst_ptr[3] = src_ptr[3] -> '4' = '4' (sin cambio visible)
i = 3: dst_ptr[2] = src_ptr[2] -> '3' = '3' (sin cambio visible)
i = 2: dst_ptr[1] = src_ptr[1] -> '2' = '2' (sin cambio visible)
i = 1: dst_ptr[0] = src_ptr[0] -> '1' = '1' (sin cambio visible)
Aunque en este caso no hay cambio visible porque estamos copiando dentro 
del mismo arreglo y los datos se solapan perfectamente, este bucle asegura
 que los bytes se copien correctamente evitando sobrescrituras indeseadas. */
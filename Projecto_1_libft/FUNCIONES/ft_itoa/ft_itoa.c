/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/19 12:07:34 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/15 16:58:26 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"


/* int	main(void)

{
	
} 

*/

// DESCRIPCION.Utilizando malloc(3), genera una string que represente
// el valor entero recibido como argumento. Los números negativos
// tienen que gestionarse.

// VALOR DEVUELTO. La string que represente el número. NULL si falla la
// reserva de memoria.

// PARAMETROS
// n: el entero a convertir.

// La función ft_itoa convierte un número entero n en una cadena de 
// caracteres correspondiente a su representación en base 10. 

// 1-Determinación de la longitud de la cadena resultante contando el 
// número de dígitos en el número entero n
// 2-Asignación de memoria para la nueva cadena utilizando malloc, 
// con un tamaño igual a la longitud calculada más uno para el carácter nulo \0.
// 3-Conversión del número entero en una cadena de caracteres. La función
//  convierte cada dígito del número entero n en un carácter, empezando por 
// el último dígito y avanzando hacia la izquierda
// 4-Manejo del signo del número. Si n es negativo, se coloca el signo - 
// al principio de la cadena y se convierte el valor absoluto de n.
// 5- Inversión de la cadena. Una vez que todos los dígitos se han agregado 
// a la cadena, esta se invierte para que los dígitos estén en el orden 
// correcto
// 6-Devolver la nueva cadena: La función devuelve la nueva cadena que
// contiene la representación de n en formato de caracteres


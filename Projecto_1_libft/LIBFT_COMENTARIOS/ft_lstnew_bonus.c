/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/13 17:06:10 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:54:19 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list	*lista;

	lista = malloc(sizeof(t_list));
	if (!lista)
		return (NULL);
	lista->content = content;
	lista->next = NULL;
	return (lista);
}

/* int main(void)
{
	char	*content = "abcdefg";

	t_list	*printc = ft_lstnew(content);
		
	if (printc != NULL)
	{
		printf("The list is: %s\n", (char *)printc->content);
		free(printc);
	}
	else
	{
		printf("Error: Unable to create a new list node.\n");
	}
	return (0);
} */

/* // Función que crea un nuevo nodo de la lista enlazada
t_list *ft_lstnew(void *content)
{
	t_list *lista; // Declaración de un puntero para el nuevo nodo

	// Asigna memoria para un nuevo nodo de la lista
	lista = malloc(sizeof(t_list));
	
	// Comprueba si la asignación de memoria fue exitosa
	if (!lista)
		return (NULL); // Si la asignación falló, retorna NULL

	// Inicializa el contenido del nuevo nodo con el valor pasado como argumento
	lista->content = content;
	
	// Inicializa el puntero al siguiente nodo como NULL (este será el último 
	nodo de la lista)
	lista->next = NULL;
	
	// Retorna el puntero al nuevo nodo creado
	return (lista);
} */
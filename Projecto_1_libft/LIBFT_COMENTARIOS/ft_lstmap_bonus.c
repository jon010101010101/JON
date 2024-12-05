/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap_bonus.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/14 12:59:32 by jurrutia          #+#    #+#             */
/*   Updated: 2024/05/23 18:51:42 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_lst;
	t_list	*node;
	void	*mapped_content;

	if (!lst || !f || !del)
		return (NULL);
	new_lst = NULL;
	while (lst)
	{
		mapped_content = f(lst->content);
		node = ft_lstnew(mapped_content);
		if (!node)
		{
			del(mapped_content);
			ft_lstclear(&new_lst, del);
			return (NULL);
		}
		ft_lstadd_back(&new_lst, node);
		lst = lst->next;
	}
	return (new_lst);
}

/* void *double_content(void *content)
{
	int *new_content = malloc(sizeof(int));
	if (!new_content)
		return (NULL);
	*new_content = *(int *)content * 2;
	return (new_content);
}

void del(void *content)
{
	free(content);
}

void print_list(t_list *lst)
{
	while (lst)
	{
		printf("%d -> ", *(int *)lst->content);
		lst = lst->next;
	}
	printf("NULL\n");
}

int	main(void)
{
	t_list *list = NULL;
	t_list *new_list = NULL;
	int values[] = {1, 2, 3, 4, 5};
	int i = 0;

	while (i < 5)
	{
		int *value = malloc(sizeof(int));
		if (!value)
			return (1);
		*value = values[i];
		t_list *new_node = ft_lstnew(value);
		if (!new_node)
		{
			free(value);
			ft_lstclear(&list, del);
			return (1);
		}
		ft_lstadd_back(&list, new_node);
		i++;
	}
	printf("Original list:\n");
	print_list(list);
	new_list = ft_lstmap(list, double_content, del);
	printf("Mapped list:\n");
	print_list(new_list);
	ft_lstclear(&list, del);
	ft_lstclear(&new_list, del);

	return (0);
} */

/* DESCRIPCION:Itera la lista ’lst’ y aplica la función ’f’ al contenido de 
cada nodo. Crea una lista resultante de la aplicación correcta y sucesiva
 de la función ’f’ sobre cada nodo. La función ’del’ se utiliza para
 eliminar el contenido de un nodo, si hace falta.

PARAMETROS:
lst: un puntero a un nodo.
f: la dirección de un puntero a una función usada en la iteración de cada
elemento de la lista.
del: un puntero a función utilizado para eliminar
el contenido de un nodo, si es necesario.
 */

/* // Función que aplica una función a cada contenido de una lista y crea 
una nueva lista con los resultados
t_list *ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list  *new_lst;         // Puntero a la nueva lista
	t_list  *node;            // Puntero a un nuevo nodo
	void    *mapped_content;  // Contenido mapeado por la función 'f'

	// Comprueba si la lista 'lst', la función 'f' o la función 'del' son NULL
	if (!lst || !f || !del)
		return (NULL);

	// Inicializa el puntero a la nueva lista como NULL
	new_lst = NULL;

	// Recorre la lista original
	while (lst)
	{
		// Aplica la función 'f' al contenido del nodo actual
		mapped_content = f(lst->content);

		// Crea un nuevo nodo con el contenido mapeado
		node = ft_lstnew(mapped_content);

		// Si no se pudo crear el nuevo nodo
		if (!node)
		{
			// Llama a la función 'del' para liberar el contenido mapeado
			del(mapped_content);

			// Limpia y libera toda la nueva lista creada hasta el momento
			ft_lstclear(&new_lst, del);

			// Retorna NULL indicando un error
			return (NULL);
		}

		// Añade el nuevo nodo al final de la nueva lista
		ft_lstadd_back(&new_lst, node);

		// Avanza al siguiente nodo de la lista original
		lst = lst->next;
	}

	// Retorna el puntero a la nueva lista
	return (new_lst);
} */

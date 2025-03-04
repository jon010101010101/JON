/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/10 13:13:05 by jurrutia          #+#    #+#             */
/*   Updated: 2025/03/04 09:35:55 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include "libft.h"

char	*get_next_line(int fd)
{
	static char	*str[MAX_FD];
	char		*buff;
	int			byte_read;

	if (fd < 0 || BUFFER_SIZE <= 0 || fd > MAX_FD)
		return (NULL);
	buff = (char *)malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!buff)
		return (NULL);
	byte_read = 1;
	while (!ft_strchr(str[fd], '\n') && byte_read != 0)
	{
		byte_read = read(fd, buff, BUFFER_SIZE);
		if (byte_read == -1)
		{
			free(buff);
			free(str[fd]);
			str[fd] = NULL;
			return (NULL);
		}
		buff[byte_read] = '\0';
		str[fd] = ft_strjoin_modified(str[fd], buff);
	}
	free(buff);
	return (ft_line(str, fd));
}

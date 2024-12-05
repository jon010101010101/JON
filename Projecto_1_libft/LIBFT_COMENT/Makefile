# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jurrutia <jurrutia@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/23 17:51:15 by jurrutia          #+#    #+#              #
#    Updated: 2024/05/23 19:04:47 by jurrutia         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a

SOURCES = 		ft_isalpha.c\
				ft_isdigit.c\
			 	ft_isalnum.c\
			 	ft_isascii.c\
			 	ft_isprint.c\
			 	ft_tolower.c\
			 	ft_toupper.c\
			 	ft_strchr.c\
			 	ft_strrchr.c\
			 	ft_strlcpy.c\
			 	ft_strlen.c\
			 	ft_strnstr.c\
			 	ft_bzero.c\
			 	ft_memchr.c\
			 	ft_memcmp.c\
			 	ft_strncmp.c\
			 	ft_atoi.c\
				ft_strlcat.c\
			 	ft_memmove.c\
				ft_memcpy.c\
				ft_memset.c\
			 	ft_calloc.c\
			 	ft_strdup.c\
				ft_putchar_fd.c\
				ft_putendl_fd.c\
				ft_putnbr_fd.c\
				ft_putstr_fd.c\
				ft_strjoin.c\
				ft_substr.c\
				ft_strtrim.c\
				ft_strmapi.c\
				ft_itoa.c\
				ft_striteri.c\
				ft_split.c\

BSOURCES = 		ft_lstnew_bonus.c\
				ft_lstadd_front_bonus.c\
				ft_lstsize_bonus.c\
				ft_lstlast_bonus.c\
				ft_lstadd_back_bonus.c\
				ft_lstdelone_bonus.c\
				ft_lstclear_bonus.c\
				ft_lstiter_bonus.c\
				ft_lstmap_bonus.c\
								
OBJECTS = $(SOURCES:.c=.o) #a variable whose dependency is to convert the . c in .o
BOBJECTS = $(BSOURCES:.c=.o)

CC = gcc #flags
CFLAGS = -Wall -Wextra -Werror 

all: $(NAME)

$(NAME): $(OBJECTS) # create the executable
	@echo "$(GREEN)Compilation $(clr_rmv)of $(YELLOW)$(NAME) $(CLR_RMV)..."
	@ar crs $(NAME) $(OBJECTS)
	@echo "$(GREEN)$(NAME) created$(CLR_RMV) ✓"

bonus: $(OBJECTS) $(BOBJECTS)
	@echo "$(GREEN)Compilation $(clr_rmv)of $(YELLOW)$(NAME) $(CLR_RMV)..."
	ar rcs $(NAME) $(OBJECTS) $(BOBJECTS)
	@echo "$(GREEN)$(NAME) created$(CLR_RMV) ✓"

%.o: %.c # indicators
	$(CC) -c $(CFLAGS) $< -o $@

CLR_RMV := \033[0m 
RED := \033[1;31m
GREEN := \033[1;32m
YELLOW := \033[1;33m
BLUE := \033[1;34m
CYAN := \033[1;36m
RM := rm -f

$(BOBJECTS): %.o: %.c
	$(CC) -c $(CFLAGS) $< -o $@
	
clean: #delete
	rm -f $(OBJECTS) $(BOBJECTS)
	@echo "$(RED)Deleting $(CYAN)$(NAME) $(CLR_RMV)objs ✓"

fclean: clean 
	rm -f $(NAME) 
	@echo "$(RED)Deleting $(CYAN)$(NAME) $(CLR_RMV)binary ✓"

re: fclean all #clean and recompile everything

.PHONY: all clean fclean re
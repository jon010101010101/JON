/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Makefile                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jurrutia <jurrutia@student.42urduliz.co    +#+  +:+       +#+         */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 12:00:00 by jurrutia          #+#    #+#             */
/*   Updated: 2023/10/03 12:00:00 by jurrutia         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

NAME = so_long
CC = cc
CFLAGS = -Wall -Wextra -Werror -g3 -I./include -I./minilibx-linux
LDFLAGS = -L./minilibx-linux -lmlx -lX11 -lXext -lm

MLX_DIR = minilibx-linux
MLX = $(MLX_DIR)/libmlx.a

SRCS = src/main.c src/load_map.c src/load_images.c src/render_game.c \
       src/key_press.c src/player.c src/close_window.c src/error_handling.c \
       src/utils.c src/check_win_condition.c

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) $(MLX) -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re


NAME = so_long

CC = cc
CFLAGS = -Wall -Wextra -Werror -g3 -I./include -I./minilibx-linux -I./libft/include
LDFLAGS = -L./minilibx-linux -L./libft -lft -lmlx -lX11 -lXext -lm

SRCS = src/main.c \
       src/load_map.c \
       src/load_images.c \
       src/render_game.c \
       src/key_press.c \
       src/player.c \
       src/close_window.c \
       src/error_handling.c \
       src/utils.c \
       src/check_win_condition.c \
       src/map_utils.c \
       src/process_line.c \
       src/validate_line_length.c \
       src/read_map_file_line.c \
	   src/load_map_utils.c \
	   src/validate_map.c \
	   src/is_map_rectangular.c \
	   src/is_map_closed.c \
	   src/has_required_components.c \
	   src/save_line.c

OBJS = $(SRCS:.c=.o)

LIBFT_DIR = libft
LIBFT = $(LIBFT_DIR)/libft.a
MLX_DIR = minilibx-linux
MLX = $(MLX_DIR)/libmlx.a

all: $(NAME)

$(NAME): $(OBJS) $(LIBFT) $(MLX)
	$(CC) $(CFLAGS) $(OBJS) $(MLX) -L$(LIBFT_DIR) -lft $(LDFLAGS) -o $(NAME)

$(LIBFT):
	$(MAKE) -C $(LIBFT_DIR)

$(MLX):
	$(MAKE) -C $(MLX_DIR)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(MAKE) -C $(LIBFT_DIR) clean
	rm -f $(OBJS)

fclean: clean
	$(MAKE) -C $(LIBFT_DIR) fclean
	rm -rf $(NAME)

re: fclean all

.PHONY: all clean fclean re

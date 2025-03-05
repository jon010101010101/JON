NAME = so_long
CC = cc
CFLAGS = -Wall -Wextra -Werror -g3
INC = -I./include -I./minilibx-linux -I./libft -I.
LIB = -L./minilibx-linux -lmlx -L./libft -lft -lX11 -lXext -lm

SRC_DIR = src
OBJ_DIR = obj

SRC = $(SRC_DIR)/check_win_condition.c \
      $(SRC_DIR)/close_window.c \
      $(SRC_DIR)/error_handling.c \
      $(SRC_DIR)/init_game.c \
      $(SRC_DIR)/key_press.c \
      $(SRC_DIR)/load_images.c \
      $(SRC_DIR)/load_map.c \
      $(SRC_DIR)/map_reader.c \
      $(SRC_DIR)/map_processor.c \
      $(SRC_DIR)/map_validation.c \
      $(SRC_DIR)/map_utils.c \
      $(SRC_DIR)/main.c \
      $(SRC_DIR)/player.c \
      $(SRC_DIR)/render_game.c \
      $(SRC_DIR)/utils.c

OBJ = $(SRC:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

all: $(NAME)

# Add libft dependency
$(NAME): $(OBJ) libft/libft.a
	$(CC) $(CFLAGS) $(INC) $(OBJ) $(LIB) -o $(NAME)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(OBJ_DIR)
	$(CC) $(CFLAGS) $(INC) -c $< -o $@

# Libft rule
libft/libft.a:
	@$(MAKE) -C libft

clean:
	rm -rf $(OBJ_DIR)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re

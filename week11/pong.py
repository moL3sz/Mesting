import pygame
import numpy as np


from tqdm import tqdm


# SZINE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


SIGN_EMPTY = " "
SIGN_BALL = "o"
SIGN_PLAYER = "x"


# az ablak mérete
SPACE_SIZE = (20, 20)


ZOOM_SIZE = 10

ACTION_IDLE = "IDLE"
ACTION_LEFT = "LEFT"
ACTION_RIGHT = "RIGHT"

ACTIONS = [
    ACTION_IDLE,
    ACTION_LEFT,
    ACTION_RIGHT
]
# tábla kezdő koordinátátja
rect_x = SPACE_SIZE[0] // 2
rect_y = SPACE_SIZE[1] - 1


rect_change_x = 0
rect_change_y = 0


# tábla méretei
rect_size_x = 5
rect_size_to_sides_x = rect_size_x // 2
rect_size_y = 1

# lambda tulajdonságai
ball_x = SPACE_SIZE[0] // 2
ball_y = 1
#
ball_change_x = 1
ball_change_y = 1
ball_size_to_sides = 1

# ez arra kell  hogy az állaptok változásait nyomon tudjuk követni időre

state_to_id = dict()

# összes lehetséges állapotok száma
num_states = SPACE_SIZE[0] * SPACE_SIZE[1] * \
    SPACE_SIZE[0] * SPACE_SIZE[1] * 2 * 2


screen = 0

agent = None


def drawrect(screen, x, y):
    pygame.draw.rect(screen, RED, [(x - rect_size_to_sides_x)*ZOOM_SIZE,
                     y*ZOOM_SIZE, ZOOM_SIZE * rect_size_x, ZOOM_SIZE*rect_size_y])


def encode_state(ball_x, ball_y, rect_x, rect_y, ball_change_x, ball_change_y):
    """Kódólja az adott állapotot"""
    return (ball_x, ball_y, rect_x, rect_y, ball_change_x, ball_change_y)


def reset():
    global rect_x
    global rect_y

    global rect_change_x
    global rect_change_y

    # tábla méretei
    global rect_size_x
    global rect_size_to_sides_x
    global rect_size_y

    # lambda tulajdonságai
    global ball_x
    global ball_y
    #
    global ball_change_x
    global ball_change_y
    global ball_size_to_sides

    ball_change_x = 1
    ball_change_y = 1
    ball_size_to_sides = 1
    # lambda tulajdonságai
    ball_x = SPACE_SIZE[0] // 2
    ball_y = 1

    # tábla visszaállítása
    rect_x = SPACE_SIZE[0] // 2
    rect_y = SPACE_SIZE[1] - 1
    rect_change_x = 0
    rect_change_y = 0
    # tábla méretei
    rect_size_x = 5
    rect_size_to_sides_x = rect_size_x // 2
    rect_size_y = 1


def init_pong():
    """Játék inicializálása"""
    global screen
    global clock

    size = (SPACE_SIZE[0] * ZOOM_SIZE, SPACE_SIZE[1] * ZOOM_SIZE)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong game!")

    clock = pygame.time.Clock()

    print("Pong init")


def play_episodes(n_episodes=10_000, max_epsilon=1.0, min_epsilon=0.05, decay_rate=0.0001, gamma=0.99, learn=True,
                  viz=False, log=False, human=False):
    global rect_x
    global rect_y
    global rect_change_x
    global rect_change_y

    # lambda tulajdonságai
    global ball_x
    global ball_y
    global ball_change_x
    global ball_change_y
    global ball_size_to_sides

    global clock
    global state_to_id

    rewards = []
    epsilon_histroy = []

    # végig megyünk az epizodokon
    for episode in tqdm(range(n_episodes)):
        done = False

        # epszlin csökkentése
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * \
            np.exp(-decay_rate * episode)
        total_reward = 0
        reset()

        # első állapot beállisa
        state = encode_state(ball_x, ball_y, rect_x, rect_y,
                             ball_change_x, ball_change_y)

        if state not in state_to_id:
            state_to_id[state] = len(state_to_id)

        while not done:
            reward = 0

            screen.fill(BLACK)  # type: ignore
            if not human:
                action = agent.act(state=state_to_id[state], epsilon=epsilon)  # type: ignore
                action_name = ACTIONS[action]
                if action_name == ACTION_LEFT:
                    rect_change_x = -1
                elif action_name == ACTION_RIGHT:
                    rect_change_x = 1
                elif action_name == ACTION_IDLE:
                    rect_change_x = 0
                else:
                    print("Error unkonw action", action)
                    exit()
            else:
                action = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            rect_change_x = -1
                        elif event.key == pygame.K_RIGHT:
                            rect_change_x = 1
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            rect_change_x = 0
                        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            rect_change_y = 0
            rect_x += rect_change_x
            rect_y += rect_change_y

            if ball_x < 0:
                ball_x = 0
                ball_change_x *= -1
            elif ball_x > SPACE_SIZE[0]:
                ball_x = SPACE_SIZE[0]
                ball_change_x *= -1
            elif ball_y < 0:
                ball_y = 0
                ball_change_y *= -1
            elif ball_y > SPACE_SIZE[1]:
                ball_y = SPACE_SIZE[1]
                ball_change_y *= -1

            # eltalálta a tényér a labdát
            elif ball_x + ball_size_to_sides >= rect_x + rect_size_to_sides_x and \
                    ball_x - ball_size_to_sides <= rect_x + rect_size_to_sides_x and \
                    ball_y == SPACE_SIZE[1] - 1:

                reward = 1
                ball_change_y *= -1
            # leesett a labda
            elif ball_y > SPACE_SIZE[1] - 1:
                ball_change_y *= -1
                done = True
                reward = -1

            new_state = encode_state(
                ball_x, ball_y, rect_x, rect_y, ball_change_x, ball_change_y)
            if new_state not in state_to_id:
                state_to_id[new_state] = len(state_to_id)

            # labda mozgása

            ball_x += ball_change_x
            ball_y += ball_change_y

            if rect_x - rect_size_to_sides_x < 0:
                done = True
                reward = -1
                rect_x = 0 + rect_size_to_sides_x
            if rect_x > SPACE_SIZE[0] - rect_size_to_sides_x - 1:
                rect_x = SPACE_SIZE[0] - rect_size_to_sides_x - 1
                done = True
                reward = -1
            
            if viz:
                # labda
                pygame.draw.rect(screen, WHITE,  # type: ignore
                                 [(ball_x - ball_size_to_sides) * ZOOM_SIZE,
                                  (ball_y - ball_size_to_sides) * ZOOM_SIZE,
                                  ball_size_to_sides * ZOOM_SIZE,
                                  ball_size_to_sides * ZOOM_SIZE])
                drawrect(screen, rect_x, rect_y)

                pygame.display.flip()
                clock.tick(60)

            if learn:
                agent.learn(state_to_id[state], action, reward, state_to_id[new_state],gamma) #type: ignore
            
            state = new_state
            total_reward += reward

        if log:
            print("Total reward: ", total_reward)
        rewards.append(total_reward)
        epsilon_histroy.append(epsilon)

    return rewards, epsilon_histroy


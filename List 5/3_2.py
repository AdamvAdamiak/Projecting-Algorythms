import pygame
from robots0 import create_robots


def refill():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(20)


def quicksort(array, l, r):
    if l < r:
        pi = partition(array, l, r)
        quicksort(array, l, pi - 1)
        refill()
        for i in range(0, pi + 1):
            arr_clr[i] = clr[3]
        quicksort(array, pi + 1, r)


def partition(array, low, high):
    pygame.event.pump()
    pivot = array[high]
    arr_clr[high] = clr[2]
    i = low - 1
    for j in range(low, high):
        arr_clr[j] = clr[1]
        refill()
        arr_clr[high] = clr[2]
        arr_clr[j] = clr[0]
        arr_clr[i] = clr[0]
        if array[j] < pivot:
            i = i + 1
            arr_clr[i] = clr[1]
            array[i], array[j] = array[j], array[i]
    refill()
    arr_clr[i] = clr[0]
    arr_clr[high] = clr[0]
    array[i + 1], array[high] = array[high], array[i + 1]

    return (i + 1)


def draw():
    element_width = (width - 150) // 150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0),
                     (0, 95), (900, 95), 6)

    for i in range(1, 100):
        pygame.draw.line(screen, arr_clr[i], (boundry_arr * i - 3, 100),
                         (boundry_arr * i - 3, array[i] * boundry_grp + 100), element_width)


if __name__ == '__main__':
    robots = create_robots(100)
    robots_resolutions = []
    for robot in robots:
        robots_resolutions.append(int(robot[4]))

    screen = pygame.display.set_mode(
        (600, 400)
    )

    pygame.display.set_caption("Quicksort visualise")
    run = True

    width = 900
    length = 500
    array = robots_resolutions
    arr_clr = [(0, 204, 102)] * 100
    clr = [(0, 204, 102), (255, 0, 0),
           (0, 0, 153), (255, 102, 0)]

    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    quicksort(array, 1, len(array) - 1)
        draw()
        pygame.display.update()
    pygame.quit()

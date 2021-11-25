import time
import pygame

class timer:
    def __init__(self):
        self.time_left = 20  # duration of the timer in seconds
        self.font = pygame.font.SysFont("Arial", 30)
        self.color = (255, 255, 255)
        self.startTime = time.time()
        self.text = self.font.render("", True, self.color)

    def startCount(self, run):
        nowTime = time.time()
        # time_left = nowTime - startTime
        showTime = self.time_left - (nowTime - self.startTime)
        total_mins = showTime // 60  # minutes left
        total_sec = showTime - (60 * (total_mins))  # seconds left
        if showTime >= 0:
            self.text = self.font.render(("Time left: " + str(int(total_mins)).zfill(2) +
                                          ":" + str(int(total_sec)).zfill(2)), True, self.color)
            # time.sleep(1)  # making the time interval of the loop 1sec
        else:
            self.text = self.font.render("Time Over!!", True, self.color)
            run.clear()
            run.append(0)

            # screen.blit(text, (200, 200))
    def setStart(self, sec):
        self.startTime = time.time()
        self.time_left = sec

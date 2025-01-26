import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# پنجره بازی
wn = turtle.Screen()
wn.title("snake lady")
wn.bgcolor("light blue")
wn.setup(width=600, height=600)
wn.tracer(0)  # غیرفعال کردن انیمیشن

# سر مار
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# غذا
food = turtle.Turtle()
food.speed(0)
colors = random.choice(['pink', 'yellow', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)


segments = []
# امتیاز
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score : 0 High Score : 0", align="center", font=("courier", 24, "bold"))

# موانع
obstacles = []
for _ in range(5):  # تعداد موانع
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    obstacle.goto(x, y)
    obstacles.append(obstacle)
    
# کنترل‌های مار
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# کلیدهای کنترل
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

# حلقه اصلی بازی
while True:
    wn.update()

    time.sleep(delay)

    # بررسی برخورد با دیوار
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # پاک‌سازی بخش‌های مار
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # بازنشانی امتیاز
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    # بررسی برخورد با غذا
    if head.distance(food) < 20:
        # تولید غذا در موقعیت تصادفی
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # اضافه کردن یک بخش جدید به مار
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # رنگ دم
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        # افزایش امتیاز
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        


    # حرکت مار
    move()

    # به‌روزرسانی موقعیت بخش‌های مار
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # بررسی برخورد با خود
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # پاک‌سازی بخش‌های مار
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # بازنشانی امتیاز
            score = 0
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

# بررسی برخورد با موانع
    for obstacle in obstacles:
        if head.distance(obstacle) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # پاک‌سازی بخش‌های مار
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # بازنشانی امتیاز
            score = 0
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))

    time.sleep(delay)

wn.mainloop()

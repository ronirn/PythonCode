import turtle

def draw_text(text, font_size, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black")
    turtle.write(text, font=("Arial", font_size, "normal"))

def draw_love(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(size)
    turtle.circle(size, 200)
    turtle.right(140)
    turtle.circle(size, 200)
    turtle.forward(size)
    turtle.end_fill()

def main():
    turtle.speed(2)
    turtle.bgcolor("lightblue")

    # Tulisan "I LOVE RAHADATUL AISY"
    draw_text("I LOVE RAHADATUL AISY", 20, -200, 100)

    # Gambar "LOVE"
    draw_love(0, -50, 50)

    turtle.hideturtle()
    turtle.done()

# Panggil fungsi utama untuk membuat gambar
main()

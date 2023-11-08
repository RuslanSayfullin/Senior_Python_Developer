import vispy
from vispy import app, gloo

# Создаем окно
canvas = app.Canvas(keys='interactive')

# Создаем простой ьреугольник
vertex = """
attribute vec2 a_position;
void main (void) {
    gl_Position = vec4(a_position, 0.0, 1.0);
}
"""

fragment = """
void main()
{
    gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

program = gloo.Program(vertex, fragment)
program['a_position'] = [(-0.6, -0.6), (0.6, -0.6), (0.0, 0.6)]

@canvas.connect
def on_draw(event):
    gloo.clear()
    program.draw('triangles')

if __name__ == '__main__':
    canvas.show()
    app.run()

import matplotlib.pyplot as plt

def midpoint_circle(radius):
    points = []
    x = radius
    y = 0
    p = 1 - radius
    def add_symmetrical_points(x, y):
        points.append((x, y))
        points.append((y, x))
        points.append((-x, y))
        points.append((-y, x))
        points.append((-x, -y))
        points.append((-y, -x))
        points.append((x, -y))
        points.append((y, -x))
    add_symmetrical_points(x, y)
    
    while x >=y:
        y += 1
        
        if p <= 0:
            p = p + 2*y + 1  
        else:
            x -= 1
            p = p + 2*y - 2*x + 1  
               
        add_symmetrical_points(x, y)

    return points

def plot_circle(radius):
    points = midpoint_circle(radius)
   
    x_points, y_points= zip(*points)
       
    plt.figure(figsize=(6,6))
    plt.scatter(x_points, y_points, color='blue', s=1)
    plt.xlim(-radius - 1, radius + 1)
    plt.ylim(-radius - 1, radius + 1)
    plt.title(f"Midpoint Circle Drawing Algorithm (radius = {radius})")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Midpoint Circle Algorithm")
    plt.grid()
    plt.show()

plot_circle(500)

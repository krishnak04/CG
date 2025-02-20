import matplotlib.pyplot as plt

def midpoint_ellipse(a, b):

    x = 0
    y = b
    a2 = a * a  
    b2 = b * b 
    dx = 2 * b2 * x
    dy = 2 * a2 * y
    points = []
    
    def add_symmetrical_points(x, y):
        points.append((x,y))
        points.append((-x,y))
        points.append((x,-y))
        points.append((-x,-y))
        
    p1 = b2 - a2 * b + 0.25 * a2  
    while dx < dy:
        x += 1
        dx = dx + 2 * b2
        if p1 < 0:
            p1 = p1 + dx + b2
        else:
            y -= 1
            dy = dy - 2 * a2
            p1 = p1 + dx - dy + b2
        add_symmetrical_points(x, y)
      
    p2 = b2 * (x + 0.5) ** 2 + a2 * (y - 1) ** 2 - a2 * b2
    while y >= 0:
        y -= 1
        dy = dy - 2 * a2
        if p2 > 0:
            p2 = p2 + a2 - dy
        else:
            x += 1
            dx = dx + 2 * b2
            p2 = p2 + dx - dy + a2
        add_symmetrical_points(x, y)
    
    return points

def plot_ellipse(a, b):
    points = midpoint_ellipse(a, b)
    x_points, y_points = zip(*points)   
    plt.figure(figsize=(6,6))
    plt.scatter(x_points, y_points, color='blue', s=1)
    plt.title(f"Midpoint Ellipse Drawing Algorithm (a = {a}, b = {b})")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Midpoint Ellipse Algorithm")
    plt.grid()
    plt.show()

plot_ellipse(1000, 500)

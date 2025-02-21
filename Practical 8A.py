INSIDE = 0 # 0000 
LEFT = 1 #0001 
RIGHT = 2 # 0010  
BOTTOM= 4 # 0100 
TOP = 8 
# 1000 
def compute_code(x, y, x_min, y_min, x_max, y_max): 
    code = INSIDE 
    if x < x_min: 
       code  |= LEFT 
    elif x > x_max: 
       code |=RIGHT 
    if y < y_min:  
       code |=BOTTOM 
    elif y > y_max:   
       code |= TOP 
    return code 
def cohen_sutherland (x0, y0, x1, y1, x_min, y_min, x_max, y_max): 
    code0=compute_code (x0, y0, x_min, y_min, x_max, y_max) 
    code1=compute_code(x1, y1, x_min, y_min, x_max, y_max) 
    accept=False
    
    while True: 
          if (code0 == 0) and (code1 == 0):
              accept = True 
              break 
          elif (code0 & code1) != 0:
              break
          else: 
              code_out = code0 if code0 != 0 else code1
              x, y = 0,0 

              if code_out & TOP: 
                  x = x0 + (x1-x0) * (y_max - y0) / (y1-y0)
                  y=y_max 
              elif code_out & BOTTOM: 
                  x = x0 + (x1-x0) * (y_min - y0) / (y1-y0)
                  y=y_min 
              elif code_out & RIGHT:
                  y = y + (y1-y0) * (x_max - x0) / (x1-x0)
                  x = x_max 
              elif code_out & LEFT: 
                  y = y + (y1-y0) * (x_min - x0) / (x1-x0)
                  x=x_min 

              if code_out == code0:
                x0,y0 = x,y 
                code0 = compute_code (x0, y0, x_min, y_min, x_max, y_max) 
              else:
                x1,y1 = x,y
                code1 = compute_code(x1, y1, x_min, y_min, x_max, y_max) 
    if accept: 
        return (x0, y0,x1,y1) 
    else: 
        return None  

if __name__ == "__main__": 

    x_min, y_min = 15 ,15 
    x_max, y_max = 25 ,25 
 
    x0, y0 = 10,10
    x1, y1 = 60,30
    clipped_line = cohen_sutherland (x0, y0,x1,y1, x_min, y_min, x_max, y_max ) 
    if clipped_line: 
        print(f"Clipped line segment: {clipped_line}") 
    else: 
        print("Line segment is completely outside the clipping window.")
        

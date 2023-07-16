import math
def calculate_dist(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def check_triangle(x1,x2,x3,y1,y2,y3):
    s1 = calculate_dist(x1,x2,y1,y2)
    s2 = calculate_dist(x2,x3,y2,y3)
    s3 = calculate_dist(x3,x1,y3,y1)
    
    if s1+s2>s3 and s2+s3>s1 and s3+s1>s2:
        return True
    else:
        return False
    
def main():
    x1, y1 = 1, 1
    x2, y2 = 4, 2
    x3, y3 = 2, 5
    
    if check_triangle(x1,x2,x3,y1,y2,y3):
        print("Triangle") 
    else:
        print("Not a triangle") 

if __name__ == "__main__":
    main()
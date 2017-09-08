from matplotlib import pyplot as plt
import time

f = plt.figure(1, figsize = (8,8))
ax = f.gca()
ax.set_xlim([0, 10000])
ax.set_ylim([0, 10000])
f.show()

# Assuming x2 > x1 and y2 > y1
x1 = 0.0
y1 = 0.0
x2 = 10000.0
y2 = 5000.0

dx = x2 - x1
dy = y2 - y1
slope = abs(dy / dx)

error = 0.0
y = y1
x = x1

begin = time.time()
while x < x2:
    ax.plot(x, y, 'ko')
    f.canvas.draw()
    x = x + 1
    error = error + slope
    if error >= 0.5:
        y = y + 1
        error -= 1.0
    # raw_input('pause : press any key ...')
end = time.time()
print('Time spent: {}'.format(end - begin))
f.close()

'''
 function line(x0, y0, x1, y1)
     real deltax := x1 - x0
     real deltay := y1 - y0
     real deltaerr := abs(deltay / deltax)    // Assume deltax != 0 (line is not vertical),
           // note that this division needs to be done in a way that preserves the fractional part
     real error := 0.0 // No error at start
     int y := y0
     for x from x0 to x1 
         plot(x,y)
         error := error + deltaerr
         if error >= 0.5 then
             y := y + 1
             error := error - 1.0
'''
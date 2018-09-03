import random
import pygame

def update_map(scr, clk, pos):
	
		
	pygame.draw.line(scr, (0, 0, 0), pos, pos)
	pygame.display.update()
	clk.tick(60)

def largest_hist(nums, sdim):
	i = 0
	h = 0
	max_area = 0
	while i < sdim:
		w = 0
		if nums[i] > 0:
			h = nums[i]

			j = i
			#Look back 
			while j >= 0:
				if nums[j] >= h:
					
					w += 1

				else:
					j = -1
				j -= 1
			#Look forward 
			j = i + 1
			while j < sdim:
				if nums[j] >= h:
					
					w += 1

				else:
					j = 999
				j += 1

		
		area = h * w
		if area > max_area:
			max_area = area
			max_h = h
			max_w = w
		i += 1
		
	return max_area, max_w, max_h
		
def largest_rec(city, sdim):
	current_stack = []
	max_a = 0
	max_w = 0
	max_h = 0
	
	for i in range(0, sdim):
		current_stack.append(0)
		
	count = 0	
	for row in city:
		count += 1
		k = 0
		ma = 0
		mw = 0
		mh = 0
		
		while k < sdim:
			if row[k] == 0:
				current_stack[k] = 0
				#print("k = " + str(k) + "Row = " + str(count))
			else:
				current_stack[k] += row[k] 	
			k += 1		
		
		#print(current_stack)
		#input()	
		
	#print(current_stack)
	ma, mw, mh = largest_hist(current_stack, sdim)
	#print(str(ma) + " " + str(mw) + " " + str(mh))
	
	if ma > max_a:
		max_a = ma
		max_w = mw
		max_h = mh
			
			
			
	return max_a, max_w, max_h



#Generate empty london
london = []

pygame.init()

sdim = 500
bombs = 5000

black = (0,0,0)
white = (255, 255, 255)
screen = pygame.display.set_mode((sdim, sdim))
clock = pygame.time.Clock()
screen.fill(white)
pygame.display.update()

for i in range(0, sdim):
	london.append([])

for l in london:
	for i in range(0, sdim):
		l.append(1)
		

#Drop 800 bombs, some will double up
c = 0
new = 0

max_area, max_width, max_height = largest_rec(london, sdim)

#print("[" + str(c) + " bombs] - Max area: " + str(max_area) + "( " + str(max_width) + " x " + str(max_height) + ")")

ratio = max_area/sdim*sdim*100
print(str(ratio) + "%")

running = True

while c < bombs and running:
	rx = random.randint(0, (sdim-1))
	ry = random.randint(0, (sdim-1))
	
	if london[ry][rx] != 0:
		london[ry][rx] = 0
		new += 1
		
	c += 1
	
	update_map(screen, clock, (rx, ry))
	
	max_area, max_width, max_height = largest_rec(london, sdim)

	#print("[" + str(c) + " bombs] - Max area: " + str(max_area) + "( " + str(max_width) + " x " + str(max_height) + ")")
	ratio = max_area/(sdim*sdim)*100
	print(str(ratio) + "% -- (" + str(max_width) + " x " + str(max_height) + ")")
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	

input()



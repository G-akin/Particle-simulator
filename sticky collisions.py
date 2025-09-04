import pygame
pygame.init()
clock = pygame.time.Clock()
import random
genn=100
psize=15
#tickrate
tickrate = 60
class esprite():
    def __init__(self,espawn=200,esize=5,floor=500,lwall=0,rwall=700,xspawn=100,yspawn=100,rgb=(90,120,200)):
        self.rgb=rgb
        self.xspawn=xspawn
        self.yspawn=yspawn
        self.esize=esize
        self.rect=pygame.Rect(xspawn,yspawn,esize,esize)
        self.vel =(random.randint(-2,2),random.randint(-2,2))
        self.restitution=1.1
        
    def drawe(self):
        pygame.draw.rect(screen,(self.rgb), self.rect)

    def randommove(self):
        self.rect.clamp_ip(0,0,700,500)   
        # self.rect.x+=random.randint(-2,2)
        # self.rect.y+=random.randint(-2,2)

    def vel_move(self):
        # self.vel.x+=dx
        # self.vel.y+=dy
        self.rect.x+=self.vel[0]
        self.rect.y+=self.vel[1]
            
    def bounce(self):
        pass
        for other_particle in objlist:
            if self.rect.colliderect(other_particle.rect) and other_particle!=self:
                # print("Collis")
                sigma_vel=(self.vel[0]+other_particle.vel[0],self.vel[1]+other_particle.vel[1]) #*self.restitution
                self.vel=(sigma_vel[0]/2,sigma_vel[1]/2)
                other_particle.vel=(sigma_vel[0]/2,sigma_vel[1]/2)
                
def generate_objects(count):
    """Generates a list of Item objects."""
    particles = []
    for i in range(count):
        name = f"Object_{i+1}"
        particles.append(esprite(name,psize,500,0,700,random.randint(0,700),random.randint(0,500),(2*random.randint(0,125),2*random.randint(0,125),2*random.randint(0,125))))
    return particles

def process_objects(objects):
    """Calls the sub-procedure for each object."""
    for obj in objects:
        obj.drawe()
        obj.randommove()
        obj.bounce()
        obj.vel_move()
objlist=generate_objects(genn)

SCREEN_W = 750
SCREEN_H =  600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

run= True
while run:
    clock.tick(tickrate)
    screen.fill((255,255,255))    
    process_objects(objlist)
    # print(clock.get_fps())
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
    #display update              
    pygame.display.update()
#game end
pygame.quit()

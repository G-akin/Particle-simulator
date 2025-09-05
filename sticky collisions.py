import pygame
pygame.init()
clock = pygame.time.Clock()
import random
genn=100
sqsize=15
psize=(sqsize,sqsize)
#tickrate
tickrate = 60
class esprite():
    def __init__(self,esize=(5,5),espawn=(100,100),
                 floor=550,ceiling=0,
                 lwall=0,rwall=650,
                 rgb=(90,120,200),start_vel=[random.randint(-2,2),random.randint(-2,2)]):
        self.rgb=rgb
        # self.xspawn=xspawn
        # self.yspawn=yspawn
        self.esize=esize
        self.rect=pygame.Rect(espawn[0],espawn[1],esize[0],esize[1])
        self.vel =start_vel
        self.restitution=1.0
        self.floor=floor
        self.lwall=lwall
        self.rwall=rwall
        self.ceiling=ceiling
        self.collided=False
        self.g= 0.0
    def drawe(self):
        pygame.draw.rect(screen,(self.rgb), self.rect)

    def gravity(self):
        # print("1",self.vel[1])
        if self.rect.y<self.floor+self.g:
            self.vel[1]+=self.g
            # print("2",self.vel[1])
        

    def randommove(self):
##        self.rect.clamp_ip(0,0,700,500)   
        self.rect.x+=random.randint(-3,3)
        self.rect.y+=random.randint(-3,3)

    def vel_move(self):
        # self.vel.x+=dx
        # self.vel.y+=dy
        self.rect.x+=self.vel[0]
        self.rect.y+=self.vel[1]
        # self.rect.clamp_ip(0,0,700,500) 
            
    def wall_bounce(self):
        if self.rect.x<self.lwall:
            self.vel[0]=abs(self.vel[0])*self.restitution
            # print(self.vel[0])
        if self.rect.x>self.rwall:
            self.vel[0]= -abs(self.vel[0])*self.restitution
            # print(self.vel[0])
        if self.rect.y<self.ceiling:
            self.vel[1]=abs(self.vel[1])*self.restitution
            # print(self.vel[1])
        if self.rect.y>self.floor:
            self.vel[1]= -abs(self.vel[1])*self.restitution
            # self.vel[1]=-math.sqrt(self.vel[1]**2)*self.restitution
            # print(self.vel[0])

    def particle_collision(self):
        for other_particle in objlist:
            if other_particle!=self and self.rect.colliderect(other_particle.rect) and self.collided==False and other_particle.collided==False:
                print("Collis")
                if self.rect.x>other_particle.rect.x:
                    self.rect.x+=self.esize[0]-(self.rect.x-other_particle.rect.x)
                    other_particle.rect.x-=self.esize[0]-(self.rect.x-other_particle.rect.x)
                
                elif self.rect.x<other_particle.rect.x:
                    self.rect.x+=self.esize[0]-(self.rect.x-other_particle.rect.x)
                    other_particle.rect.x-=self.esize[0]-(self.rect.x-other_particle.rect.x)

                # elif self.rect.x<other_particle.rect.x:
                #     self.rect.x+=self.esize[0]-(self.rect.x-other_particle.rect.x)
                #     other_particle.rect.x

                    # self.rect.x+=self.esize[0]/2
                    # other_particle.rect.x-=self.esize[0]/2
                sigma_vel=(self.vel[0]+other_particle.vel[0],self.vel[1]+other_particle.vel[1]) #*self.restitution
                self.vel=[-sigma_vel[0]/2,-sigma_vel[1]/2]
                # other_particle.vel=[sigma_vel[0]/2,sigma_vel[1]/2]
                self.collided=True
            else:
                self.collided=False

    def run(self):
        # self.collided=False
        # self.drawe()
        # self.randommove()
        self.particle_collision()
        # self.wall_bounce()
        self.gravity()
        self.wall_bounce()
        self.vel_move()
        self.drawe()


def generate_objects(count):
    # Generates a list of Item objects
    particles = []
    for i in range(count):
        lwall=0
        rwall=650
        floor=550
        ceiling=0
        vel_mag_range=4
        name = f"Object_{i+1}"
        name =esprite(esize=psize,espawn=(random.randint(lwall,rwall),random.randint(ceiling,floor)),
                      floor=floor,ceiling=ceiling,lwall=lwall,rwall=rwall,
                      rgb=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
                      start_vel=[random.randint(-vel_mag_range,vel_mag_range),random.randint(-vel_mag_range,vel_mag_range)])
        particles.append(name)
        

            

    return particles

def process_objects(objects):
    # Calls the sub-procedure for each object
    for obj in objects:
        obj.run()
objlist=generate_objects(genn)

floorline=esprite(esize=(700,3),espawn=(0,550+sqsize),
                      floor=0,ceiling=0,lwall=0,rwall=0,
                      rgb=(0,0,0))

SCREEN_W = 750
SCREEN_H =  600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

run= True
while run:
    clock.tick(tickrate)
    screen.fill((255,255,255))    
    process_objects(objlist)
    floorline.drawe()
    # print(clock.get_fps())
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            run = False
    #display update              
    pygame.display.update()
#game end
pygame.quit()

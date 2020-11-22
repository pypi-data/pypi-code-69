import pygame


class Player(object):

    def __init__(self, is_player_one, display):
        """
        Super Class for all characters
        :param is_player_one: (bool) is player one or player two
        :param display: (surface) game display
        """

        #Screen variables
        self.display = display
        self.window_size = pygame.display.get_window_size()
        self.floor = self.window_size[1]-228
        
        #Player direction
        self.right = False
        self.left = False
        self.jumping = False

        #Attack variables
        self.basic_attack_left = False
        self.basic_attack_right = False
        self.attack_hitbox = []
        self.attacked = False
        self.alive = True
    
        #Frames movement variables
        self.speed = 8
        self.yspeed = 0
        self.framecount = 0
        self.attack_count = 0
        self.walk_sprites = 9

        #Define player as one or two
        self.is_player_one = is_player_one
        if self.is_player_one:
            self.standingRight = True
            self.standingLeft = False
            self.position = [10,self.floor]
        else:
            self.standingLeft = True
            self.standingRight = False
            self.position = [self.window_size[0]-138,self.floor]

        """
        Characther atributes
        set them to None to be assigned by subclass
        """
        self.max_health = None
        self.health = None
        self.health_percentage = None
        self.base_damage = None
        self.size = None
        self.hitbox = None
        
    def draw(self, sprites, font):
        if self.basic_attack_left:
            self.display.blit(sprites['BAL'+str((self.attack_count//3)%4)], self.position)
            self.attack_count += 1

        elif self.basic_attack_right:
            self.display.blit(sprites['BAR'+str((self.attack_count//3)%4)], self.position)
            self.attack_count += 1

        elif self.standingRight:
            self.display.blit(sprites['WR0'], self.position)

        elif self.standingLeft:
            self.display.blit(sprites['WL0'], self.position)

        elif self.right:
            self.display.blit(sprites['WR'+str(1+(self.framecount//3)%self.walk_sprites)], self.position)
            self.framecount += 1

        elif self.left:
            self.display.blit(sprites['WL'+str(1+(self.framecount//3)%self.walk_sprites)], self.position)
            self.framecount += 1

        self.health_bar(font)
        self.show_hitbox(False) #Develper Tool

    def health_bar(self, font):
        self.health_percentage = self.health/self.max_health
        color = (0,0,0)
        if self.health_percentage > 0.7:
            color = (0,255*self.health_percentage,0)
        elif self.health_percentage > 0.2:
            color = (
                50+255*(1-self.health_percentage),
                255*self.health_percentage*1.3,0,
                )
        else:
            color = (255*(1-self.health_percentage),0,0)
            
        if self.is_player_one:
            health_bar_rect = self.health_bar_rect(0.05, 0, color)
        else:
            health_bar_rect = self.health_bar_rect(
                0.55, 
                self.window_size[0]*0.4*(1-self.health_percentage), 
                color,
            )

        self.character_name(health_bar_rect.left, health_bar_rect.right,font)
           
    def health_bar_rect(self, initial_position, reverse_position, color):
        pygame.draw.rect(
            self.display,(200,100,100),
            (
                self.window_size[0]*initial_position-2,
                self.window_size[1]*0.05-2,
                self.window_size[0]*0.4+4,
                self.window_size[1]*0.03+4
            )
        )
        rect = pygame.draw.rect(
            self.display,(200,200,200),
            (
                self.window_size[0]*initial_position,
                self.window_size[1]*0.05,
                self.window_size[0]*0.4,
                self.window_size[1]*0.03
            ),
        )
        pygame.draw.rect(
            self.display,color,
            (
                self.window_size[0]*initial_position+reverse_position,
                self.window_size[1]*0.05,
                self.window_size[0]*0.4*self.health_percentage,
                self.window_size[1]*0.03
            )
        )

        return rect

    def character_name(self, left, right, font_name):
        font = pygame.font.Font(font_name, 20)
        name = font.render(self.name,True,(0,0,0))
        name_rectangle = name.get_rect()

        if self.is_player_one:
            name_rectangle.left = left
        else:
            name_rectangle.right = right

        name_rectangle.top = self.window_size[1]*0.1
        self.display.blit(name, name_rectangle)

    def show_hitbox(self, show):
        if show:
            pygame.draw.rect(self.display,(235, 64, 52),self.hitbox,4)
            if self.attacked:
                pygame.draw.rect(self.display, (235, 64, 52), self.attack_hitbox, 4)

    def move_hitbox(self):
        self.hitbox = pygame.Rect(
            (self.position[0]+self.size[0], self.position[1]+self.size[2]),
            (self.size[1], self.size[3]),
        )

    """
    Player actions
        Stand
        Move Right
        Move Left
        Jump
        Basic Attack
    """
    def stand(self):
        if self.right:
            self.standingRight = True
            self.right = False
        elif self.left:
            self.standingLeft = True
            self.left = False

    def move_right(self):
        if self.hitbox[0] < self.window_size[0] - self.size[0] -self.speed:
            self.position[0] += self.speed
            self.right = True
            self.left = False
            self.standingRight = False
            self.standingLeft = False
            self.move_hitbox()
        else:
            self.stand()

    def move_left(self):
        if self.hitbox[0] > self.speed:
            self.position[0] -= self.speed
            self.right = False
            self.left = True
            self.standingRight = False
            self.standingLeft = False
            self.move_hitbox()
        else:
            self.stand()

    def jump(self):
        gravity = 20
        if self.jumping:
            if self.position[1] <= self.floor:
                self.position[1] -= self.yspeed
                if self.position[1] > self.floor:
                    self.position[1] = self.floor + 1
                self.yspeed -= gravity
            else:
                self.position[1] = self.floor
                self.yspeed = 0
                self.jumping = False
        else:
            self.jumping = True
            self.yspeed = 100
        self.move_hitbox()

    def basic_attack(self, other_player):
        if self.right or self.standingRight:
            self.basic_attack_right = True
            self.basic_attack_left = False
        elif self.left or self.standingLeft:
            self.basic_attack_left = True
            self.basic_attack_right = False

        if self.attack_count > 9:
            self.basic_attack_left = False
            self.basic_attack_right = False
            self.attack_count = 0
        elif self.attack_count == 7:
            direction = 0
            if self.basic_attack_right:
                direction = 40
            else:
                direction = -40
            self.attacked = True
            self.attack_hitbox = (pygame.Rect(
                (self.position[0]+self.size[1]+direction, self.position[1] + self.size[3]/3),
                (40, 40),
            ))

            if self.attack_hitbox.colliderect(other_player.hitbox):
                other_player.health -= self.base_damage
                if other_player.health < 0:
                    other_player.health = 0
            
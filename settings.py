


class Settings:

    def __init__(self):
        #screen settings
        self.screen_width=800
        self.screen_height=1200
        self.bg_color=(230,230,230)
        #ship settings
        self.ship_speed=2
        self.ship_limit=3
        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed = 10.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1




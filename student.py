#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 80
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''

    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""

        
        if not self.safe_to_dance():
            return False # Shut the dance down


        for x in range(1): # The only way I can get the code to run right is to not use the loop
            self.forward_skipp()
            time.sleep(.5)
            self.right_twirl()
            time.sleep(.1)
            self.left_twirl()
            time.sleep(.8) # I have to add time.sleep because the robot's motor will overheat
            self.cha_cha()
            time.sleep(.8)
            self.laberinth()
            time.sleep(.5)
            self.cha_cha()
            time.sleep(.5)
            self.forward_skipp()
            time.sleep(.5)
            self.right_twirl()
            time.sleep(.1)
            self.left_twirl()
            time.sleep(.8)
            self.cha_cha()
            time.sleep(.8)
            self.laberinth()
            time.sleep(.5)
            self.cha_cha()
            time.sleep(.5)


        self.wheelie_time()
        self.stop()
            

            # look for more moves

    def forward_skipp(self):
        """this is my first move"""
        for x in range(3):
            self.fwd(right=100, left=100)
            time.sleep(.5)
            self.servo(1000)# Head is moving while stopped
            time.sleep(.1)
            self.servo(2000)
            time.sleep(.1)
            self.fwd(right=-100, left=-100)# Goes back to make a skip and a wheelie
            time.sleep(.1)
            self.servo(-1000)
            self.stop()
        
        
        # Then I twist to the right 
    def right_twirl(self):
        """ First spin going to the right"""
        for x in range(2):
            self.turn_by_deg(180) # spins 2 times to the right
            self.turn_by_deg(180)
            self.stop()

        # in the spin, the robot should be in a wheelie    

    def left_twirl(self):
        """ Second spin going the left"""
        for x in range(2):
            self.turn_by_deg(-170)# spins 2 times to the left
            self.turn_by_deg(-170)
            self.stop()

         # should be in a wheelie

    def cha_cha(self):
        """ Does a cha cha backwards"""
        for x in range(4):
            self.back()
            time.sleep(.3)
            self.servo(1000) # head should be moving while backing up
            time.sleep(.3)
            self.servo(2000)
            time.sleep(.3)
            self.fwd() # moves the cha cha foward and created a small wheelie
            time.sleep(.3)
            self.stop()

        # cha cha should backup and go foward four times

    def laberinth(self):   # Thanks Haydyn for the code! # I changed the timeing a little from Haydyn's
        """Moves like a snake!"""
        for x in range(4):
            self.servo(1000) 
            time.sleep(.1)
            self.right(primary=70, counter=30)
            time.sleep(1)
            self.servo(2000)
            time.sleep(.1) # time makes each turn longer and wider
            self.left(primary=70, counter=30)
            time.sleep(1)
        self.stop()

        # should move in a laberinth pattern

    def wheelie_time(self): 
        """THE GRAND FINALE!"""
        self.fwd(right=100, left=100) # goes backwards, to make some room
        time.sleep(.5)
        self.fwd(right=-100, left=-100) # Pops a wheelie and spins
        time.sleep(.3)
        for x in range(2):
            self.turn_by_deg(180)
            self.turn_by_deg(180)
            self.stop()

         # This is the last part of the dance, and only happens once after the loop          

    def safe_to_dance(self):
        """ Does a 360 distance check and returns true if safe """
        # Check for all fail/early-termination conditions
        for _ in range(4):
            if self.read_distance()< 600:
                print("NOT SAFE TO DANCE!!!")
                return False
            else:
                self.turn_by_deg(90)
            
        # After all checks have been done. We deduce it's safe   
        print("SAFE TO DANCE!")
        return True   

    def shake(self):
        self.deg_fwd(720)
        self.stop()
        self.back(720)
        self.stop()
    
    
    def example_move(self):
        
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  

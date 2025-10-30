class Robot:
    active_count = 0

    def __init__(self, name):
        self.name = name
        self.alive = True              
        Robot.active_count += 1
        print(f"Robot {self.name} has been activated.")

    def remove(self):
        if self.alive:
            self.alive = False
            Robot.active_count -= 1
            print(f"Robot {self.name} has been deactivated.")
        else:
            print(f"Robot {self.name} is already deactivated.")

    @classmethod
    def number_active(cls):
        print(f"Number of active robots: {cls.active_count}")



r1 = Robot("A")
r2 = Robot("B")

Robot.number_active()  
r1.remove()            
r1.remove()            
Robot.number_active() 
r2.remove()
r2.remove()
Robot.number_active() 
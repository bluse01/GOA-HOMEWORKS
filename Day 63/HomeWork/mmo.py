class Hero(object):
    def __init__(self, inte=15, speed=.1, dm=5):
        self.inte = inte
        self.speed = speed
        self.damage = dm
        
def check(p1, p2):
    p1_point = 0
    p2_point = 0
    
    if p1.damage > p2.damage:
        p1_point += 1
    elif p2.damage > p1.damage:
        p2_point += 1
        
    if p1.speed > p2.speed:
        p1_point += 2
    elif p2.speed > p2.speed:
        p2_point += 2

    p1_point += ((p1.speed + p1.damage) ** 2) / 10
    p2_point += ((p2.speed + p2.damage) ** 2) / 10
        
    if p1_point > p2_point:
        return f"Player1 Won! p: {p1_point}"
    elif p2_point > p1_point:
        return f"player2 Won! p: {p2_point}"
    else:
        return "Draw!"
    

player1 = Hero(inte=15, speed=.5, dm=10);
player2 = Hero(inte=13, speed=.4, dm=11);

print(check(player1, player2))

class person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calc_BMI(self):
        return  self.weight / pow(self.height, 2)

def main():
    p_height = float(input("Input you're height in M: "))
    p_weight = float(input("Input you're weight in KG: "))

    user = person(p_height, p_weight)
    BMI = user.calc_BMI()

    print(BMI)

main()
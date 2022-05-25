class alive:
    alive = True

    def check_alive(self):
        print("Alive =", self.alive)


class blood_group(alive):
    bg = "B+"

    def check_bg(self):
        print("Blood Group =", self.bg)


class medical_report(blood_group):
    def __init__(self, name):
        print("Pateint Name =", name)
        self.check_alive()
        self.check_bg()


piyush = medical_report("Piyush")

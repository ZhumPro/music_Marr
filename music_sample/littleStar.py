from scale import Scales


class LittleStar:
    def __init__(self):
        self.name = "Dahai"
        self.music = Scales(240)

    def generator(self):
        # ------------------------ start ------------------------ #
        # 1
        self.music.c5(1)
        self.music.c5(1)
        self.music.g5(1)
        self.music.g5(1)
        # 2
        self.music.a5(1)
        self.music.a5(1)
        self.music.g5(2)
        # 3
        self.music.f5(1)
        self.music.f5(1)
        self.music.e5(1)
        self.music.e5(1)
        # 4
        self.music.d5(1)
        self.music.d5(1)
        self.music.c5(2)
        # 5
        self.music.g5(1)
        self.music.g5(1)
        self.music.f5(1)
        self.music.f5(1)
        # 6
        self.music.e5(1)
        self.music.e5(1)
        self.music.d5(2)
        # 7
        self.music.g5(1)
        self.music.g5(1)
        self.music.f5(1)
        self.music.f5(1)
        # 8
        self.music.e5(1)
        self.music.e5(1)
        self.music.d5(2)
        # 9
        self.music.c5(1)
        self.music.c5(1)
        self.music.g5(1)
        self.music.g5(1)
        # 10
        self.music.a5(1)
        self.music.a5(1)
        self.music.g5(2)
        # 11
        self.music.f5(1)
        self.music.f5(1)
        self.music.e5(1)
        self.music.e5(1)
        # 12
        self.music.d5(1)
        self.music.d5(1)
        self.music.c5(2)
        # ------------------------ end ------------------------ #
        with open(self.name, "wb") as output_file:
            self.music.get_midi().writeFile(output_file)
        return self.name

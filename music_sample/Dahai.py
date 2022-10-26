from scale import Scales


class Dahai:
    def __init__(self):
        self.name = "Dahai"
        self.music = Scales(120)

    def generator(self):
        # ------------------------ start ------------------------ #
        # 0
        self.music.a5s(2.5)
        self.music.f4(0.5)
        self.music.a5s(0.5)
        self.music.d5(0.5)
        self.music.d5s(1)
        self.music.d5(1)
        self.music.a5s(1)
        self.music.c5(1)
        # 01
        self.music.d5(3)
        self.music.a5s(1)
        self.music.c5(4)
        # 02
        self.music.a5s(2.5)
        self.music.f4(0.5)
        self.music.a5s(0.5)
        self.music.d5(0.5)
        self.music.d5s(1)
        self.music.d5(1)
        self.music.c5(1)
        self.music.a5s(1)
        # 03
        self.music.d5(3)
        self.music.a5s(1)
        self.music.c5(4)
        # 04
        self.music.a5s(14)
        # 1
        self.music.f4(1)
        self.music.g4(1)

        with open(self.name, "wb") as output_file:
            self.music.get_midi().writeFile(output_file)
        return self.name



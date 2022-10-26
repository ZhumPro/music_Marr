from scale import Scales


class Demo:
    def __init__(self):
        self.name = "demo"
        self.music = Scales(220)

    def generator(self):
        for i in range(4):
            self.music.c6(8)
            self.music.modify_time(8, 1)
            self.music.c4(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.e5(1)
            self.music.g3(1)
            self.music.d4(1)
            self.music.g4(1)
            self.music.b4(1)
            # 42
            self.music.modify_time(8, 0)
            self.music.modify_time(8, 1)
            self.music.a3(1)
            self.music.e4(1)
            self.music.a4(1)
            self.music.c5(1)
            self.music.e3(1)
            self.music.e4(1)
            self.music.g4(1)
            self.music.b4(1)
            # 43
            self.music.modify_time(8, 0)
            self.music.modify_time(8, 1)
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.a4(1)
            self.music.c4(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.e5(1)
            # 44
            self.music.modify_time(8, 0)
            self.music.modify_time(8, 1)
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.a4(1)
            self.music.g3(1)
            self.music.d4(1)
            self.music.g4(1)
            self.music.b4(1)

        with open(self.name, "wb") as output_file:
            self.music.get_midi().writeFile(output_file)
        return self.name

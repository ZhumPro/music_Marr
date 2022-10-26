from scale import Scales


class TheSpectre:

    def __init__(self):
        self.name = "thespectre"
        self.music = Scales(270)

    def generator(self):
        pertime = 2
        onebartime = pertime * 4            # 小节（全音符）
        halfnote = pertime * 2              # 二分音符
        quarternote = pertime               # 四分音符
        quaver = pertime / 2                # 八分音符
        sixteenthnote = pertime / 4         # 十六分音符
        # 1
        self.music.g5s(quarternote)
        self.music.c5s(quarternote)
        self.music.e7(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.e6(halfnote)
        self.music.modify_time(onebartime, 1)
        for i in range(4):
            self.music.d4s(quarternote)
            self.music.modify_time(quarternote,1)
            self.music.a4(quarternote)
            self.music.modify_time(quarternote,1)
            self.music.f4s(quarternote)
            self.music.modify_time(quarternote,1)
            self.music.d3s(quarternote)
        # 2
        self.music.a5(quarternote)
        self.music.c5s(quarternote)
        self.music.a6(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.a5(halfnote)
        self.music.modify_time(onebartime, 1)
        for i in range(4):
            self.music.b4(quarternote)
            self.music.modify_time(quarternote, 1)
            self.music.f4s(quarternote)
            self.music.modify_time(quarternote, 1)
            self.music.d3s(quarternote)
            self.music.modify_time(quarternote, 1)
            self.music.b3(quarternote)

        with open(self.name, "wb") as output_file:
            self.music.get_midi().writeFile(output_file)
        return self.name




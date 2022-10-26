from scale import Scales


class CannonC:
    primarybpm = 72

    # pertime = 2
    # onebartime = pertime * 4            # 小节（全音符）
    # halfnote = pertime * 2              # 二分音符
    # quarternote = pertime               # 四分音符
    # quaver = pertime / 2                # 八分音符
    # sixteenthnote = pertime / 4         # 十六分音符

    def __init__(self, primarybpm=72, metre=4):
        """
        :param primarybpm:主节奏
        :param metre: 节拍数
        """
        self.metre = metre
        self.name = "CannonC"
        self.primarybpm = primarybpm
        self.music = Scales(120)

    def generator(self):
        # ---------------- start ---------------------#

        pertime = float(72 / 82) * 2
        onebartime = pertime * self.metre
        halfnote = pertime * 2
        quarternote = pertime  # 四分音符
        quaver = pertime / 2  # 八分音符
        sixteenthnote = pertime / 4
        # 1
        self.music.e5(halfnote)
        self.music.d5(halfnote)
        self.music.modify_time(onebartime, 1)
        self.music.c4(halfnote)
        self.music.g3(halfnote)
        # 2
        self.music.c5(halfnote)
        self.music.b4(halfnote)
        self.music.modify_time(onebartime, 1)
        self.music.a3(halfnote)
        self.music.e3(halfnote)
        # 3
        self.music.a4(halfnote)
        self.music.g4(halfnote)
        self.music.modify_time(onebartime, 1)
        self.music.f3(halfnote)
        self.music.a3(halfnote)
        # 4
        self.music.a4(halfnote)
        self.music.b4(halfnote)
        self.music.modify_time(onebartime, 1)
        self.music.f3(halfnote)
        self.music.g3(halfnote)
        # 5
        self.music.e6(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.g5(halfnote)
        self.music.d6(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.g5(halfnote)
        self.music.modify_time(onebartime, 1)
        self.music.c4(halfnote)
        self.music.g3(halfnote)
        # 6
        self.music.c6(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.e5(halfnote)
        self.music.b5(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.e5(halfnote)
        self.music.modify_time(onebartime, 1)
        self.music.a3(halfnote)
        self.music.e3(halfnote)
        # 7
        self.music.a5(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.c5(halfnote)
        self.music.g5(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.c5(halfnote)
        self.music.modify_time(onebartime, 1)
        self.music.f3(halfnote)
        self.music.c4(halfnote)
        # 8
        self.music.a5(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.c5(halfnote)
        self.music.b5(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.d5(halfnote)
        self.music.modify_time(onebartime, 1)
        self.music.f3(halfnote)
        self.music.g3(halfnote)

        # # change BPM
        # self.primarybpm = 72
        pertime = 2
        onebartime = pertime * self.metre
        halfnote = pertime * 2
        quarternote = pertime  # 四分音符
        quaver = pertime / 2  # 八分音符
        sixteenthnote = pertime / 4

        # 9
        self.music.e6(halfnote)
        self.music.modify_time(halfnote, 1)
        self.music.g5(halfnote)
        self.music.d6(quarternote)
        self.music.modify_time(quarternote, 1)
        self.music.g5(quarternote)
        self.music.f5(quarternote)
        self.music.modify_time(onebartime, 1)
        self.music.c4(quaver)
        self.music.g4(quaver)
        self.music.c5(quaver)
        self.music.b3(quaver)
        self.music.d4(quaver)
        self.music.g4(quaver)
        self.music.b4(quaver)
        # 10
        self.music.c6(halfnote)
        self.music.b5(quarternote)
        self.music.g5(quarternote)
        self.music.modify_time(onebartime, 1)
        self.music.a3(quaver)
        self.music.e4(quaver)
        self.music.a4(quaver)
        self.music.c5(quaver)
        self.music.e3(quaver)
        self.music.e4(quaver)
        self.music.g4(quaver)
        self.music.b4(quaver)
        # 11
        self.music.a5(halfnote)
        self.music.g5(quarternote)
        self.music.e5(quarternote)
        self.music.modify_time(onebartime,1)
        self.music.f3(quaver)
        self.music.c4(quaver)
        self.music.f4(quaver)
        self.music.a4(quaver)
        self.music.c4(quaver)
        self.music.e4(quaver)
        self.music.g4(quaver)
        self.music.c5(quaver)
        # 12
        self.music.a5(halfnote)
        self.music.modify_time(halfnote,1)
        self.music.f5(halfnote)
        self.music.g5(quarternote)
        self.music.modify_time(quarternote,1)
        self.music.d5(quarternote)
        self.music.modify_time(onebartime,1)
        self.music.f3(quaver)
        self.music.c4(quaver)
        self.music.f4(quaver)
        self.music.a4(quaver)
        self.music.g3(quaver)
        self.music.d4(quaver)
        self.music.b4(quaver)
        # 13
        self.music.c6(quaver)
        self.music.b5(quaver)
        self.music.c6(quaver)
        self.music.e5(quaver)
        self.music.g5(quarternote)
        self.music.b5(quarternote)
        self.music.modify_time(onebartime,1)
        self.music.c4(quaver)
        self.music.e4(quaver)
        self.music.g4(quaver)
        self.music.c5(quaver)
        self.music.g3(quaver)
        self.music.d4(quaver)
        self.music.g4(quaver)
        self.music.b4(quaver)
        # 14

        with open(self.name, "wb") as output_file:
            self.music.get_midi().writeFile(output_file)
        return self.name

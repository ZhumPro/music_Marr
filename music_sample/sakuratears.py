from scale import Scales


class SakuraTears:

    def __init__(self):
        self.name = 'SakuraTears'
        self.music = Scales(220)

    def generator(self):
        # ------------------------ start ------------------------ #
        # ---------------- first bar ---------------- #
        self.music.modify_time(4)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------------------- repeat part -------------------- #
        for i in range(0, 2):
            # ---------------- second bar ---------------- #
            # -------- major -------- #
            self.music.a5(2)
            self.music.a5(1)
            self.music.g5(2)
            self.music.g5(1)
            self.music.d5(1)
            self.music.e5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.c4(1)
            self.music.e3(1)
            self.music.d4(1)
            self.music.e4(1)
            self.music.d4(1)
            # ---------------- third bar ---------------- #
            # -------- major -------- #
            self.music.modify_time(3)
            self.music.e5(1)
            self.music.c6(1)
            self.music.b5(1)
            self.music.a5(1)
            self.music.g5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.c4(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            # ---------------- fourth bar ---------------- #
            # -------- major -------- #
            self.music.a5(2)
            self.music.a5(1)
            self.music.e6(1)
            self.music.b5(1)
            self.music.c6(1)
            self.music.b5(1)
            self.music.b5(2)
            # -------- modify time -------- #
            self.music.modify_time(9, 1)
            # -------- minor -------- #
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.c4(1)
            self.music.e3(1)
            self.music.d4(1)
            self.music.e4(1)
            self.music.d4(1)
            # ---------------- fifth bar ---------------- #
            # -------- modify time -------- #
            self.music.modify_time(1)
            # -------- major -------- #
            self.music.c6(2)
            self.music.c6(0.5)
            self.music.c6(0.5)
            self.music.c6(1)
            self.music.b5(1)
            self.music.a5(1)
            self.music.g5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.a3(1)
            self.music.e4(1)
            self.music.c5(1)
            self.music.e4(1)
            self.music.c5(1)
            self.music.e4(1)
            self.music.c5(2)
            # ----------------sixth bar ---------------- #
            # -------- major -------- #
            self.music.a5(2)
            self.music.a5(1)
            self.music.g5(2)
            self.music.g5(1)
            self.music.d5(1)
            self.music.e5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.c4(1)
            self.music.e3(1)
            self.music.d4(1)
            self.music.e4(1)
            self.music.d4(1)
            # ---------------- seventh bar ---------------- #
            # -------- major -------- #
            self.music.modify_time(3)
            self.music.e5(1)
            self.music.c6(1)
            self.music.b5(1)
            self.music.a5(1)
            self.music.g5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.c4(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            # ---- differential ---- #
            if i == 0:
                # ---------------- eighth bar ---------------- #
                # -------- major -------- #
                self.music.a5(2)
                self.music.a5(1)
                self.music.e6(1)
                self.music.b5(1)
                self.music.c6(1)
                self.music.b5(1)
                self.music.b5(2)
                # -------- modify time -------- #
                self.music.modify_time(9, 1)
                # -------- minor -------- #
                self.music.f3(1)
                self.music.c4(1)
                self.music.f4(1)
                self.music.c4(1)
                self.music.e3(1)
                self.music.d4(1)
                self.music.e4(1)
                self.music.d4(1)
                # ---------------- ninth bar ---------------- #
                # -------- modify time -------- #
                self.music.modify_time(1)
                # -------- major -------- #
                self.music.c6(3)
                self.music.c6(1)
                self.music.b5(1)
                self.music.a5(1)
                self.music.g5(1)
                # -------- modify time -------- #
                self.music.modify_time(8, 1)
                # -------- minor -------- #
                self.music.a3(1)
                self.music.e4(1)
                self.music.c5(2)
                self.music.modify_time(4)
            # ---- differential ---- #
            else:
                # ---------------- tenth bar ---------------- #
                # -------- major -------- #
                self.music.a5(2)
                self.music.a5(1)
                self.music.e6(1)
                self.music.b5(1)
                self.music.c6(1)
                self.music.b5(1)
                self.music.b5(2)
                # -------- modify time -------- #
                self.music.modify_time(9, 1)
                # -------- minor -------- #
                self.music.f3(1)
                self.music.c4(1)
                self.music.f4(1)
                self.music.c4(1)
                self.music.e3(1)
                self.music.d4(1)
                self.music.e4(1)
                self.music.d4(1)
        # ---------------- eleventh bar ---------------- #
        # -------- modify time -------- #
        self.music.modify_time(1)
        # -------- major -------- #
        self.music.c6(2)
        self.music.c7(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(2)
        self.music.modify_time(3)
        self.music.g3(1)
        # -------- modify time -------- #
        self.music.modify_time(4, 1)
        # -------- other -------- #
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # -------------------- repeat part -------------------- #
        for i in range(0, 2):
            # ---------------- twelfth bar ---------------- #
            # -------- major -------- #
            self.music.a5(2)
            self.music.a5(1)
            self.music.g5(2)
            self.music.g5(1)
            self.music.d5(1)
            self.music.e5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.c4(1)
            self.music.e3(1)
            self.music.d4(1)
            self.music.e4(1)
            self.music.d4(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- other -------- #
            self.music.a6(2)
            self.music.a6(1)
            self.music.g6(2)
            self.music.g6(1)
            self.music.d6(1)
            self.music.e6(1)
            # ---------------- thirteenth bar ---------------- #
            # -------- major -------- #
            self.music.modify_time(3)
            self.music.e5(1)
            self.music.c6(1)
            self.music.b5(1)
            self.music.a5(1)
            self.music.g5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.c4(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            # -------- modify time -------- #
            self.music.modify_time(5, 1)
            # -------- other -------- #
            self.music.e6(1)
            self.music.c7(1)
            self.music.b6(1)
            self.music.a6(1)
            self.music.g6(1)
            # ---------------- fourteenth bar ---------------- #
            # -------- major -------- #
            self.music.a5(2)
            self.music.a5(1)
            self.music.e6(1)
            self.music.b5(1)
            self.music.c6(1)
            self.music.b5(1)
            self.music.b5(2)
            # -------- modify time -------- #
            self.music.modify_time(9, 1)
            # -------- minor -------- #
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.c4(1)
            self.music.e3(1)
            self.music.d4(1)
            self.music.e4(1)
            self.music.d4(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- other -------- #
            self.music.a6(2)
            self.music.a6(1)
            self.music.e7(1)
            self.music.b6(1)
            self.music.c7(1)
            self.music.b6(1)
            self.music.b6(2)
            # ---------------- fifteenth bar ---------------- #
            # -------- major -------- #
            self.music.c6(2)
            self.music.c6(0.5)
            self.music.c6(0.5)
            self.music.c6(1)
            self.music.b5(1)
            self.music.a5(1)
            self.music.g5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.a3(1)
            self.music.e4(1)
            self.music.c5(1)
            self.music.e4(1)
            self.music.c5(1)
            self.music.e4(1)
            self.music.c5(2)
            # -------- modify time -------- #
            self.music.modify_time(7, 1)
            # -------- other -------- #
            self.music.c7(2)
            self.music.c7(0.5)
            self.music.c7(0.5)
            self.music.c7(1)
            self.music.b6(1)
            self.music.a6(1)
            self.music.g6(1)
            # ---------------- sixteenth bar ---------------- #
            # -------- major -------- #
            self.music.a5(2)
            self.music.a5(1)
            self.music.g5(2)
            self.music.g5(1)
            self.music.d5(1)
            self.music.e5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.c4(1)
            self.music.e3(1)
            self.music.d4(1)
            self.music.e4(1)
            self.music.d4(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- other -------- #
            self.music.a6(2)
            self.music.a6(1)
            self.music.g6(2)
            self.music.g6(1)
            self.music.d6(1)
            self.music.e6(1)
            # ---------------- seventeenth bar ---------------- #
            # -------- major -------- #
            self.music.modify_time(3)
            self.music.e5(1)
            self.music.c6(1)
            self.music.b5(1)
            self.music.a5(1)
            self.music.g5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.c4(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            self.music.c5(1)
            self.music.g4(1)
            # -------- modify time -------- #
            self.music.modify_time(5, 1)
            # -------- other -------- #
            self.music.e6(1)
            self.music.c7(1)
            self.music.b6(1)
            self.music.a6(1)
            self.music.g6(1)
            # ---------------- eighteenth bar ---------------- #
            # -------- major -------- #
            self.music.a5(2)
            self.music.a5(1)
            self.music.e6(1)
            self.music.b5(1)
            self.music.d6(1)
            self.music.b5(1)
            self.music.b5(2)
            # -------- modify time -------- #
            self.music.modify_time(9, 1)
            # -------- minor -------- #
            self.music.f3(1)
            self.music.c4(1)
            self.music.f4(1)
            self.music.c4(1)
            self.music.e3(1)
            self.music.d4(1)
            self.music.e4(1)
            self.music.d4(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- other -------- #
            self.music.a6(2)
            self.music.a6(1)
            self.music.e7(1)
            self.music.b6(1)
            self.music.d7(1)
            self.music.b6(1)
            self.music.b6(2)
            # ---------------- nineteenth bar ---------------- #
            # -------- major -------- #
            self.music.c6(2)
            self.music.c7(1)
            self.music.c6(1)
            self.music.b5(1)
            self.music.a5(1)
            self.music.g5(1)
            # -------- modify time -------- #
            self.music.modify_time(8, 1)
            # -------- minor -------- #
            self.music.a3(1)
            self.music.e4(1)
            self.music.c5(2)
            self.music.modify_time(4)
            # -------- modify time -------- #
            self.music.modify_time(7, 1)
            # -------- other -------- #
            self.music.c7(2)
            self.music.c7(1)
            self.music.c7(1)
            self.music.b6(1)
            self.music.a6(1)
            self.music.g6(1)
        # ---------------- twentieth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- twenty-first bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- twenty-second bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- twenty-third bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c6(0.5)
        self.music.c6(0.5)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.c7(2)
        self.music.c7(0.5)
        self.music.c7(0.5)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- twenty-fourth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- twenty-fifth bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- twenty-sixth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.d6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.d7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- twenty-seventh bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c7(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(2)
        self.music.modify_time(4)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.c7(2)
        self.music.c7(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- twenty-eighth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- twenty-ninth bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- thirtieth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- thirty-first bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c6(0.5)
        self.music.c6(0.5)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.c7(2)
        self.music.c7(0.5)
        self.music.c7(0.5)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- thirty-second bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- thirty-third bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- thirty-fourth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.d6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.d7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- thirty-fifth bar ---------------- #
        # -------- major -------- #
        self.music.c6(1)
        self.music.c6(2)
        self.music.modify_time(2)
        self.music.c6(1)
        self.music.d6(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(2)
        self.music.modify_time(4)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.e6(1)
        # -------- modify time -------- #
        self.music.modify_time(1, 1)
        # -------- other -------- #
        self.music.a6(1)
        self.music.modify_time(6)
        # ---------------- thirty-sixth bar ---------------- #
        # -------- major -------- #
        self.music.e6(2)
        self.music.e6(2)
        self.music.d6(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # ---------------- thirty-seventh bar ---------------- #
        # -------- modify time -------- #
        self.music.modify_time(1)
        # --------major -------- #
        self.music.c6(3)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.g4(1)
        # ---------------- thirty-eighth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.d6(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # ---------------- thirty-ninth bar ---------------- #
        # -------- major -------- #
        self.music.a5(1)
        self.music.e6(3)
        self.music.f6(1)
        self.music.e6(1)
        self.music.d6(1)
        self.music.c6(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # ---------------- forty bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.g6(1)
        self.music.d6(2)
        self.music.c6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # ---------------- forty-first bar ---------------- #
        # -------- modify time -------- #
        self.music.modify_time(1)
        # -------- major -------- #
        self.music.c6(2)
        self.music.c6(0.5)
        self.music.c6(0.5)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.g4(1)
        # ---------------- forty-second bar ---------------- #
        # -------- major -------- #
        self.music.f5(4)
        self.music.d5(3)
        self.music.e5(4)
        # -------- modify time -------- #
        self.music.modify_time(11, 1)
        # -------- minor -------- #
        self.music.f3(4)
        self.music.g3(3)
        self.music.c4(5)
        # -------- modify time -------- #
        self.music.modify_time(12, 1)
        # -------- other -------- #
        self.music.a5(4)
        self.music.g5(3)
        self.music.g5(4)
        # -------- modify time -------- #
        self.music.modify_time(11, 1)
        # -------- other -------- #
        self.music.c6(4)
        self.music.b5(3)
        self.music.c6(4)
        # -------- modify time -------- #
        self.music.modify_time(11, 1)
        # -------- minor -------- #
        self.music.f4(4)
        self.music.g4(3)
        self.music.c5(5)
        # ---------------- forty-third bar ---------------- #
        # -------- modify time -------- #
        self.music.modify_time(1, 1)
        # -------- major -------- #
        self.music.c7(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(4, 1)
        # -------- minor -------- #
        self.music.modify_time(3)
        self.music.g3(1)
        # -------- modify time -------- #
        self.music.modify_time(4, 1)
        # -------- other -------- #
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- forty-fourth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- forty-fifth bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- forty-sixth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- forty-seventh bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c6(0.5)
        self.music.c6(0.5)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.c7(2)
        self.music.c7(0.5)
        self.music.c7(0.5)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- forty-eighth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- forty-ninth bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- fiftieth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.d6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.d7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- fifty-first bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c7(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(2)
        self.music.modify_time(4)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.c7(2)
        self.music.c7(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- fifty-second bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- fifty-third bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- fifty-fourth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- fifty-fifth bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c6(0.5)
        self.music.c6(0.5)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.c7(2)
        self.music.c7(0.5)
        self.music.c7(0.5)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- fifty-sixth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- fifty-seventh bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- fifty-eighth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.d6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.d7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- fifty-ninth bar ---------------- #
        # -------- major -------- #
        self.music.c6(1)
        self.music.c6(2)
        self.music.e5(2)
        self.music.e5(2)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(2)
        self.music.modify_time(4)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.modify_time(2)
        self.music.a5(2)
        self.music.a5(2)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.a6(1)
        self.music.modify_time(2)
        self.music.c6(2)
        self.music.c6(2)
        # ---------------- sixtieth bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.d6(1)
        self.music.d6s(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        # -------- modify time -------- #
        self.music.modify_time(2, 1)
        # -------- minor -------- #
        self.music.modify_time(1)
        self.music.a3(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.d7(1)
        self.music.d7s(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        # ---------------- sixty-first bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- sixty-second bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- sixty-third bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- sixty-fourth bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c6(0.5)
        self.music.c6(0.5)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.c7(2)
        self.music.c7(0.5)
        self.music.c7(0.5)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- sixty-fifth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- sixty-sixth bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- sixty-seventh bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.d6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.d7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- sixty-eighth bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c7(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(3, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.modify_time(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- sixty-ninth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- seventy bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- seventy-first bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- seventy-second bar ---------------- #
        # -------- major -------- #
        self.music.c6(2)
        self.music.c6(0.5)
        self.music.c6(0.5)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(1)
        self.music.e4(1)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.c7(2)
        self.music.c7(0.5)
        self.music.c7(0.5)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- seventy-third bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.g5(2)
        self.music.g5(1)
        self.music.d5(1)
        self.music.e5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.g6(2)
        self.music.g6(1)
        self.music.d6(1)
        self.music.e6(1)
        # ---------------- seventy-fourth bar ---------------- #
        # -------- major -------- #
        self.music.modify_time(3)
        self.music.e5(1)
        self.music.c6(1)
        self.music.b5(1)
        self.music.a5(1)
        self.music.g5(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.c4(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        self.music.c5(1)
        self.music.g4(1)
        # -------- modify time -------- #
        self.music.modify_time(5, 1)
        # -------- other -------- #
        self.music.e6(1)
        self.music.c7(1)
        self.music.b6(1)
        self.music.a6(1)
        self.music.g6(1)
        # ---------------- seventy-fifth bar ---------------- #
        # -------- major -------- #
        self.music.a5(2)
        self.music.a5(1)
        self.music.e6(1)
        self.music.b5(1)
        self.music.d6(1)
        self.music.b5(1)
        self.music.b5(2)
        # -------- modify time -------- #
        self.music.modify_time(9, 1)
        # -------- minor -------- #
        self.music.f3(1)
        self.music.c4(1)
        self.music.f4(1)
        self.music.c4(1)
        self.music.e3(1)
        self.music.d4(1)
        self.music.e4(1)
        self.music.d4(1)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- other -------- #
        self.music.a6(2)
        self.music.a6(1)
        self.music.e7(1)
        self.music.b6(1)
        self.music.d7(1)
        self.music.b6(1)
        self.music.b6(2)
        # ---------------- seventy-sixth bar ---------------- #
        # -------- major -------- #
        self.music.c6(3)
        self.music.a5(2)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(8, 1)
        # -------- minor -------- #
        self.music.a3(1)
        self.music.e4(1)
        self.music.c5(2)
        # -------- modify time -------- #
        self.music.modify_time(3, 1)
        # -------- other -------- #
        self.music.e6(3)
        self.music.c6(2)
        self.music.a5(2)
        # -------- modify time -------- #
        self.music.modify_time(7, 1)
        # -------- other -------- #
        self.music.a6(3)
        self.music.modify_time(4)
        # ---------------- seventy-seventh bar ---------------- #
        # -------- minor -------- #
        self.music.a3(4)
        # -------- modify time -------- #
        self.music.modify_time(4, 1)
        # -------- other -------- #
        self.music.a2(4)
        # ------------------------ end ------------------------ #
        with open(self.name, "wb") as output_file:
            self.music.get_midi().writeFile(output_file)
        return self.name

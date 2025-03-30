from manim import *

class JednaScenaZAntyoksydantemBezNakladania(Scene):
    def construct(self):
        # Tytuł
        title = Text(
            "",
            font_size=30
        ).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # --- 1) Wolny rodnik (R1) po LEWEJ, przesunięty bardziej w lewo ---
        r1_nucleus = Circle(radius=0.4, color=RED, fill_opacity=0.2).shift(LEFT*5)
        r1_orbit_1 = Circle(radius=1.0, color=GRAY).shift(LEFT*5)
        r1_orbit_2 = Circle(radius=1.4, color=GRAY).shift(LEFT*5)

        r1_pair_1 = VGroup(
            Dot(color=BLUE).move_to(r1_orbit_1.point_at_angle(60*DEGREES)),
            Dot(color=BLUE).move_to(r1_orbit_1.point_at_angle(240*DEGREES)),
        )
        r1_unpaired = Dot(color=YELLOW).move_to(r1_orbit_2.point_at_angle(0*DEGREES))

        r1_group = VGroup(r1_nucleus, r1_orbit_1, r1_orbit_2, r1_pair_1, r1_unpaired)

        self.play(Create(r1_nucleus), Create(r1_orbit_1), Create(r1_orbit_2))
        self.play(FadeIn(r1_pair_1), FadeIn(r1_unpaired))
        self.wait(1)

        # Błysk
        for _ in range(2):
            self.play(Flash(r1_unpaired, color=YELLOW, flash_radius=0.4))
            self.wait(0.5)

        # --- 2) Stabilna cząsteczka (S1) po PRAWEJ, też przesunięta bardziej ---
        s1_nucleus = Circle(radius=0.4, color=GREEN, fill_opacity=0.2).shift(RIGHT*4)
        s1_orbit_1 = Circle(radius=1.0, color=GRAY).shift(RIGHT*4)
        s1_orbit_2 = Circle(radius=1.4, color=GRAY).shift(RIGHT*4)

        s1_pair_1 = VGroup(
            Dot(color=BLUE).move_to(s1_orbit_1.point_at_angle(45*DEGREES)),
            Dot(color=BLUE).move_to(s1_orbit_1.point_at_angle(225*DEGREES)),
        )
        s1_pair_2 = VGroup(
            Dot(color=BLUE).move_to(s1_orbit_2.point_at_angle(90*DEGREES)),
            Dot(color=BLUE).move_to(s1_orbit_2.point_at_angle(270*DEGREES)),
        )

        s1_group = VGroup(s1_nucleus, s1_orbit_1, s1_orbit_2, s1_pair_1, s1_pair_2)

        self.play(Create(s1_nucleus), Create(s1_orbit_1), Create(s1_orbit_2))
        self.play(FadeIn(s1_pair_1), FadeIn(s1_pair_2))
        self.wait(1)

        # --- 3) R1 zbliża się do S1 (ale pokonuje większy dystans) ---
        # Zamiast shift(RIGHT*2) daj np. shift(RIGHT*3) lub R1 i S1 jeszcze dalej, zależnie od potrzeb
        self.play(r1_group.animate.shift(RIGHT*3), run_time=2)
        self.wait(1)

        # Kradzież elektronu
        stolen_electron = s1_pair_1[0]
        self.play(Flash(stolen_electron, color=YELLOW, flash_radius=0.5))
        self.wait(0.5)

        self.play(
            stolen_electron.animate.move_to(r1_unpaired.get_center() + RIGHT*0.3),
            run_time=2
        )
        self.wait(1)

        self.play(r1_nucleus.animate.set_color(BLUE))
        self.play(FadeOut(r1_unpaired), FadeOut(stolen_electron))
        r1_new_pair = VGroup(
            Dot(color=BLUE).move_to(r1_orbit_2.point_at_angle(10*DEGREES)),
            Dot(color=BLUE).move_to(r1_orbit_2.point_at_angle(-10*DEGREES))
        )
        self.play(FadeIn(r1_new_pair))
        self.wait(1)

        # S1 -> R2
        r2_unpaired = s1_pair_1[1]
        self.play(r2_unpaired.animate.set_color(YELLOW))
        self.play(s1_nucleus.animate.set_color(RED))
        self.wait(1)

        for _ in range(2):
            self.play(Flash(r2_unpaired, color=YELLOW, flash_radius=0.4))
            self.wait(0.5)

        # --- 4) Antyoksydant (A) – przesunięty jeszcze bardziej w górę/prawo ---
        text_phase = Text(
            "",
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(text_phase))
        self.wait(2)

        ant_core = Circle(radius=0.4, color=GREEN, fill_opacity=0.2).shift(UP*2 + RIGHT*6)
        ant_orbit = Circle(radius=1.0, color=GRAY).shift(UP*2 + RIGHT*6)

        a_pair_1 = VGroup(
            Dot(color=BLUE).move_to(ant_orbit.point_at_angle(45*DEGREES)),
            Dot(color=BLUE).move_to(ant_orbit.point_at_angle(225*DEGREES)),
        )
        a_extra = Dot(color=PURPLE).move_to(ant_orbit.point_at_angle(315*DEGREES))

        ant_group = VGroup(ant_core, ant_orbit, a_pair_1, a_extra)

        self.play(Create(ant_core), Create(ant_orbit))
        self.play(FadeIn(a_pair_1), FadeIn(a_extra))
        self.wait(1)

        # Nie przesuwamy całego antyoksydanta, tylko sam elektron lecący do R2
        self.play(Flash(a_extra, color=PURPLE, flash_radius=0.5))
        self.wait(0.5)

        self.play(
            a_extra.animate.move_to(r2_unpaired.get_center() + LEFT*0.3),
            run_time=2
        )
        self.wait(1)

        self.play(s1_nucleus.animate.set_color(BLUE))
        self.play(FadeOut(r2_unpaired), FadeOut(a_extra))
        r2_new_pair = VGroup(
            Dot(color=BLUE).move_to(s1_orbit_1.point_at_angle(45*DEGREES + 10*DEGREES)),
            Dot(color=BLUE).move_to(s1_orbit_1.point_at_angle(45*DEGREES - 10*DEGREES))
        )
        self.play(FadeIn(r2_new_pair))
        self.wait(1)

        self.play(Indicate(ant_core, color=GREEN))
        self.wait(1)

        # Koniec
        self.play(FadeOut(text_phase))
        end_text = Text("",
                        font_size=30).to_edge(DOWN)
        self.play(Write(end_text))
        self.wait(3)

        self.play(
            FadeOut(end_text),
            FadeOut(r1_group),
            FadeOut(r1_new_pair),
            FadeOut(s1_group),
            FadeOut(r2_new_pair),
            FadeOut(ant_group),
            FadeOut(title)
        )
        self.wait(1)




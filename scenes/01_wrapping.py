from manim import *


class TokenToLocker(Scene):
    def construct(self):
        # Create objects
        token = Circle(radius=0.5, color=BLUE).shift(LEFT * 3)
        locker = Square(side_length=2, color=GREEN).shift(RIGHT * 2)
        ve_token = Circle(radius=0.5, color=RED).shift(RIGHT * 2)

        # Add labels
        token_label = Text("Token").next_to(token, DOWN)
        locker_label = Text("Escrow").next_to(locker, DOWN)

        # Add objects to the scene
        self.add(token, locker, token_label, locker_label)

        self.wait(1)

        # Animate the movement
        animation = token.animate.shift(RIGHT * 5)
        self.play(animation)

        self.remove(token_label)

        # Add veToken to the scene after the movement
        self.add(ve_token)
        self.play(FadeIn(ve_token))
        self.play(ve_token.animate.shift(LEFT * 5))

        # Add ve_token_label below the final position of ve_token
        ve_token_label = Text(
            "veToken",
        ).next_to(ve_token, DOWN)
        ve_token_label_description = (
            Text("(Voting Escrow)").next_to(ve_token_label, DOWN).scale(0.75)
        )
        self.play(FadeIn(ve_token_label), FadeIn(ve_token_label_description))

        # Pause the scene for 3 seconds
        self.wait(3)

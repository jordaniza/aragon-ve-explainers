from manim import *
import numpy as np


class LogarithmicCurve(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 48, 6],
            y_range=[0, 110, 10],
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 49, 6),
                "label_direction": DOWN,
                "decimal_number_config": {"num_decimal_places": 0},
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 110, 10),
                "label_direction": LEFT,
                "decimal_number_config": {"num_decimal_places": 0, "unit": r"\%"},
                "include_tip": False,
            },
        )

        # Add labels
        x_label = axes.get_x_axis_label("Time (months)")
        y_label = Text("Voting Power (%)").to_edge(UP).shift(LEFT * 5).scale(0.6)

        # Define the logarithmic function
        def log_func(x):
            return 100 * np.log(x + 1) / np.log(48 + 1)  # Normalized to 100%

        # Create the curve
        curve = axes.plot(log_func, x_range=[0, 48], color=YELLOW)

        # Create a dot at the beginning of the curve
        dot = Dot(color=RED).move_to(axes.i2gp(0, curve))

        # Create the dot animation
        dot_animation = MoveAlongPath(dot, curve, run_time=5, rate_func=there_and_back)

        # Add elements to the scene
        self.add(axes, x_label, y_label, curve, dot)
        self.play(dot_animation)
        self.wait(2)

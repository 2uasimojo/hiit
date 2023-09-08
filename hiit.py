#!/bin/env python

import random

ex_per_cycle = 11

exercises = {
    "Overhead triceps": set(("triceps",)),
    "DB Curls": set(("biceps",)),
    "Arnold Press": set(
        (
            "deltoids",
            "triceps",
        )
    ),
    "Wall Ball": set(
        (
            "triceps",
            "pecs",
            "cardio",
            "lumbar",
        )
    ),
    "Overhead Ball Slams": set(
        (
            "lats",
            "cardio",
            "quads",
        )
    ),
    "Upright row": set(
        (
            "biceps",
            "deltoids",
        )
    ),
    "Dumbbell bent over fly": set(
        (
            "deltoids",
            "rhomboids",
        )
    ),
    "Bent over row": set(
        (
            "lats",
            "biceps",
        )
    ),
    "Renegade Row": set(
        (
            "biceps",
            "lats",
            "triceps",
            "pecs",
        )
    ),
    "Lateral Ball Slam": set(
        (
            "triceps",
            "pecs",
            "core",
            "cardio",
            "lumbar",
            "quads",
        )
    ),
    "Cross body hammer curl": set(("biceps",)),
    "Zottman curl": set(("biceps",)),
    "Scaption": set(("deltoids",)),
    "Handstand": set(
        (
            "triceps",
            "deltoids",
            "trapezius",
        )
    ),
    "Squats": set(
        (
            "quads",
            "glutes",
        )
    ),
    "180 squats": set(
        (
            "quads",
            "glutes",
        )
    ),
    "DB reverse Lunge": set(
        (
            "quads",
            "adductors",
        )
    ),
    "Lunges": set(
        (
            "quads",
            "adductors",
        )
    ),
    "Walking lunges": set(
        (
            "quads",
            "adductors",
        )
    ),
    "Frog jumps": set(
        (
            "quads",
            "cardio",
            "glutes",
        )
    ),
    "Rover’s Revenge": set(("abductors",)),
    "Wall Sit": set(("quads",)),
    "Deadlifts bent": set(("lumbar",)),
    "Deadlifts straight": set(
        (
            "hamstrings",
            "lumbar",
        )
    ),
    "Sissy squats": set(("quads",)),
    "Heel Flicks": set(
        (
            "cardio",
            "hamstrings",
        )
    ),
    "High Knees": set(
        (
            "hip flexors",
            "cardio",
            "calves",
        )
    ),
    "Jumping Jacks": set(
        (
            "cardio",
            "calves",
        )
    ),
    "Jumprope": set(
        (
            "cardio",
            "calves",
        )
    ),
    "Russian Twist": set(("core",)),
    "Bird Dog": set(
        (
            "deltoids",
            "glutes",
        )
    ),
    "Battle Rope": set(("cardio",)),
    "Bag Kicks": set(
        (
            "cardio",
            "core",
            "hip flexors",
        )
    ),
    "Bear Crawl": set(
        (
            "cardio",
            "triceps",
            "deltoids",
        )
    ),
    "Glute Bridge": set(("glutes",)),
    "Plank": set(("core",)),
    "Comando Push-ups": set(
        (
            "core",
            "triceps",
            "deltoids",
            "pecs",
        )
    ),
    "Superman": set(
        (
            "rhomboids",
            "glutes",
        )
    ),
    "Single Leg Raise": set(("hamstrings",)),
    "Mountain Climbers": set(
        (
            "cardio",
            "hip flexors",
            "deltoids",
            "triceps",
        )
    ),
    "Around the World": set(
        (
            "triceps",
            "deltoids",
        )
    ),
    "Kettlebell Swing": set(
        (
            "cardio",
            "lumbar",
            "deltoids",
        )
    ),
    "Burpees": set(
        (
            "cardio",
            "quads",
            "hip flexors",
            "triceps",
            "pecs",
        )
    ),
    "Ball toss/lunge": set(
        (
            "pecs",
            "cardio",
            "quads",
            "glutes",
        )
    ),
}

workout = []
seen_ex = set()
last_groups = set()
for _ in range(ex_per_cycle):
    # TODO: Emergency brake
    remaining = [
        k
        for k, v in exercises.items()
        if k not in seen_ex and not v.intersection(last_groups)
    ]
    if len(remaining) == 0:
        raise RuntimeError("Ran out of exercises!")
    ex = random.choice(remaining)
    last_groups = exercises[ex]
    workout.append(ex)

print("\n".join(workout))

#!/bin/env python

import random

# Exercises per cycle. Adjust as desired.
# TODO: Command line option for this.
ex_per_cycle = 11

# A dictionary, keyed by exercise name, of sets of muscle groups worked by that
# exercise. The sets are used when generating a workout to ensure that no two
# exercises working the same muscle group are back to back.
# Python-ism: dict
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
exercises = {
    "Side lunges": set(
        (
            "quads",
            "glutes",
            "adductors",
        )
    ),
    "Plough rollovers": set(("core",)),
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
            "lumbar",
        )
    ),
    "Bent over row": set(
        (
            "lats",
            "biceps",
            "lumbar",
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
    "Surrender": set(
        (
            "quads",
            "adductors",
        )
    ),
    "Band Resistance Squats": set(
        (
            "quads",
            "abductors",
        )
    ),
    "Side Leg Raise": set(("abductors",)),
    "Step Up High Knees": set(
        (
            "quads",
            "hip flexors",
            "cardio",
            "calves",
        )
    ),
}

# A list to accumulate the sequence of exercises in a workout.
# It is populated with keys from the `exercises` dict above.
workout = []
# Loop variable that tracks which muscle groups were worked by the exercise
# added in the previous iteration. On each iteration, we assign it the set
# from the `exercises` dictionary for the exercise we added to the `workout`.
last_groups = set()
# Main driver.
# Python-isms:
# - range(<number>) produces an iterator from zero to (<number> - 1). In this
#   case we want to run `ex_per_cycle` iterations of the loop because we want
#   to generate a workout with `ex_per_cycle` exercises.
#   https://docs.python.org/3/library/stdtypes.html#typesseq
# - The `_` (underscore) is where we would normally put the loop variable, like
#   `i`. But we don't have a use for that variable -- we just want to run the
#   loop a certain number of times -- so we use `_`, which by convention
#   indicates "unused".
#   https://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers
for _ in range(ex_per_cycle):
    # On each loop iteration, we build a list of exercises from which to choose
    # the next one to add to our workout.
    # Python-ism: This way of generating a list is called "list comprehension".
    # https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    candidates = [
        # Each element of the list will be a `k`...
        k
        # ...where we get `k` (and also `v`, used below) by looping over the
        # `exercises` dictionary -- `k` is the key (the exercise name) and`v`
        # is the value (the set of muscle groups for that entry).
        for k, v in exercises.items()
        # ...but we only add this `k` to the list if these two conditions hold:
        # - `k` isn't already in the `workout` list we're generating -- i.e.
        #   make sure we don't duplicate exercises in a workout.
        # - The intersection (as in set mathematics, the overlapping part of
        #   the venn diagram) of `v` (this exercise's muscle groups) and
        #   `last_groups` (the set of muscle groups from the previous iteration
        #   -- see below) is empty. This ensures we don't hit the same muscle
        #   group two exercises in a row.
        # Python-ism: `not <whatever>` means that `<whatever>` must evaluate to
        # False for the condition to fire. In Python, in addition to actual
        # True and False, other data types are implicitly True or False if
        # they're non-empty or empty, respectively. In this case an empty set
        # is implicitly False, and that's the logic we're counting on.
        # https://docs.python.org/3/library/stdtypes.html#truth-value-testing
        if k not in workout and not v.intersection(last_groups)
    ]
    # This is a stop-gap in case we somehow were unable to find any exercises
    # that match our criteria. If we allowed the loop to keep running, it would
    # blow up with a more inscrutable error later on.
    if len(candidates) == 0:
        # Python-ism: `raise` is how we generate an error that stops the normal
        # execution of the program.
        # https://docs.python.org/3/tutorial/errors.html
        raise RuntimeError("Ran out of exercises!")
    # So now we have `candidates` with some number of possibilities in it for
    # the next exercise in our workout. Pick one at random.
    # Python-ism: `random` is a standard library from which we're using the
    # `choice` function.
    # https://docs.python.org/3/library/random.html#random.choice
    ex = random.choice(candidates)
    # Now we replace `last_groups` with the set of muscle groups from the
    # exercise we just added to the workout. On the next loop iteration, this
    # will be what we use to ensure we don't repeat muscle groups.
    last_groups = exercises[ex]
    # Add the selected execrise to our workout.
    workout.append(ex)

# Okay, we finished looping, and at this point `workout` should be a list of
# `ex_per_cycle` exercise names. Print them out, one per line.
# Python-ism:
# `join()` is a function that takes a string on one side (in this case "\n",
# which means "newline") and a sequence on the other side (in this case our
# generated `workout` list of exercises) and produces one long string where
# all the elements of the sequence are joined together, separated by the
# delimiter.
# https://docs.python.org/3/library/stdtypes.html#str.join
print("\n".join(workout))

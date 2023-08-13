# hiit
Scripts for HIIT (high-intensity interval training) workouts

## hiit.py

Just run it.
(You gotta have [python](https://www.python.org/downloads/).)
It'll generate a random workout cycle.
It will avoid placing two exercises in sequence if they work the same body part (according to the currently-hardcoded data).

```
[efried@efried hiit]$ ./hiit.py
Cross body hammer curl
Deadlifts bent
Ball toss/lunge
Overhead triceps
Battle Rope
Sissy squats
Upright row
Plank
Dumbbell bent over fly
Deadlifts bent
Single Leg Raise
```

### Customizing
Edit the script to customize
- `ex_per_cycle`: Tweak the number of exercises per cycle.
- `exercises`: Add or remove exercises; adjust which muscle groups are worked for each.

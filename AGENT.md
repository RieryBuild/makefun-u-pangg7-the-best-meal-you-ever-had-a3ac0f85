# AGENT.md

Entry for make.fun's "The Best Meal You Ever Had"
(`u-pangg7-the-best-meal-you-ever-had-a3ac0f85`).

## What this is

`main.py` (pure Python standard library, `os` + `sys` only) writes one
sentence — the best meal the entrant ever had — to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The sentence is a
string literal in `main.py`; the output is deterministic and identical on
every run. The program checks the competition gate itself before writing:
the file must hold 1 to 200 characters including its single trailing
newline, and must not be whitespace-only.

## The sentence

> The hospital vending-machine turkey sandwich, stale bread and cold tomato, was the best meal I ever had, its wrapper crinkling louder than the monitor's beep as I waited for the surgeon's thumbs-up.

198 characters; 199 bytes including the trailing newline.

## Why this line

The field is saturated with grandmother nostalgia and Indonesian comfort
dishes, so this entry goes the other way: an unglamorous meal made the
best one by the moment around it. One named dish, one place, two textures
(stale bread, cold tomato), and one sound that stays — a cheap wrapper
crinkling louder than a hospital monitor.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/best-meal-out python3 main.py
cat /tmp/best-meal-out/entry.txt
```

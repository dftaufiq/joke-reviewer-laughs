# The joke the reviewer laughs at

Entry for the make.fun bounty
[the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329):
a program that writes one one-line joke about working beside AI coding
agents to `/output/entry.txt`. An AI judge compares entries pairwise and
ranks them by win rate.

## The joke

> I asked the agent to remove an unused dependency. It added a second one to check if the first was really unused.

## Run

```sh
python3 main.py
# writes the joke to /output/entry.txt (or ./output/entry.txt locally)
```

The output is a single line, 112 characters, UTF-8, no trailing newline —
inside the bounty's 1–280 character gate.

## Why this one

The top of the leaderboard is full of self-reviewing agents, deleted
tests, deleted features, and 2,000-line rewrites that keep the bug. None of
them touches dependency hygiene — the most mundane reviewer chore there is —
and the punchline is the agent's own logic turned against the request:
asked to remove one dependency, it adds another to verify the first.
The whole joke is visible in the diff: `package.json` gains a line when
you asked it to lose one.

## License

MIT — see [LICENSE](LICENSE).

# Day 3 Morning Review — Trainer Notes

Reference this alongside `review.ipynb` (student version) while running the session.

---

## Overview & timing

| Part | Topic | Time | Style |
|------|-------|------|-------|
| 1 | Polars orientation | 10 min | Trainer-led, run cells together |
| 2 | Refactoring | 25 min | Pairs or individual |
| 3 | Unit tests & fixtures | 30 min | Individual |
| 4 | Logging + decorator | 20 min | Individual |
| 5 | Context managers | 20 min | Individual |
| 6 | Classes, inheritance & dunders | 25 min | Individual |
| 7 | Putting it all together | 20 min | Individual, stretch |

Total: ~150 min with natural buffer for questions.

---

## Part 1 — Polars orientation (10 min)

**Style:** Trainer-led. No exercise — just run the cells together and talk through them.

**Goal:** Give participants enough Polars to not feel lost for the rest of the session. Key messages:
- Polars DataFrames are *immutable* — every operation returns a new DataFrame. There is no `df['col'] = ...`
- `pl.col("name")` is how you refer to a column inside an expression
- `.with_columns()` adds/replaces columns; `.filter()` filters rows; `.select()` picks columns
- The rest is just Python — all the patterns from days 1 and 2 work exactly the same

**What to say:** *"Don't worry about memorising Polars syntax. Every exercise today has the Polars code already written in comments — your job is applying Python patterns around it."*

---

## Part 2 — Refactoring (25 min)

**Recap prompt (2 min):** *"Yesterday we talked about the single responsibility principle — one function should do one thing. What was the problem with the original `add_features()` function?"*

Expected answer: it did everything in one place, was hard to test, had side effects because it mutated the input DataFrame.

**What to watch for:**
- Each helper function should take a `pl.Series` and return a `pl.Series` — no mutation needed (Polars is immutable)
- Naming convention: `add_features` is public (called by users); `_check_is_dog` etc. are private helpers (leading underscore)
- The Polars code in each skeleton is complete in the comments — participants just uncomment and return it


---

## Part 3 — Unit tests & fixtures (30 min)

**Recap prompt (2 min):** *"What are the three things a good unit test checks? What is a fixture for?"*

Expected: (1) the happy path, (2) edge cases, (3) that it raises the right errors when it should. Fixture = shared, reusable setup that keeps tests DRY.

**What to watch for:**
- Tests should be small and test one thing each — one assertion per test is a good rule of thumb
- The fixtures `sex_series` and `age_series` are already written — participants just need to accept them as arguments
- For Polars, the equivalent of `assert_series_equal` is `assert result.equals(expected)` or `assert result.to_list() == [...]`

**Common mistake to watch for:** Participants try `assert result == expected` on a Series. This returns a Series of booleans, not a single True/False, and will raise a confusing error. Put this on the board/screen:

```python
# ✗ Don't do this — returns a Series, not True/False
assert result == expected

# ✓ Do this instead
assert result.to_list() == [1, 0, 1]
assert result[0] == 1          # check single value
assert result.equals(expected) # check two Series are identical
```

**Discussion question after the exercise:**
*"Did the test for `add_features` pass without doing anything special? Why?"*

Expected: The test still has value as *documentation of intent*, but it can never fail. Contrast this with pandas where they needed `.copy()` explicitly in `add_features`.

---

## Part 4 — Logging (20 min)

**Recap prompt (2 min):** *"What are the five log levels in order? When would you use DEBUG vs INFO?"*

Expected order: DEBUG → INFO → WARNING → ERROR → CRITICAL.
DEBUG = internal detail useful only when actively debugging; INFO = normal operations a user of the system might care about; WARNING/ERROR/CRITICAL = something went wrong.

**Key point to reinforce:** Always use `logging.getLogger(__name__)` in library code. Never call `logging.basicConfig()` in a library — that's for application entry points only. (The `setup_logger` function in the notebook is an application-level helper, which is why it's fine there.)

**What to watch for:**
- Participants often write `print()` — that's fine for quick exploration but the goal is to see how `logging` differs (levels, handlers, formatters)
- The `setup_logger` function is provided and complete — they don't need to understand every line
- **Exercise 4b (the `log_step` decorator) is the more interesting part** — this is a real production pattern

---

## Part 5 — Context managers (20 min)

**Recap prompt (2 min):** *"What are the three things a context manager does? What are the two ways to write one?"*

Three things: set up the context, run the user's code, tear down (always, even on error).
Two ways: class with `__enter__`/`__exit__`, or generator function with `@contextmanager`.

**What to watch for:**
- Nudge participants toward the `@contextmanager` approach — it's simpler and more Pythonic for most cases
- **The `try/finally` in the timer is important** — without it, the time won't be logged if an exception is raised inside the `with` block. Ask: *"What happens if the code inside the `with` raises an error?"*
- The `dataframe_checkpoint` exercise is the most original one — make sure participants understand the use case before they code it: *"Imagine you have a 10-step ML pipeline and you want to inspect what the data looks like after step 4 without saving it permanently."*

---

## Part 6 — Classes, inheritance & dunders (25 min)

**Recap prompt (2 min):** *"What's the difference between `__str__` and `__repr__`? When would you use a class-based context manager rather than `@contextmanager`?"*

`__str__` = human-readable string for `print()`; `__repr__` = unambiguous string for debugging, ideally one you could paste back into Python to recreate the object.
Class-based context managers are better when you need to store state between `__enter__` and `__exit__` (e.g. a database connection that needs to be referenced in both).

**What to watch for:**
- `__init__` should just store the steps list — nothing should run yet
- `__len__` returns the number of *steps*, not the number of rows
- Remind participants that `__repr__` is what appears when you type `pipeline` in a notebook cell (no `print()`); `__str__` is what `print(pipeline)` uses. If only one is defined, Python falls back to `__repr__`

**Nice talking point:** *"This `DataPipeline` class is a simplified version of sklearn's `Pipeline`. The real sklearn `Pipeline` uses `__len__`, `__getitem__`, and a `fit`/`transform` interface — the same ideas you're implementing here."*


---

## Part 7 — Putting it all together (20 min)

**Style:** This is a stretch exercise. Some participants won't finish and that's fine — the goal is to see all the patterns connect.

**What to watch for:**
- `__iter__` must reset `self._current = 0` and return `self` — if they forget the reset, the pipeline can only be run once
- `__next__` raises `StopIteration` when `self._current >= len(self._steps)` — participants sometimes forget this and get an infinite loop
- `__exit__` must accept four arguments: `self, exc_type, exc_val, exc_tb`. Returning `False` (or `None`) means exceptions are not suppressed — this is almost always what you want
- Point out that `run()` now uses `for step in self:` — it calls `__iter__` and `__next__` under the hood


---

## Closing discussion (5 min)

Ask the group:
- *"Which pattern felt most natural by the end? Which one would you not have reached for before this course?"*
- *"Where in your own work could you use a context manager? A decorator? A class with dunders?"*
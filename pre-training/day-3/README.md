# Day 3 — OOP + File I/O: Task Tracker CLI

A command-line task tracker built with classes and JSON persistence.

## How to Use

```bash
python3 tasks.py add "Prepare Demo for Client"
python3 tasks.py add "Write unit tests"
python3 tasks.py list
python3 tasks.py done 1
python3 tasks.py list --filter done
python3 tasks.py list --filter todo
python3 tasks.py delete 2
```

## What's Inside

- **Task** class — holds id, title, status (`todo`/`done`), and `created_at` timestamp.
- **TaskManager** class — handles add, complete, delete, list. Reads from and writes to `tasks.json` so data sticks around between runs.
- CLI parsing with `sys.argv` — no external libraries.

## Error Handling

- If you pass an id that doesn't exist, it tells you.
- If `tasks.json` gets corrupted (bad JSON), it warns you and starts fresh instead of crashing.
- If you forget an argument, it prints usage help.

## What I Learned

Writing a class forces you to think about what data belongs together and what operations make sense on that data. Before today I would've just written a bunch of functions and a global list, this is cleaner because the TaskManager owns the data and the file, and nothing else touches it directly.

File I/O with JSON is straightforward but you have to think about edge cases: file doesn't exist yet, file is empty, file has garbage in it. Wrapping the load in a try/except felt like the right call.

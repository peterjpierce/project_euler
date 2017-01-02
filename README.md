# Project Euler Solutions

My solutions for problems from [Project Euler](https://projecteuler.net).  Just for fun.

## Prerequisites

These solutions require Python 3, but have no external dependencies, so
employing a virtual environment is entirely optional.  If you choose to, and
it exists at `<project_root>/env`, it will be activated automatically
at run time.

## Running Solutions

Use `run` to execute solutions, which establishes the environment
necessary for shared modules and simplifies CLI args.  Call it with
no arguments (or `-h` or `--help` or `help`) to see usage instructions:

```
usage: run <problem #>
   ex: run 2
       run 002
       run 002.py
```

*(Note that arguments may take any of the forms shown.)*

Alternatively, individual solution files (e.g., `solutions/002.py`) can
be run or debugged directly if your system.path includes the project root.
This can be set in your IDE, or via
`export PYTHONPATH=<project_root>:$PYTHONPATH` from the CLI.

## Feedback

These solutions have been tested with Python 3.5.2. Please share feedback and
questions with me at:  peterjpierce@gmail.com

Thank you!

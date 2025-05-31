# Mental Exercises Scripts

A collection of Python scripts designed to help you practice and improve various mental skills, from quick lettermath quizzes and chess‑board drills to memory palace exercises.


## Usage

Each script is standalone. To run a drill or game:

```bash
python path/to/script.py
```

Most scripts support simple command‑line arguments or will guide you via interactive prompts. For advanced configuration or explanation, check the top of each file for docstrings and usage examples.




## Memory Palace Trainer


A desktop GUI application to help you build and practice your own memory palaces. Create loci–item pairs one by one or in bulk, then quiz yourself endlessly on order and associations while tracking accuracy, response time, and streaks.


## Features

- **Create Palaces**  
  - Add loci–item pairs one at a time  
  - Bulk import via comma-separated lists  
- **Two Quiz Modes**  
  - **Order Quiz**: “What comes before/after X?”  
  - **Association Quiz**: Multiple-choice matching of loci and items  
- **Infinite Practice**  
  - Pools automatically reshuffle after every question set  
  - No forced time limits—practice until you click **Finish Test**  
- **Live Metrics**  
  - Accuracy (correct / total)  
  - Average response time  
  - Current and best correct streaks  
- **Plain-vanilla Dependencies**  
  - Written in python using the built-in `tkinter` GUI library  
  - Zero external packages required  


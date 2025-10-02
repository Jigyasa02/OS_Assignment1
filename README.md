# OS Lab Assignment 1 - Process Management

## 🎯 Objective
The purpose of this assignment is to simulate Linux process management operations using Python.  
It demonstrates *process creation, execution, zombie & orphan processes, process inspection using /proc, and process prioritization*.

---

## 📂 Files in this Repository
- process_management.py → Python code with all 5 tasks (menu-driven program).
- output.txt → Sample outputs from running the code.
- report.pdf → Detailed report with objectives, code snippets, and results.
- README.md → Instructions and documentation.

---

## 📝 Tasks Implemented
1. *Process Creation Utility*  
   - Create N child processes using os.fork().  
   - Each child prints its PID, Parent PID, and a message.  
   - Parent waits for all children.  

2. *Command Execution using exec()*  
   - Each child process executes a Linux command (ls, date, ps, etc.) using os.execvp() or subprocess.run().  

3. *Zombie & Orphan Processes*  
   - *Zombie:* Parent skips wait() after forking a child.  
   - *Orphan:* Parent exits before the child finishes.  
   - Verified using ps -el | grep defunct.  

4. *Inspect Process Info from /proc*  
   - Take PID as input.  
   - Display: process name, state, memory usage, executable path, and open file descriptors.  

5. *Process Prioritization*  
   - Create CPU-intensive processes.  
   - Assign different nice() values.  
   - Observe scheduler impact on execution.  

---

## ⚙️ Requirements
- *Operating System:* Linux (tested on Kali/Ubuntu)  
- *Python Version:* Python 3.x  

---

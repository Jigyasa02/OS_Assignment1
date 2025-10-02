TASK1:
# --------------------
# Task 1: create N children and wait
# --------------------
def task1_create_children(n):
    import os
    print(f"[TASK1] Parent PID {os.getpid()} creating {n} children")
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            # child process
            print(f"Child {i+1}: PID={os.getpid()}, PPID={os.getppid()}, msg='Hello from child {i+1}'")
            os._exit(0)   # child exits
        else:
            print(f"Parent: created child {pid}")
    # parent waits for all children
    while True:
        try:
            pid, status = os.wait()
            print(f"Parent: reaped child {pid} (status {status})")
        except ChildProcessError:
            break
    print("[TASK1] Done.")


TASK2:

# --------------------
# Task 2: have children execute a system command (execvp or subprocess)
# --------------------
def task2_exec_commands(n, command, use_exec=True):
    import os, subprocess
    print(f"[TASK2] Parent PID {os.getpid()} creating {n} children to run {command} (use_exec={use_exec})")
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            # child process
            print(f"[child {os.getpid()}] will run: {command}")
            if use_exec:
                # os.execvp replaces the child process image with the given command
                try:
                    os.execvp(command[0], command)
                except FileNotFoundError:
                    print("exec failed: command not found")
                    os._exit(1)
            else:
                # subprocess.run executes the command but stays inside child process
                subprocess.run(command)
                os._exit(0)
        else:
            print(f"Parent: forked child {pid}")
    # parent waits for all children
    while True:
        try:
            pid, status = os.wait()
            print(f"Parent: reaped child {pid} (status {status})")
        except ChildProcessError:
            break
    print("[TASK2] Done.")


TASK3:

# --------------------
# Task 3: Zombie & Orphan examples
# --------------------
def task3_zombie_demo(sleep_parent=30):
    import os, time
    print("[TASK3-ZOMBIE] Forking child; parent will NOT wait (sleeping).")
    pid = os.fork()
    if pid == 0:
        # child exits immediately
        print(f"[child {os.getpid()}] exiting immediately to become zombie.")
        os._exit(0)
    else:
        # parent sleeps instead of waiting
        print(f"[parent {os.getpid()}] child PID {pid}. Sleeping for {sleep_parent}s (do NOT run wait()).")
        time.sleep(sleep_parent)
        print("[parent] after sleep, now I'll wait to clean up (if child still exists).")
        try:
            os.wait()
        except Exception as e:
            print("wait error:", e)
        print("[TASK3-ZOMBIE] Done.")


def task3_orphan_demo(child_sleep=20):
    import os, time
    print("[TASK3-ORPHAN] Forking child; parent will exit immediately so child becomes orphan.")
    pid = os.fork()
    if pid == 0:
        # child keeps running even after parent exits
        print(f"[child {os.getpid()}] started; sleeping {child_sleep}s. Initial PPID={os.getppid()}")
        time.sleep(child_sleep)
        print(f"[child {os.getpid()}] after sleep. Current PPID={os.getppid()} (should be 1 or systemd pid)")
        os._exit(0)
    else:
        print(f"[parent {os.getpid()}] exiting immediately, child {pid} will be orphaned.")
        os._exit(0)


TASK4:

# --------------------
# Task 4: Inspect /proc/[pid] info
# --------------------
def task4_inspect(pid):
    import os
    pid = str(pid)
    base = f"/proc/{pid}"
    print(f"[TASK4] Inspecting {base}")
    try:
        with open(os.path.join(base, "status"), "r") as f:
            data = f.read()
            # print a few useful fields
            for key in ("Name:", "State:", "VmRSS:", "VmSize:"):
                for line in data.splitlines():
                    if line.startswith(key):
                        print(line)
    except Exception as e:
        print("Could not read status:", e)
    # exe path
    try:
        exe_path = os.readlink(os.path.join(base, "exe"))
        print("Executable path:", exe_path)
    except Exception as e:
        print("Could not read exe link:", e)
    # open file descriptors
    try:
        fds = os.listdir(os.path.join(base, "fd"))
        print("Open file descriptors:")
        for fd in fds:
            try:
                link = os.readlink(os.path.join(base, "fd", fd))
                print(f"  fd {fd} -> {link}")
            except Exception as e:
                print(f"  fd {fd} -> (error: {e})")
    except Exception as e:
        print("Could not list fd:", e)
    print("[TASK4] Done.")


TASK5:
Task 5: Priority (nice) and CPU-bound children
# --------------------
def cpu_work(duration_s=5):
    # simple CPU loop for duration
    t0 = time.time()
    x = 0
    while time.time() - t0 < duration_s:
        x += 1  # busy work
    return x

def task5_priority_demo(children=3, duration=5):
    ensure_unix()
    nice_values = [0, 5, 10][:children]  # example positive niceness va>    pids = []
    print(f"[TASK5] Parent {os.getpid()} creating {children} CPU-bound >    for i in range(children):
        pid = os.fork()
        if pid == 0:
            # child
            try:
                os.nice(nice_values[i])
                except Exception as e:
                print("Could not set nice:", e)
            start = time.time()
            print(f"[child {os.getpid()} nice={nice_values[i]}] start a>            count = cpu_work(duration)
            end = time.time()
            print(f"[child {os.getpid()} nice={nice_values[i]}] end at >            os._exit(0)
        else:
            pids.append(pid)
            print(f"Parent: forked child {pid} with target nice {nice_v>    # parent waits and logs order
    order = []
    while True:
        try:
            pid, status = os.wait()
            order.append(pid)
            print(f"Parent: reaped {pid}, status {status}")
        except ChildProcessError:
            break
    print("[TASK5] children reaped in order:", order)
    print("[TASK5] Done.")



find -D exec -name test.txt -type f -execdir mv {} example.txt \;

find -D exec -name example.txt -type f -execdir mv {} test.txt \;

Results:
DebugExec: launching process (argc=3): ‘mv’ ‘./example.txt’ ‘test.txt’
DebugExec: process (PID=96266) terminated with exit status: 0
DebugExec: launching process (argc=3): ‘mv’ ‘./example.txt’ ‘test.txt’
DebugExec: process (PID=96267) terminated with exit status: 0

---

find -D opt -name test.txt -type f -execdir mv {} example.txt \;

find -D opt -name example.txt -type f -execdir mv {} test.txt \;

Results:
    Too verbose

---

find -D rates -name test.txt -type f -execdir mv {} example.txt \;

find -D rates -name example.txt -type f -execdir mv {} test.txt \;

Results:
Predicate success rates after completion:
 ( -name example.txt [est success rate 0.1] [real success rate 2/17=0.1176] -a [est success rate 0.875] [real success rate 2/17=0.1176] [need type] -type f [est success rate 0.875] [real success rate 2/2=1]  ) -a [est success rate 0.0875] [real success rate 2/17=0.1176] -execdir mv [est success rate 1] [real success rate 2/2=1] 

---

find -D search -name test.txt -type f -execdir mv {} example.txt \;

find -D search -name example.txt -type f -execdir mv {} test.txt \;

Results:
    Too verbose

---

find -D stat -name test.txt -type f -execdir mv {} example.txt \;

find -D stat -name example.txt -type f -execdir mv {} test.txt \;

Results:
    No output

---

find -D tree -name test.txt -type f -execdir mv {} example.txt \;

find -D tree -name example.txt -type f -execdir mv {} test.txt \;

Results:

Predicate List:
[-name] [-a] [-type] [-a] [-execdir] 
Eval Tree:
    <...>
Normalized Eval Tree:
    <...>
Optimized Eval Tree:
    <...>
Optimized command line:
 ( -name test.txt [est success rate 0.1] -a [est success rate 0.875] [need type] -type f [est success rate 0.875]  ) -a [est success rate 0.0875] -execdir mv [est success rate 1] 

---

find -D all -name test.txt -type f -execdir mv {} example.txt \;

find -D all -name example.txt -type f -execdir mv {} test.txt \;

---

find -O3 -name test.txt -type f -execdir mv {} example.txt \;

find -O3 -name example.txt -type f -execdir mv {} test.txt \;

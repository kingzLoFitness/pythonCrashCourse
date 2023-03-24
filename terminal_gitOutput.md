Welcome to Linux Lite 6.2 kingzlofitness
 
Tuesday 14 March 2023, 07:28:02
Memory Usage: 4885/7875MB (62.03%)
Disk Usage: 218/233GB (99%)
Support - https://www.linuxliteos.com/forums/ (Right click, Open Link)
 
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git add README.md
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   README.md

 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git commit -m "Add README.md"
[master 02072bf] Add README.md
 1 file changed, 10 insertions(+)
 create mode 100644 README.md
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git log 
commit 02072bf9149d19ba6f008002cac23b5b14cd9e94 (HEAD -> master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:29:00 2023 -0400

    Add README.md

commit c535ca99fa86e330eb07b2499f31477a036bc7ab (origin/master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:17:33 2023 -0400

    add new files from ch6_dictinary

commit 5180e02f34e7013855cbae5365a357825f1ef246
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Thu Feb 23 17:38:02 2023 -0500

    Files of Work done a few month ago in Python Programming.
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 654 bytes | 654.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:kingzLoFitness/pythonCrashCourse.git
   c535ca9..02072bf  master -> master
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git rm '/home/kingzlofitness/Documents/Programming/Python/PythonCrashCourse/Python Crash Course - A Hands-On, Project-Based Introduction to Programming.pdf'
rm 'Python Crash Course - A Hands-On, Project-Based Introduction to Programming.pdf'
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    Python Crash Course - A Hands-On, Project-Based Introduction to Programming.pdf

 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git restore
fatal: you must specify path(s) to restore
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  128  git restore '/home/kingzlofitness/Documents/Programming/Python/PythonCrashCourse/Python Crash Course - A Hands-On, Project-Based Introduction to Programming.pdf'
error: pathspec '/home/kingzlofitness/Documents/Programming/Python/PythonCrashCourse/Python Crash Course - A Hands-On, Project-Based Introduction to Programming.pdf' did not match any file(s) known to git
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  1  git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    Python Crash Course - A Hands-On, Project-Based Introduction to Programming.pdf

 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git restore
fatal: you must specify path(s) to restore
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  128  git push
Everything up-to-date
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git log
commit 02072bf9149d19ba6f008002cac23b5b14cd9e94 (HEAD -> master, origin/master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:29:00 2023 -0400

    Add README.md

commit c535ca99fa86e330eb07b2499f31477a036bc7ab
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:17:33 2023 -0400

    add new files from ch6_dictinary

commit 5180e02f34e7013855cbae5365a357825f1ef246
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Thu Feb 23 17:38:02 2023 -0500

    Files of Work done a few month ago in Python Programming.
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    Python Crash Course - A Hands-On, Project-Based Introduction to Programming.pdf

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    python-crash-course.pdf
        deleted:    python_crash_course_2nd_edition.pdf

 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git commit -m "deleted .pdf files"
[master bd0f7d5] deleted .pdf files
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 Python Crash Course - A Hands-On, Project-Based Introduction to Programming.pdf
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git log
commit bd0f7d559079d1665cc1086f7f270f3ee2c74b1a (HEAD -> master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:55:44 2023 -0400

    deleted .pdf files

commit 02072bf9149d19ba6f008002cac23b5b14cd9e94 (origin/master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:29:00 2023 -0400

    Add README.md

commit c535ca99fa86e330eb07b2499f31477a036bc7ab
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:17:33 2023 -0400

    add new files from ch6_dictinary

commit 5180e02f34e7013855cbae5365a357825f1ef246
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Thu Feb 23 17:38:02 2023 -0500

    Files of Work done a few month ago in Python Programming.

 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  SIGINT  q
Command 'q' not found, but can be installed with:
sudo snap install q                       # version 1.6.3-1, or
sudo apt  install python3-q-text-as-data  # version 3.1.6-1
See 'snap info q' for additional versions.
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  127  git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    python-crash-course.pdf
        deleted:    python_crash_course_2nd_edition.pdf

no changes added to commit (use "git add" and/or "git commit -a")
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git rm
fatal: No pathspec was given. Which files should I remove?
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  128  git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    python-crash-course.pdf
        deleted:    python_crash_course_2nd_edition.pdf

no changes added to commit (use "git add" and/or "git commit -a")
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git log
commit bd0f7d559079d1665cc1086f7f270f3ee2c74b1a (HEAD -> master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:55:44 2023 -0400

    deleted .pdf files

commit 02072bf9149d19ba6f008002cac23b5b14cd9e94 (origin/master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:29:00 2023 -0400

    Add README.md

commit c535ca99fa86e330eb07b2499f31477a036bc7ab
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:17:33 2023 -0400

    add new files from ch6_dictinary

commit 5180e02f34e7013855cbae5365a357825f1ef246
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Thu Feb 23 17:38:02 2023 -0500

    Files of Work done a few month ago in Python Programming.
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    python-crash-course.pdf
        deleted:    python_crash_course_2nd_edition.pdf

no changes added to commit (use "git add" and/or "git commit -a")
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git commit -m "deleted two .pdf files"
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    python-crash-course.pdf
        deleted:    python_crash_course_2nd_edition.pdf

no changes added to commit (use "git add" and/or "git commit -a")
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  1  git rm python-crash-course.pdf
rm 'python-crash-course.pdf'
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    python-crash-course.pdf

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    python_crash_course_2nd_edition.pdf

 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git rm python_crash_course_2nd_edition.pdf
rm 'python_crash_course_2nd_edition.pdf'
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    python-crash-course.pdf
        deleted:    python_crash_course_2nd_edition.pdf

 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git commit -m "deleted 2 .pdf's"
[master fb27d31] deleted 2 .pdf's
 2 files changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 python-crash-course.pdf
 delete mode 100644 python_crash_course_2nd_edition.pdf
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git log
commit fb27d31ab3b85e7b727dc17f7ce430f856ddbd79 (HEAD -> master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:59:39 2023 -0400

    deleted 2 .pdf's

commit bd0f7d559079d1665cc1086f7f270f3ee2c74b1a
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:55:44 2023 -0400

    deleted .pdf files

commit 02072bf9149d19ba6f008002cac23b5b14cd9e94 (origin/master)
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:29:00 2023 -0400

    Add README.md

commit c535ca99fa86e330eb07b2499f31477a036bc7ab
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Tue Mar 14 07:17:33 2023 -0400

    add new files from ch6_dictinary

commit 5180e02f34e7013855cbae5365a357825f1ef246
Author: Kingsley Cross <kingzlofitness@gmail.com>
Date:   Thu Feb 23 17:38:02 2023 -0500

    Files of Work done a few month ago in Python Programming.
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git log --oneline
fb27d31 (HEAD -> master) deleted 2 .pdf's
bd0f7d5 deleted .pdf files
02072bf (origin/master) Add README.md
c535ca9 add new files from ch6_dictinary
5180e02 Files of Work done a few month ago in Python Programming.
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 424 bytes | 424.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
To github.com:kingzLoFitness/pythonCrashCourse.git
   02072bf..fb27d31  master -> master
 kingzlofitness   master  …  Programming  Python  PythonCrashCourse  
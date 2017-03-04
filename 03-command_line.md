# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > show current working directory path:
> > pwd
> >
> > creating a directory:
> > 
> > mkdir dirname
> > 
> > 
> > deleting a directory:
> > 
> > rm -r dirname
> > 
> >
> > creating a file using `touch` command
> > touch filename
> > 
> > deleting a file
> > rm filename
> > 
> > renaming a file
> > mv filename newfilename
> > 
> > listing hidden files
> > ls -a
> >
> > copying a file from one directory to another
> > cp filename newdir/filename

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls: list files in current directory
> > ls -a: list all files in current directory, including hidden files
> > ls -l: long list of all files in current, shows permissions, file sizes, and date/time of last modification
> > ls -lh: same as "ls -l", but file sizes are shortened by using unit prefixes (B, K, M, etc)
> > ls -lah: same as "ls -lh", but including hidden files
> > ls -t: list of files in current directory sorted by modification time/date
> > ls -Glp: long ("l") file list where files are colorized by type ("G") and a "/" is added to folder names ("p")

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > Ones I didn't know about and like:
> > ls -R: file list of current directory and subdirectories, which would save time rather than searching subdirectories one at a time.
> > ls -c: sort by oldest files first
> > ls -r: reverse order of file list
> > ls -m: comma-separated list, good for creating csv file of file list?
> > ls -u: sort by last access

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 


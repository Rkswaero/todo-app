#!/usr/bin/env python3
from datetime import date
import sys
def display_help():
    print('Usage :-')
    print('$ ./todo add "todo item"                 # Add a new todo')
    print('$ ./todo insert "todo item" NUMBER       # Insert at a given position')
    print('$ ./todo update "todo item" NUMBER       # Update at a given position')
    print('$ ./todo swap NUMBER NUMBER              # Swap given todos')
    print('$ ./todo ls                              # Show remaining todos')
    print('$ ./todo del NUMBER                      # Delete a todo')
    print('$ ./todo done NUMBER                     # Complete a todo')
    print('$ ./todo help                            # Show usage')
    print('$ ./todo report                          # Statistics')
argument_size = len(sys.argv)
deleted_todo = 0
if argument_size == 1:
    display_help()
elif argument_size == 2:
    if sys.argv[1] == "report":
        file = open('todo.txt', 'r')
        pending_count = len(file.readlines())
        file1 = open('done.txt', 'r')
        completed_count = len(file1.readlines())
        print("{} Pending : {} Completed : {}".format(date.today(),pending_count,completed_count))
    elif sys.argv[1] == "help":
        display_help()
    elif sys.argv[1] == "ls":
        file = open('todo.txt', 'r')
        Lines = file.readlines()
        count = len(Lines)
        for line in Lines[::-1]:
            print("[{}] {}".format(count, line.strip()))
            count -= 1     
elif argument_size == 3 and sys.argv[1] == "add":
    file = open('todo.txt', 'a')
    file.writelines(sys.argv[2] + '\n')
elif argument_size == 3 and sys.argv[1] == "del":
    file = open('todo.txt','r')
    Lines = file.readlines()
    del Lines[int(sys.argv[2]) - 1]
    file = open('todo.txt','w')
    for line in Lines:
        file.write(line)
    print("Deleted todo #{}".format(sys.argv[2]))
elif argument_size == 3 and sys.argv[1] == "done":  
    file = open('todo.txt','r')
    Lines = file.readlines()
    file_1 = open('done.txt','a')
    file_1.write(Lines[int(sys.argv[2]) - 1])
    del Lines[int(sys.argv[2]) - 1]
    file = open('todo.txt','w')
    for line in Lines:
        file.write(line)
    print("Marked #{} to as done".format(sys.argv[2]))
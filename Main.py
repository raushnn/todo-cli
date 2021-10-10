from modules.TodoList import TodoList
from modules.TodoListChecker import checker
import threading
import time
import sys

# This is a sample intended application of the to-do cli

if __name__ == "__main__":
    t = TodoList()
    def main_program():
        INPUT= int(input("""Welcome to Command Line based ToDo List.
        Enter 1 to add task to your todo List.
        Enter 2 to view your upcoming task:"""))
        # This will be done via interactive CLI (WIP)
        task= ''; description= ''; minute_deadline_offset=0
        x=-1
        if INPUT==1:
            while True:
                if x==2:
                    sys.exit()
                elif x==0:
                    print("Going back")
                    break
                else:
                    task= input("Enter the task name:\n")
                    description= input("Enter the description of the task:\n")
                    minute_deadline_offset= float(input("Enter the minute deadline offset:\n"))
                    t.add_todo(task, description, minute_deadline_offset)
                    x= int(input("Press 0 if you want to go back.\nPress 2 if you want to exit.\n"))
                    print(t.get_next_todo())
            main_program()
        elif INPUT==2:
            while True:
                if x==2:
                    sys.exit()
                elif x==0:
                    print("Going back")
                    break
                print(t.get_next_todo())
                x= int(input("Press 1 if you want to go back.\nPress 2 if you want to exit\n"))
            main_program()
    z=int(input("Enter 1 to start:\nEnter 0 to exit:\n"))
    if z==1:
        main_program()
    if z==0:
        sys.exit()
    # t.add_todo(
    #     task='Wash Dishes',
    #     description="Don't forget to use Vim bar also",
    #     minute_deadline_offset=1.5)

    # t.add_todo(
    #     task='Hang Clothes',
    #     description="Also install new hanging rope",
    #     minute_deadline_offset=0.5)

    # t.add_todo(
    #     task='Run Washing Machine',
    #     description="Also use Comfort in the end",
    #     minute_deadline_offset=1)

    # multithreading used here st it doesn't interfere with Future to-do Insertion
    t1 = threading.Thread(target=checker, args=(t,), name='t1')
    # this makes the thread auto close when the parent thread closes
    t1.setDaemon(True)
    t1.start()

    # WIP: as there should be a Interactive CLI, there will be something
    # similar to an infinite loop with KeyboardInterrupt/exit() close
    # here this is simulated as a sleep timer
    time.sleep(100)
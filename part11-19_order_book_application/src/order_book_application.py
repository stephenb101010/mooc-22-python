class Task:
    total_tasks = 0
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self. workload = workload
        Task.total_tasks += 1
        self.id = Task.total_tasks
        self.__finished = False

    def is_finished(self):
        return self.__finished

    def finished_status(self):
        finished = "NOT FINISHED"
        if self.__finished:
            finished = "FINISHED"
        return finished

    def mark_finished(self):
        self.__finished = True

    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished_status()}"

class OrderBook:
    def __init__(self):
        self.__tasks = []

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.__tasks.append(task)

    def all_orders(self):
        return self.__tasks

    def programmers(self):
        return list(set([task.programmer for task in self.__tasks]))

    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f"Order with {id} does not exist")

    def finished_orders(self):
        return [task for task in self.__tasks if task.is_finished() == True]

    def unfinished_orders(self):
        return [task for task in self.__tasks if task.is_finished() == False]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f"No such {programmer} exists")
        tasks = [task for task in self.__tasks if task.programmer == programmer]
        finished = 0
        unfinished = 0
        finished_workload = 0
        unfinished_workload = 0
        for task in tasks:
            if task.is_finished():
                finished += 1
                finished_workload += task.workload
            else:
                unfinished += 1
                unfinished_workload += task.workload
        return (finished, unfinished, finished_workload, unfinished_workload)

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def __error(self):
        print("erroneous input")

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        prog_load = input("programmer and workload estimate: ")
        prog_load = prog_load.split(" ")
        programmer = prog_load[0]
        try:
            workload = int(prog_load[1])
        except:
            self.__error()
            return
        self.__orderbook.add_order(description, programmer, workload)
        print("added!")

    def list_finished_tasks(self):
        if len(self.__orderbook.finished_orders()):
            for task in self.__orderbook.finished_orders():
                print(task)
        else:
            print("no finished tasks")

    def list_unfinished_tasks(self):
        if len(self.__orderbook.unfinished_orders()):
            for task in self.__orderbook.unfinished_orders():
                print(task)
        else:
            print("no unfinished tasks")

    def mark_finished(self):
        try:
            id = int(input("id: "))
        except:
            self.__error()
            return

        ids = [task.id for task in self.__orderbook.all_orders()]
        if id not in ids:
            self.__error()
            return

        self.__orderbook.mark_finished(id)
        print("marked as finished")

    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def programmer_status(self):
        programmer = input("programmer: ")
        if programmer not in self.__orderbook.programmers():
            self.__error()
            return
        f, u, fw, uw = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {f} not finished {u}, hours: done {fw} scheduled {uw}")

    def execute(self):
        self.help()
        while True:
            print()
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                self.add_order()
            elif command == 2:
                self.list_finished_tasks()
            elif command == 3:
                self.list_unfinished_tasks()
            elif command == 4:
                self.mark_finished()
            elif command == 5:
                self.programmers()
            elif command == 6:
                self.programmer_status()
            else:
                self.help()

app = OrderBookApplication()
app.execute()

'''
class Task:
    id = 0
    @classmethod 
    def new_id(cls):
        Task.id += 1
        return Task.id

    def __init__(self, description, programmer, workload):
        self.programmer = programmer
        self.description = description
        self.workload = workload
        self.id = Task.new_id()
        self.finished = False

    def is_finished(self):
        return self.finished 

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        status = "NOT FINISHED" if not self.finished else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.__tasks = []

    def add_order(self, description, programmer, workload):
        self.__tasks.append(Task(description, programmer, workload))
 
    def all_orders(self):
        return self.__tasks

    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))

    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        # not incorrect
        raise ValueError("wrong id")

    def unfinished_orders(self):
        return [t for t in self.__tasks if not t.is_finished()]

    def finished_orders(self):
        return [t for t in self.__tasks if t.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError("Programmer does not exists")
        finished_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished() ]
        not_finished_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished() ]
        finished_hours = sum(t.workload for t in finished_tasks)
        not_finished_hours = sum(t.workload for t in not_finished_tasks)
        return (len(finished_tasks), len(not_finished_tasks), finished_hours, not_finished_hours)

class Application:
    def __init__(self):
        self.orders = OrderBook()

    def instructions(self):
        # Defining multiline string is possible with triple apostrophes
        instructions_str = """
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer"""
        print(instructions_str)

    def add(self):
        description = input("description: ")
        programmer_and_estimate = input("programmer and workload estimate: ")
        try:
            programmer = programmer_and_estimate.split(' ')[0]
            workload = int(programmer_and_estimate.split(' ')[1])
            self.orders.add_order(description, programmer, workload)
            print("added!")
        except:
            print("erroneous input")

    def unfinished(self):
        for task in self.orders.unfinished_orders():
            print(task)

    def finished(self):
        finished_orders = self.orders.finished_orders()
        if len(finished_orders)==0:
            print("no finished tasks")
            return

        for task in finished_orders:
            print(task)

    def programmers(self):
        for programmer in self.orders.programmers():
            print(programmer)

    def mark_finished(self):
        try:
            order_id = int(input("id: "))
            self.orders.mark_finished(order_id)
            print("marked as finished")
        except:
            print("erroneous input")

    def programmers_status(self):
        programmer = input("programmer: ")
        if not programmer in self.orders.programmers():
            print("erroneous input")
            return
        status = self.orders.status_of_programmer(programmer)
        print(f"tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}")

    def run(self):
        self.instructions()
        while True:
            command = input("command: ")
            if command == "0":
                return
            elif command == "1":
                self.add()
            elif command == "2":
                self.finished()
            elif command == "3":
                self.unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.programmers_status()

Application().run()
'''
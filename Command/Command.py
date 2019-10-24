class Command():
    def execute(self):
        pass

class LunchCommand(Command):
    def __init__(self, lunch):
        self.lunch = lunch

    def execute(self):
        self.lunch.make_lunch()

class DinnerCommand(Command):
    def __init__(self, dinner):
        self.dinner = dinner

    def execute(self):
        self.dinner.make_dinner()

class Lunch:
    def make_lunch(self):
        print("Lunch is being made")

class Dinner:
    def make_dinner(self):
        print("Dinner is being made")

class MealInvoker:
    def __init__(self, command=None):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()

def main():
    queue= list()
    lunch = Lunch()
    dinner = Dinner()
    lcommand = LunchCommand(lunch)
    dcommand = DinnerCommand(dinner)
    queue.append(lcommand)
    queue.append(dcommand)
    invoker = MealInvoker()
    while(len(queue)>0):
        invoker.set_command(queue.pop())
        invoker.invoke()

if __name__=='__main__':
    main()


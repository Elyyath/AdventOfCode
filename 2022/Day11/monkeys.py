with open("C:/Users/Elias/Documents/AdventOfCode/2022/Day11/input.txt") as input:
    lines = [line.strip() for line in input]
    monkeys = []
    inspectations = []
    monkeyBusiness = 0
    class Item:
        def __init__(self, worryLevel):
            self.worryLevel = worryLevel

        def __str__(self):
            return f"{self.worryLevel}"

    class Monkey:
        def __init__(self, id):
            self.id = id
            self.items = []
            self.trueMonkey = 0
            self.falseMonkey = 0
            self.divisibleBy = 0
            self.operand = ""
            self.operationValue = 0
            self.inspectations = 0
        def operate(self, old):
            if self.operand == "+":
                return old + self.operationValue
            elif self.operand == "-":
                return old - self.operationValue
            elif self.operand == "*":
                return old * self.operationValue
            elif self.operand == "/":
                return old / self.operationValue
            elif self.operand == "^":
                return old * old
            

        def test(self, itemValue):
            if itemValue % self.divisibleBy == 0:
                return self.trueMonkey

            return self.falseMonkey

    def takeTurn(monkey):
        if len(monkey.items) == 0:
            return
        
        for item in monkey.items:
            monkey.inspectations += 1
            item.worryLevel = monkey.operate(item.worryLevel)
            item.worryLevel = int(item.worryLevel / 3)
            newMonkey = monkeys[monkey.test(item.worryLevel)]
            newMonkey.items.append(item)
        monkey.items = []

    def listInspectations():
        for monkey in monkeys:
            inspectations.append(monkey.inspectations)

    #create Monkeys
    for line in lines:
        if line:
            line = line.split(":")
            category = line[0]
            if "Monkey" in category:
                id = category.split(" ")[1]
                monkey = Monkey(id)
                monkeys.append(monkey)
            elif category == "Starting items":
                items = [int(item) for item in line[1].split(",")]
                for worryLevel in items:
                    monkeys[-1].items.append(Item(worryLevel))
            elif category == "Operation":
                operation = line[1].split(" ")
                if operation[-1] == "old":
                    
                    monkeys[-1].operand = "^"
                else:
                    monkeys[-1].operationValue = int(operation[-1])
                    monkeys[-1].operand = operation[-2]
            elif category == "Test":
                value = int(line[1].split(" ")[-1])
                monkeys[-1].divisibleBy = value
            elif "true" in category:
                id = int(line[1].split(" ")[-1])
                monkeys[-1].trueMonkey = id
            else:
                id = int(line[1].split(" ")[-1])
                monkeys[-1].falseMonkey = id

    


    #Take turns
    for round in range(20):
        for monkey in monkeys:
            takeTurn(monkey)

    listInspectations()

    for monkey in monkeys:
        print(f"monkey {monkey.id} inspected {monkey.inspectations} items.")
    
    inspectations = sorted(inspectations)
    monkeyBusiness = inspectations[-1] * inspectations[-2]
    print(monkeyBusiness)

    
    



        # for item in monkey.items:
        #     print(item)



        
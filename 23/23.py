class StateMachine:
    def __init__(self, inst_list):
        self.a = 0
        self.b = 0
        self.head = 0
        self.instructions = tuple(inst_list)
        self.instr_len = len(self.instructions)
        
    def read(self):
        current = self.instructions[self.head]
        if current[0] == 'hlf':
            self.half(current[1])
        elif current[0] == 'tpl':
            self.triple(current[1])
        elif current[0] == 'inc':
            self.increment(current[1])
        elif current[0] == 'jmp':
            self.jump(current[1])
        elif current[0] == 'jie':
            self.jumpifeven(current[1], current[2])
        elif current[0] == 'jio':
            self.jumpifone(current[1], current[2])
        else:
            raise ValueError('Bad Instruction Read At Entry: %d' % self.head)
        
    def half(self, register):
        if register == 'a':
            self.a = self.a // 2
        elif register == 'b':
            self.b = self.b // 2
        self.head += 1
        
    def triple(self, register):
        if register == 'a':
            self.a *= 3
        elif register == 'b':
            self.b *= 3
        self.head += 1
        
    def increment(self, register):
        if register == 'a':
            self.a += 1
        elif register == 'b':
            self.b += 1
        self.head += 1
        
    def jump(self, offset):
        self.head += int(offset)
        
    def jumpifeven(self, register, offset):
        if register == 'a':
            if self.a % 2 == 0:
                self.head += int(offset)
            else:
                self.head += 1
        elif register == 'b':
            if self.b % 2 == 0:
                self.head += int(offset)
            else:
                self.head += 1
                
    def jumpifone(self, register, offset):
        if register == 'a':
            if self.a == 1:
                self.head += int(offset)
            else:
                self.head += 1
                
        elif register == 'b':
            if self.b == 1:
                self.head += int(offset)
            else:
                self.head += 1
        
    def run(self):
        while 0 <= self.head < self.instr_len:
            self.read()
                
data = []

with open("input.txt", "r") as input:
    for line in input:
        if ',' in line:
            instruc, reg, offset = line.split()
            data.append((instruc, reg[0], offset))
        else:
            instruc, reg = line.split()
            data.append((instruc, reg))
            
santa = StateMachine(data)
santa.run()
print(santa.b)

santa2 = StateMachine(data)
santa2.a = 1
santa2.run()
print(santa2.b)
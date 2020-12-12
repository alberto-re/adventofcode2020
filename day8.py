#!/usr/bin/env python3
# --- Day 8: Handheld Halting ---


class Vm:
    def __init__(self):
        self._acc = 0
        self._ip = 0
        self._hist = {}

    def run(self, program):
        while self._ip < len(program):
            opcode, arg = program[self._ip].split()
            self._hist[self._ip] = 1
            if opcode == "acc":
                self._acc += int(arg)
            elif opcode == "nop":
                pass
            elif opcode == "jmp":
                if self._ip + int(arg) in self._hist.keys():
                    return 1
                self._ip += int(arg)
                continue
            else:
                raise Exception(f"invalid opcode {opcode}")
            self._ip += 1
        return 0

    @property
    def acc(self):
        return self._acc

    @property
    def ip(self):
        return self._ip


def mutate_program(program, pos, mutation):
    mutated = []
    for i, instr in enumerate(program):
        if i == pos:
            mutated.append(mutation)
        else:
            mutated.append(instr)
    return mutated


def fix_program(program):
    for op in range(len(program) - 1, -1, -1):
        opcode, arg = program[op].split()
        if opcode == "acc":
            continue
        if opcode == "nop":
            opcode = "jmp"
        else:
            opcode = "nop"
        vm = Vm()
        exit_code = vm.run(mutate_program(program, op, f"{opcode} {arg}"))
        if exit_code == 0:
            return vm.acc
    raise Exception("solution not found")


lines = []
with open("input/day8.txt") as f:
    lines = [line.rstrip() for line in f]


vm = Vm()
vm.run(lines)
print("part1 solution:", vm.acc)

print("part2 solution:", fix_program(lines))

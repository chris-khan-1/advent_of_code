def parse_instruction_list(instruction_list: list) -> dict:
    instructions = dict()
    for instruction in instruction_list:
        operation, output_wire = instruction.split(" -> ")
        instructions[output_wire] = operation
    return instructions


def evaluate(wire: str, instructions: dict, wire_cache: dict = {}):
    if wire.isdigit():
        return int(wire)
    if wire in wire_cache:
        return wire_cache[wire]

    instruction = instructions[wire]

    parts = instruction.split(" ")

    if "AND" in parts:
        left = evaluate(wire=parts[0], instructions=instructions, wire_cache=wire_cache)
        right = evaluate(
            wire=parts[2], instructions=instructions, wire_cache=wire_cache
        )
        result = left & right
    elif "OR" in parts:
        left = evaluate(wire=parts[0], instructions=instructions, wire_cache=wire_cache)
        right = evaluate(
            wire=parts[2], instructions=instructions, wire_cache=wire_cache
        )
        result = left | right
    elif "LSHIFT" in parts:
        left = evaluate(wire=parts[0], instructions=instructions, wire_cache=wire_cache)
        shift_ammount = int(parts[2])
        result = left << shift_ammount
    elif "RSHIFT" in parts:
        left = evaluate(wire=parts[0], instructions=instructions, wire_cache=wire_cache)
        shift_ammount = int(parts[2])
        result = left >> shift_ammount
    elif "NOT" in parts:
        value = evaluate(
            wire=parts[1], instructions=instructions, wire_cache=wire_cache
        )
        result = ~value & 0xFFFF
    else:
        result = evaluate(
            wire=parts[0], instructions=instructions, wire_cache=wire_cache
        )

    wire_cache[wire] = result
    return result


if __name__ == "__main__":
    with open("./2015/7/input.txt", "r") as input_file:
        instruction_list = [line.rstrip() for line in input_file]
        instructions = parse_instruction_list(instruction_list)
        # # Part 1
        wire_a_signal = evaluate(wire="a", instructions=instructions, wire_cache={})
        # Part 2
        instructions["b"] = str(wire_a_signal)
        new_wire_a_signal = evaluate(wire="a", instructions=instructions, wire_cache={})

    with open("./2015/7/solution.txt", "w") as output_file:
        output_file.write(f"Part 1: The signal provided to wire a is {wire_a_signal}\n")
        output_file.write(
            f"Part 2: The new signal provided to wire a is {new_wire_a_signal}"
        )

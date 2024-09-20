def generate_assembly(ast):
    assembly = []
    register_count = 1
    
    for node in ast:
        if node.type == 'assignment':
            var = node.children[0].value
            value = node.children[1].value
            
            # Load immediate value into a register (RISC style)
            assembly.append(f"LI R{register_count}, {value}")  # LI = Load Immediate
            assembly.append(f"STORE R{register_count}, {var}")  # Store value into memory
            register_count += 1

    return '\n'.join(assembly)

from flask import Flask, jsonify, request
from compiler.lexer import lexer
from compiler.parser import parser
from compiler.codegen import generate_assembly
from compiler.assembler import assemble
from compiler.simulator import simulate

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.json.get('code')
    
    # 1. Lexical Analysis
    tokens = lexer(code)
    
    # 2. Parsing
    ast = parser(tokens)
    
    # 3. Code Generation (Assembly)
    assembly_code = generate_assembly(ast)
    
    # 4. Assembly to Machine Code
    machine_code = assemble(assembly_code)
    
    # 5. Simulate Execution on RISC Architecture
    execution_result = simulate(machine_code)
    
    return jsonify({
        'tokens': tokens,
        'ast': ast,
        'assembly': assembly_code,
        'machine_code': machine_code,
        'execution_result': execution_result
    })

if __name__ == '__main__':
    app.run(debug=True)

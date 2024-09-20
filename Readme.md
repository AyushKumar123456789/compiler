# RISC Compiler Project

## Overview

This project is a simple RISC-based compiler that processes pseudo-code through multiple stages: lexical analysis, parsing, assembly code generation, machine code generation, and simulation of execution. The project consists of a Flask backend and a React frontend.

Project is in just starting phase containin lots of bugs and still to write 80% of code

## Features

- Lexical analysis to tokenize the input code.
- Parsing to generate an Abstract Syntax Tree (AST).
- Code generation to create RISC-like assembly code.
- Machine code generation from assembly.
- Simulation of execution on a RISC architecture.

## Project Structure

```
compiler-project/
│
├── backend/                   # Flask backend
│   ├── app.py                 # Main application
│   ├── compiler/              # Compiler modules
│   │   ├── lexer.py           # Lexer for tokenization
│   │   ├── parser.py          # Parser for generating AST
│   │   ├── codegen.py         # Code generation for assembly
│   │   ├── assembler.py        # Assembly to machine code
│   │   └── simulator.py        # Execution simulation
│   └── requirements.txt       # Required Python packages
│
└── frontend/                  # React frontend
    ├── components/            # React components
    │   ├── CodeEditor.js      # Code editor component
    │   └── CompilationResults.js # Results display component
    └── pages/
        └── index.js           # Main page
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm run dev
   ```

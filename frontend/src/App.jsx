import { useState } from "react";
import CodeEditor from "./components/CompilationResults";
import CompilationResults from "./components/CodeEditor";

export default function App() {
  const [results, setResults] = useState(null);

  const handleCompile = async (code) => {
    const response = await fetch("http://localhost:5000/compile", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code }),
    });
    const data = await response.json();
    setResults(data);
  };

  return (
    <div>
      <h1>RISC Compiler Simulation</h1>
      <CodeEditor onSubmit={handleCompile} />
      {results && <CompilationResults results={results} />}
    </div>
  );
}

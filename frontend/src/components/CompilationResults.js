export default function CompilationResults({ results }) {
  return (
    <div>
      <h3>Tokens:</h3>
      <pre>{JSON.stringify(results.tokens, null, 2)}</pre>

      <h3>AST:</h3>
      <pre>{JSON.stringify(results.ast, null, 2)}</pre>

      <h3>Assembly Code:</h3>
      <pre>{results.assembly}</pre>

      <h3>Machine Code:</h3>
      <pre>{results.machine_code.join("\n")}</pre>

      <h3>Execution Result:</h3>
      <pre>{JSON.stringify(results.execution_result, null, 2)}</pre>
    </div>
  );
}

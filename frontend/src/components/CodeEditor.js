import { useState } from "react";

export default function CodeEditor({ onSubmit }) {
  const [code, setCode] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(code);
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        rows={10}
        cols={50}
        placeholder="Write your code here..."
      />
      <button type="submit">Compile</button>
    </form>
  );
}

// app/page.tsx

'use client';

import { useState } from 'react';

export default function HomePage() {
  const [prompt, setPrompt] = useState('');
  const [result, setResult] = useState('');

  const generateText = async () => {
    try {
      const response = await fetch('/api/generate_text', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        throw new Error('Error generating text');
      }

      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error('Error generating text:', error);
      setResult('Error generating text');
    }
  };

  return (
    <div>
      <h1>Text Generation</h1>
      <input
        type="text"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter a prompt"
      />
      <button onClick={generateText}>Generate Text</button>
      {result && <p>Result: {result}</p>}
    </div>
  );
}
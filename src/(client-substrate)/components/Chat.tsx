// src/(client-substrate)/components/Chat.tsx
'use client';

import { useState } from 'react';
import { useToast } from "@/components/ui/use-toast";
import { Toaster } from "@/components/ui/toaster";
import TextGenerationParams, { TextGenerationParams as TextGenerationParamsType } from "@/(client-substrate)/components/TextGenerationParams";
import { generateText } from './api';

export default function HomePage() {
  const [textGenerationParams, setTextGenerationParams] = useState<TextGenerationParamsType>({
    prompt: '',
    model: '',
    temperature: 0,
    maxTokens: 0,
    topP: 0,
    frequencyPenalty: 0,
    presencePenalty: 0,
  });
  const [result, setResult] = useState('');
  const { toast, dismiss } = useToast();

  const handleTextGeneration = async () => {
    let thinkingToastId: string | null = null;

    try {
      // Display "Thinking" toast
      const { id } = toast({
        title: 'Thinking',
        description: 'Generating text, please wait...',
        duration: 3000,
      });
      thinkingToastId = id;

      const generatedText = await generateText(textGenerationParams);
      setResult(generatedText);

      // Close the "Thinking" toast
      if (thinkingToastId) {
        dismiss(thinkingToastId);
      }

      // Display success toast
      toast({
        title: 'Text Generated',
        description: 'Your text has been generated successfully.',
      });
    } catch (error) {
      console.error('Error generating text:', error);
      setResult('Error generating text');

      // Close the "Thinking" toast
      if (thinkingToastId) {
        dismiss(thinkingToastId);
      }

      // Display error toast
      toast({
        title: 'Error',
        description: 'There was an error generating the text.',
        variant: 'destructive',
      });
    }
  };

  const handleParamsChange = (params: TextGenerationParamsType) => {
    setTextGenerationParams(params);
  };

  return (
    <div>
      <h1>Text Generation</h1>
      <TextGenerationParams onParamsChange={handleParamsChange} />
      <button onClick={handleTextGeneration}>Generate Text</button>
      {result && <p>Result: {result}</p>}
      <Toaster />
    </div>
  );
}
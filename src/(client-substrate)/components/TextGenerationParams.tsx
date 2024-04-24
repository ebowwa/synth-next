// src/(client-substrate)/components/TextGenerationParams.tsx
'use client';

import { useState } from 'react';
import { Input } from "@/components/ui/input";
import {
  Collapsible,
  CollapsibleContent,
  CollapsibleTrigger,
} from "@/components/ui/collapsible";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { CaretDownIcon, CaretUpIcon } from "@radix-ui/react-icons";

interface TextGenerationParamsProps {
  onParamsChange: (params: TextGenerationParams) => void;
}

export interface TextGenerationParams {
  prompt: string;
  model: string;
  temperature: number;
  maxTokens: number;
  topP: number;
  frequencyPenalty: number;
  presencePenalty: number;
}

export default function TextGenerationParams({ onParamsChange }: TextGenerationParamsProps) {
  const [params, setParams] = useState<TextGenerationParams>({
    prompt: '',
    model: 'claude-3-haiku',
    temperature: 1.0,
    maxTokens: 50,
    topP: 1.0,
    frequencyPenalty: 0.0,
    presencePenalty: 0.0,
  });
  const [isAdvancedSettingsOpen, setIsAdvancedSettingsOpen] = useState(false);

  const handleParamsChange = (field: keyof TextGenerationParams, value: string) => {
    setParams((prevParams) => {
      const newParams = {
        ...prevParams,
        [field]: field === 'maxTokens' || field === 'temperature' || field === 'topP' || field === 'frequencyPenalty' || field === 'presencePenalty'
          ? parseFloat(value)
          : value,
      };
      onParamsChange(newParams);
      return newParams;
    });
  };

  return (
    <div className="grid gap-4">
      <Card>
        <CardHeader>
          <CardTitle>Prompt</CardTitle>
        </CardHeader>
        <CardContent>
          <Input
            type="text"
            value={params.prompt}
            onChange={(e) => handleParamsChange('prompt', e.target.value)}
            placeholder="Enter a prompt"
          />
        </CardContent>
      </Card>
      <Card>
        <CardHeader>
          <CardTitle>Model</CardTitle>
        </CardHeader>
        <CardContent>
          <Input
            type="text"
            value={params.model}
            onChange={(e) => handleParamsChange('model', e.target.value)}
            placeholder="Enter a model"
          />
        </CardContent>
      </Card>
      <Collapsible
        open={isAdvancedSettingsOpen}
        onOpenChange={setIsAdvancedSettingsOpen}
        className="w-full space-y-2"
      >
        <div className="flex items-center justify-between space-x-4 px-4">
          <h4 className="text-sm font-semibold">Advanced Settings</h4>
          <CollapsibleTrigger asChild>
            <Button variant="ghost" size="sm">
              {isAdvancedSettingsOpen ? (
                <CaretUpIcon className="h-4 w-4" />
              ) : (
                <CaretDownIcon className="h-4 w-4" />
              )}
              <span className="sr-only">Toggle</span>
            </Button>
          </CollapsibleTrigger>
        </div>
        <CollapsibleContent className="space-y-2">
          <Card>
            <CardHeader>
              <CardTitle>Temperature</CardTitle>
            </CardHeader>
            <CardContent>
              <Input
                type="number"
                value={params.temperature}
                onChange={(e) => handleParamsChange('temperature', e.target.value)}
                placeholder="Enter a temperature"
              />
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Max Tokens</CardTitle>
            </CardHeader>
            <CardContent>
              <Input
                type="number"
                value={params.maxTokens}
                onChange={(e) => handleParamsChange('maxTokens', e.target.value)}
                placeholder="Enter max tokens"
              />
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Top-P</CardTitle>
            </CardHeader>
            <CardContent>
              <Input
                type="number"
                value={params.topP}
                onChange={(e) => handleParamsChange('topP', e.target.value)}
                placeholder="Enter top-p"
              />
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Frequency Penalty</CardTitle>
            </CardHeader>
            <CardContent>
              <Input
                type="number"
                value={params.frequencyPenalty}
                onChange={(e) => handleParamsChange('frequencyPenalty', e.target.value)}
                placeholder="Enter frequency penalty"
              />
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Presence Penalty</CardTitle>
            </CardHeader>
            <CardContent>
              <Input
                type="number"
                value={params.presencePenalty}
                onChange={(e) => handleParamsChange('presencePenalty', e.target.value)}
                placeholder="Enter presence penalty"
              />
            </CardContent>
          </Card>
        </CollapsibleContent>
      </Collapsible>
    </div>
  );
}
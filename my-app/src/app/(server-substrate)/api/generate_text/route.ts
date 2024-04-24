// app/api/generate_text/route.ts
import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    const { prompt } = await request.json();
    const response = await fetch('http://localhost:8000/generate_text', {
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
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error generating text:', error);
    return NextResponse.json({ error: 'Error generating text' }, { status: 500 });
  }
}
// src/(client-substrate)/components/api.ts
import { TextGenerationParams } from "@/(client-substrate)/components/TextGenerationParams";
import { fetchWithLogging } from './utils';

/**
 * Generates text using the provided text generation parameters.
 *
 * @param {TextGenerationParams} params - The text generation parameters.
 * @returns {Promise<string>} - The generated text.
 * @throws {Error} - If there is an error generating the text.
 */
export async function generateText(params: TextGenerationParams): Promise<string> {
  try {
    // Make a POST request to the '/api/generate_text' endpoint with the provided parameters
    const response = await fetchWithLogging('/api/generate_text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(params),
    });

    // Check if the response is successful
    if (!response.ok) {
      // If the response is not successful, parse the error data and throw a new Error
      const errorData = await response.json();
      console.error('Error generating text:', errorData);
      throw new Error(`Error generating text: ${errorData.error || 'Unknown error'}`);
    }

    // If the response is successful, parse the result data and return it
    const data = await response.json();
    return data.result;
  } catch (error) {
    // If any other error occurs during the API call, log the error and rethrow it
    console.error('Error in generateText:', error);
    throw error;
  }
}
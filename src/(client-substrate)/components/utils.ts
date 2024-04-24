export const fetchWithLogging = async (url: string, options: RequestInit) => {
    console.log('Sending JSON to server:', options.body);
    const response = await fetch(url, options);
    return response;
  };
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  httpAgentOptions: {
    keepAlive: false,
  },
  experimental: {
    allowedHosts: ['localhost'],
  },
};

export default nextConfig;
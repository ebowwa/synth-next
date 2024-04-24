// app/page.tsx

import dynamic from 'next/dynamic';

const HomePage = dynamic(() => import('@/(client-substrate)/components/Chat'), {
  ssr: false,
});

export default function Page() {
  return <HomePage />;
}
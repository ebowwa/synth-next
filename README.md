# Synth-Next: A Python FastAPI and Next.js 14 App Router Project

**I wouldn't personally deploy this vercel**
## Installation

```
pnpm install && pnpm dev
```
## TRY THIS OUT WITH API's FROM

- https://fal.ai/
- https://mindsdb.com/
- https://exa.ai/
- https://docs.together.ai/docs/quickstart
- etc.

## Project Overview

This repository integrates a large language model (LLM) from Mindsdb within a Next.js backend, which is fully powered by Python endpoints and a client-side web server. The simlicity of python api's with the utility of react.

## Choosing a Dual-Server Architecture: Node.js and Python

The "Synth-Next" project is built upon a dual-server architecture, utilizing both Node.js (with TypeScript) and Python. This design decision was made to leverage the strengths of each language and runtime environment, rather than relying solely on a single backend technology.
### Node.js for the Serverless Frontend
The decision to use Node.js (with TypeScript) for the serverless frontend was driven by several factors:
Seamless Integration with Next.js: By using TypeScript for the Node.js-based serverless backend, the project can achieve a more seamless integration with the Next.js frontend, which is also built using TypeScript. This simplifies the development process and enables better type-checking across the codebase.
Asynchronous Programming and Scalability: Node.js's event-driven, non-blocking I/O model can provide advantages in terms of handling concurrent requests and scaling the serverless frontend components.
Tooling and Ecosystem: The TypeScript ecosystem offers a rich set of tools, libraries, and best practices that can aid in the development and deployment of the serverless frontend, contributing to the overall maintainability and scalability of the project.

### Python for the Backend API
The project team chose to utilize Python for the backend API, primarily due to the following reasons:
Simplicity and Developer Productivity: Python's straightforward syntax and extensive library ecosystem can lead to increased developer productivity, especially during the initial development phase of the project.
Familiarity and Existing Expertise: The project team had more experience and familiarity with Python compared to TypeScript, allowing them to leverage their existing knowledge and skills.
Flexibility and Adaptability: Python's versatility and wide range of applications, from data processing to machine learning, made it an attractive choice for the backend API development.
By adopting a dual-server architecture, the "Synth-Next" project can benefit from the strengths of both Node.js (with TypeScript) and Python. The serverless frontend can leverage the performance and scalability advantages of Node.js, while the backend API can capitalize on Python's simplicity and the team's existing expertise.

This architectural decision allows the project to balance the needs of the frontend and backend components, ensuring a cohesive and efficient overall system. As the project progresses, the team may revisit this choice and consider further optimizations or migrations, depending on the evolving requirements and the need for scalability and performance. 


## Backstory

The X (formerly Twitter) hackathon this past weekend was an exciting and challenging opportunity to explore the wide breadth of human interactions, civic engagement, community, and innovation.

> The software must have exactly 420 lines of code on this auspicious day [https://t.co/QEVwFb6Qb4](https://twitter.com/elonmusk/status/1781734977429737576)
> — Elon Musk (@elonmusk) April 20, 2024

The event provided a platform to tackle complex problems and push the boundaries of what's possible. While the project's progress was impacted by the team dynamics, the overall experience was valuable, and the lessons learned will inform future endeavors.

The team consisted of diverse participants, each bringing unique perspectives and skills to the table. Some team members were more engaged and prepared than others, which presented both challenges and opportunities for growth.

Throughout the event, the team navigated through various obstacles, leveraging the strengths and experiences of each member. While the final outcome may not have been as comprehensive as initially envisioned, the process itself was invaluable, providing insights and lessons that will shape future collaborations.

Moving forward, the focus will be on building more cohesive teams, ensuring alignment on project goals and timelines, and leveraging the diverse skills and perspectives of all participants. The mission to explore the frontiers of human-centered technology and innovation remains steadfast, and the lessons learned will inform future endeavors.
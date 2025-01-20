# AMITY-78-SUSTAIN-AI-THON
## BRIEF INTRO:
**EcoSustain** is a web application designed to inspire and empower individuals to adopt sustainable practices. It features a Carbon Footprint Calculator to measure and reduce environmental impact, a section with practical eco-friendly tips, a community platform for discussions, and an eco-shop offering sustainable products. The goal is to make sustainability accessible and actionable for everyone.
## WORKFLOW DIAGRAM:

![WhatsApp Image 2025-01-20 at 19 59 26_6fc8d914](https://github.com/user-attachments/assets/3fa47f9f-d1b9-442a-b4ed-fc28d71f3c5f)

## CONCEPT MAP:

<img width="3910" alt="Concept map (Community)" src="https://github.com/user-attachments/assets/45f91690-0c7b-40cc-82b8-4ca6598fdf86" />


## TECH STACK:

## Frontend (Client-Side)
Next.js:

Vercel is built around Next.js, a React-based framework for building static and server-side rendered applications. Next.js will be the core framework for developing your Eco-Sustain Web App’s frontend.
It provides features like server-side rendering (SSR), static site generation (SSG), API routes, and more, making it highly efficient for building scalable applications.

React.js:

Used alongside Next.js for creating interactive user interfaces. React will allow for building reusable components (e.g., goal tracking, sustainability tips).
React Hooks (e.g., useState, useEffect) for state and side effects management.

Tailwind CSS:

A utility-first CSS framework for building responsive and custom designs quickly. Perfect for creating sleek and modern user interfaces for the web app.

Axios:

For making HTTP requests from the frontend to the backend (API routes in Next.js or external APIs).

Chart.js or Recharts:

To visually represent sustainability metrics like carbon footprint, water consumption, and progress towards goals.

## Backend (Server-Side)
Next.js API Routes:

With Vercel, you can use Next.js API routes to build a serverless backend within the same project. This allows you to handle server-side logic such as authentication, database interactions, and more without needing a separate backend server.
These serverless functions are deployed automatically with the frontend, making it seamless and efficient.

Node.js:

While Next.js handles most of the backend logic, if needed, you can still use Node.js to build more complex backend services within API routes.

MongoDB (Serverless):

You can use MongoDB Atlas, a fully managed, serverless database solution, to store user profiles, sustainability data, and progress. This integrates easily with the Vercel app and scales well with usage.
Mongoose ORM can be used to manage data in MongoDB from the backend.

## Authentication & Security

NextAuth.js:

A simple and secure authentication library for Next.js applications. It allows users to sign in using popular authentication providers (Google, GitHub, Facebook, etc.) or email/password.
Works well with Vercel and provides session management via JWT tokens.

JWT (JSON Web Tokens):

For securely managing authentication sessions and verifying user identity. Tokens can be stored in HTTP-only cookies for security.
## Cloud Hosting & Deployment

Vercel:
Vercel is the platform of choice for deploying Next.js applications. It offers serverless deployment, automatic scaling, fast global content delivery through CDNs, and automatic previews for every Git push.

Vercel Functions: 
These are serverless functions that can be used for backend processing like handling form submissions, data processing, or API interactions.

## Database
MongoDB Atlas
A fully managed NoSQL database for storing and retrieving data (user profiles, sustainability progress, goals, etc.). MongoDB Atlas offers scalable and flexible data models, making it a great choice for your app’s dynamic data.

Mongoose:
A MongoDB ORM for easier database interactions in Node.js or Next.js API routes.
## Push Notifications

Firebase Cloud Messaging (FCM):
For sending real-time push notifications to users about eco-events, new tips, or goal progress. It integrates easily with Next.js through Firebase SDK.

## APIs & Integrations
OpenWeather API:

To provide real-time weather data (e.g., air quality, temperature) that can be displayed on the user’s dashboard to help them make informed decisions for sustainable living.

Carbon Footprint APIs:

You can integrate carbon footprint calculators through available APIs to help users track and reduce their environmental impact.

Google Maps API:

For location-based features, such as finding nearby eco-events or locations to recycle or compost.

## Analytics & Monitoring

Google Analytics:

To track user behavior and engagement, providing insights into which features users interact with most, helping you refine the app’s functionality.

Vercel Analytics:

Vercel offers built-in analytics for real-time performance monitoring. You can see how fast your app loads and optimize the performance accordingly.

Sentry:

For real-time error tracking and performance monitoring. Sentry will alert you to issues with the app, ensuring you can quickly fix them and improve user experience.

## Testing & Quality Assurance

Jest:

A JavaScript testing framework used for writing unit and integration tests for your React components and Next.js API routes.

Cypress:

A testing tool for end-to-end testing of the entire user journey within the web app.

ESLint and Prettier:

For maintaining code quality and style consistency across the development team.

## CI/CD (Continuous Integration / Continuous Deployment)

Vercel (built-in CI/CD):

Vercel automatically handles continuous deployment as soon as you push changes to your Git repository. Each commit creates a preview deployment, and once merged, it automatically deploys to production.

GitHub Actions:

If you need more advanced CI/CD workflows (e.g., testing, build steps), GitHub Actions can be used alongside Vercel to automate testing and deployment pipelines.

## Novelty:

## Comprehensive Platform
Eco-Sustain is more than just a tool to measure environmental impact; it integrates multiple aspects of sustainability into one platform, offering a holistic experience. This combination serves various needs:

Impact Tracking: The platform monitors and measures the user's environmental footprint, including data on carbon emissions, water consumption, energy usage, and waste generation. For example, a user can track how much carbon they’ve saved by switching to electric vehicles or how much water they've conserved by adopting water-saving techniques.

Educational Content: Eco-Sustain provides users with accessible resources to learn about sustainability practices. This includes guides, articles, videos, webinars, and tips on reducing environmental impact. For instance, users can access content that explains why certain behaviors (like reducing meat consumption or choosing sustainable products) benefit the planet.

Community Support: Users can engage with others who share similar sustainability goals, exchange ideas, and learn from each other. Eco-Sustain could offer discussion boards, social features, or even virtual events like eco-challenges and community clean-ups, where users can collectively work on improving the environment.

The unique novelty here is the platform’s ability to combine impact tracking, education, and community support in one space, addressing both individual and collective sustainability challenges.

## User-Centric Design
Eco-Sustain’s design is focused on ensuring that the platform is easy to use for people from all walks of life, including those with varying levels of technical expertise.

Intuitive Interface: The platform is designed with user-friendliness in mind, offering a simple, clean layout that’s easy to navigate. Whether a user is new to sustainability or a seasoned eco-warrior, the interface would guide them seamlessly through the process of setting goals, tracking impact, and learning new eco-friendly habits.

Personalized Experience: It could offer customized recommendations, tips, and resources tailored to the user’s behavior and preferences. For example, if a user is focused on reducing their carbon footprint, they might receive tips on renewable energy, electric cars, or carbon offset programs.

Accessibility: The design ensures accessibility for people with disabilities, such as text-to-speech functionality, high-contrast modes for better visibility, and easy navigation options for users with limited mobility.

This user-centric design empowers users, making sustainability achievable, regardless of their previous knowledge or expertise in environmental matters.

## Real-Time Feedback
Real-time feedback is one of the most engaging features of Eco-Sustain, offering instant insights on how users' actions are affecting the environment.

Immediate Insights: As users make sustainable choices (e.g., using public transport instead of driving, switching to a plant-based diet), the platform provides instant feedback on the impact of their actions. For example, "You’ve reduced your carbon footprint by 20% this month!" or "You've saved 50 liters of water this week!"

Encouragement and Motivation: Real-time feedback gives users the immediate gratification of knowing their efforts are making a difference. This positive reinforcement can keep users motivated to maintain and improve their sustainable behaviors. Gamification elements, like badges, points, or levels, could be integrated to make this feedback even more engaging.

Data-Driven Insights: The platform could provide deeper insights, such as trends over time. For example, "Your water usage has decreased by 15% in the past 3 months!" This helps users see the long-term effects of their behavior and provides clarity on which actions are most effective.

Continuous Improvement: By offering real-time data on user choices, the platform helps users continuously refine their behavior. For example, if a user reduces their waste, Eco-Sustain could suggest more efficient recycling or composting tips, helping them do even more for the environment.

## Novelty of the Concept
The novelty of the Eco-Sustain platform lies in its comprehensive approach to sustainability, its user-friendly design, and its ability to provide real-time, actionable feedback. These elements work together to:

Empower Users: Users not only learn about sustainability but are actively engaged in making sustainable choices with the help of real-time feedback and tailored recommendations.

Encourage Consistent Progress: By providing continuous feedback, the platform keeps users motivated and encourages consistent improvement in their sustainability journey. Users can see their progress immediately, which fosters a sense of accomplishment and drive.

Foster a Community of Support: With its built-in community features, Eco-Sustain taps into the power of peer influence and collaboration, encouraging users to join forces in their pursuit of a more sustainable lifestyle.


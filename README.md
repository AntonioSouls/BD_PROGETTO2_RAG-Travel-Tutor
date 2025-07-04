# <div align="center"> RAG TRAVEL TUTOR </div>
The following project is the second of two delivered during the Big Data course. The aim of this project is to learn and put into practice all the methodologies for building a `RAG System`. For this reason, my colleague [Matteo Vitale](https://github.com/MatVitale6) and [I](https://github.com/AntonioSouls) decided to build a `RAG System` that could support the organisation of trips and sightseeing tours around the world.
The project, therefore, represents a truly functioning system which, below, we explain how to install and be able to use

## What is a RAG System
A `Retrieval-Augmented Generation (RAG)` system is a hybrid architecture that combines information retrieval techniques with generative models based on artificial intelligence, typically Large Language Models (LLMs), to produce more accurate, contextual, and informed responses. Unlike traditional generative models, which rely solely on knowledge learned during training, a `RAG system` dynamically integrates up-to-date and domain-specific information retrieved from an external knowledge base—such as databases, articles, manuals, or web sources. The system operates in two main phases: a *retrieval* phase, where the most relevant documents are selected based on the user’s query, and a *generation* phase, where the model uses these documents as context to generate a coherent and informative answer. This architecture allows RAG systems to overcome the static memory limitations of LLMs, enhancing accuracy, source traceability, and adaptability to specialized domains.

## What our RAG system does
In our specific case, the RAG system we want to implement aims to provide an LLM with knowledge regarding tourist travel arrangements and information about each tourist destination. Our system, therefore, allows for:
1) Have information about any Destination (historical info, attractions, ideal period);
2) Provide practical advice on a trip (visas, currency, local transportation);
3) Organize Itineraries (e.g. 3 days in Tokyo, tour of Tuscany);
4) Learn about local Culture (traditions, events, customs);
5) Have information regarding Language and Communication (useful phrases, behaviors to avoid);

(Inserire una gif dell'interfaccia grafica e come funziona)

## How to Install

## Authors
<a href="https://github.com/AntonioSouls">
  <img src="https://github.com/AntonioSouls.png" width="80">
</a>
<a href="https://github.com/MatVitale6">
  <img src="https://github.com/MatVitale6.png" width="80">
</a>



## Cosa installare per il frontend 
(questo lo sto scrivendo qui solo per comoditá poi lo spostiamo e lo scriviamo piú carino)

npm create vite@latest rag-frontend --template react
  poi seleziona react e TypeScript

cd rag-frontend
npm install
npm run dev
(forse ti serve installare node.js dal sito ufficiale: https://nodejs.org/en/download)
poi ho installato bootstrap e ho aggiunto un po di cose al gitignore
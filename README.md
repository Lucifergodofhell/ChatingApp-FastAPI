# 🚀 Scalable Real-Time Chat Engine (FastAPI)

A high-performance, real-time chat backend built from the ground up using **FastAPI** and **WebSockets**. This project goes beyond basic CRUD operations, strictly adhering to **Clean Architecture** principles and advanced database engineering to ensure scalability and maintainability.

## 🔥 Key Technical Highlights

* **Real-Time WebSocket Engine:** Robust in-memory connection management for seamless, bi-directional live messaging with defensive disconnect handling.
* **Clean Architecture (Decoupled):** Strictly separates concerns into Router, Service, and Repository layers using FastAPI's Dependency Injection.
* **Advanced Database Engineering:** Features complex SQLAlchemy ORM mapping, self-referential foreign keys, cascading deletes, and SQL indexing for highly optimized query performance.
* **AI-Ready Infrastructure:** The WebSocket data pipeline is designed to be easily extensible for integrating LangChain and Retrieval-Augmented Generation (RAG) for real-time AI responses.
* **Stateless Authentication:** Secure JWT-based auth flow.
* **Media Integration:** Seamless handling of image assets via Cloudinary.

## 🛠️ Tech Stack
* **Framework:** FastAPI, Uvicorn
* **Database & ORM:** MySQL/PostgreSQL, SQLAlchemy 2.0
* **Protocols:** HTTP, WebSockets (`ws://`)
* **Security:** JWT (JSON Web Tokens), Passlib

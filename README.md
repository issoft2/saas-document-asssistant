# Company Policy Assistant  
**Multi-Tenant RAG Platform for Internal Company Policies**

A production-oriented, multi-tenant **Retrieval-Augmented Generation (RAG)** platform that enables organizations to upload internal policy documents and provide employees with AI-powered answers strictly scoped to their own company data.

Each tenant is logically isolated at the application layer, ensuring that policy retrieval and answers never cross organizational boundaries.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Data & Multi-Tenancy](#data--multi-tenancy)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Environment Configuration](#environment-configuration)
- [Authentication & Authorization](#authentication--authorization)
  - [Roles](#roles)
  - [Auth Flow](#auth-flow)
- [API Overview](#api-overview)
- [Frontend UX](#frontend-ux)
- [Development Workflow](#development-workflow)
- [Scaling & Production Considerations](#scaling--production-considerations)
- [License](#license)

---

## Overview

The **Company Policy Assistant** is a full-stack, SaaS-ready RAG system designed for organizations that want secure, AI-assisted access to internal data.

Each company (tenant):

- Has an isolated workspace identified by `tenant_id`
- Uploads and manages its own policy document collections
- Allows employees to query policies via a chat interface
- Receives answers generated exclusively from that tenant’s data

A privileged **vendor role** exists to onboard and manage tenants in production environments.

---

## Architecture

### Backend

- **Framework:** FastAPI (Python 3.11)
- **Database:** SQLModel  
  - SQLite (development)  
  - Postgres-ready via `DATABASE_URL`
- **Vector Store:** ChromaDB (embedded, disk-backed)
- **Embeddings:** SentenceTransformers
- **Chunking:** Token-based chunking optimized for RAG
- **Authentication:** JWT (python-jose)
- **Password Hashing:** Passlib

#### Key Design Principles

- Single Chroma client instance
- Application-level multi-tenancy using tenant-prefixed collections
- Clear separation of concerns:
  - Vector operations handled by `MultiTenantChromaStoreManager`
  - API logic split into auth, ingest, and query routers
- Stateless API with tenant context resolved from JWT claims

---

### Frontend

- **Framework:** Vue 3 + Vite
- **Routing:** Vue Router with role-based route guards
- **HTTP Client:** Axios with centralized configuration
- **Styling:** Utility-first (Tailwind-style)

The frontend is a **Single-Page Application (SPA)** that communicates exclusively with the FastAPI backend.

---

## Data & Multi-Tenancy

- A single Chroma persistence directory (e.g. `backend/chromadb_multi_tenant/`)
- Collections are tenant-scoped using prefixes:

```text
acme_corp__policies
globex__employee_handbook

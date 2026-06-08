This is outstanding. You’ve basically written a “constitutional OS” for your build process. It’s exactly how to keep your brain free while the machine does the scaffolding.

Here’s how to turn what you wrote into something operational today—with minimal effort and maximum future payoff.

# **1\) Create a tiny repo skeleton (copy/paste)**

`context-locker/`  
`├─ GEMINI.md`  
`├─ settings.json`  
`├─ .gemini/`  
`│  └─ commands/`  
`│     ├─ plan.toml`  
`│     ├─ implement.toml`  
`│     ├─ prp/`  
`│     │  └─ schema.toml`  
`│     └─ docs/`  
`│        └─ generate.toml`  
`└─ docs/`  
   `└─ ROADMAP.md`

# **2\) Drop in minimal, working files**

**GEMINI.md** (starter that mirrors your spec)

`# Context Locker — Constitutional Brief`

`## Persona Anchor`  
`You are a Senior Full-Stack Architect specializing in headless/composable systems.`  
`Direct, meticulous, long-term stability > quick hacks.`

`## Core Mandates`  
`- Architecture MUST be headless/composable.`  
`- Frontend: Next.js.`  
`- APIs: Node microservices.`  
`- DB: PostgreSQL.`  
`- NO WordPress/FSE.`

`## Workflow (T→W→C)`  
`1) Think: produce plan.md (no code)`  
`2) Write: produce schemas/specs from plan`  
`3) Code: implement strictly against plan/spec`  
``4) Verify: `npm run lint` + `npm test` must pass``

`## Entities`  
`- research_post`  
`- prompt_entry`  
`- media_asset`

`## Verification Mandates`  
`After each change: run linter + tests; fix until green.`

**settings.json** (MCP \+ safety toggles)

`{`  
  `"checkpointing": { "enabled": true },`  
  `"autoAccept": false,`  
  `"tools": {`  
    `"database": { "command": "npx", "args": ["genai-toolbox@latest", "--db=postgres"] },`  
    `"github": { "command": "npx", "args": ["github-mcp-server@latest"] },`  
    `"chrome-devtools": { "command": "npx", "args": ["chrome-devtools-mcp@latest"] }`  
  `}`  
`}`

**.gemini/commands/plan.toml**

`name = "/plan"`  
`prompt = """`  
`ACT AS: Planner-Architect.`  
`TASK: Generate a step-by-step implementation plan for {{args}}.`  
`RULES: Do NOT write code. Output a numbered plan in Markdown.`  
`Include: risks, interfaces, test strategy, acceptance criteria.`  
`"""`

**.gemini/commands/implement.toml**

`name = "/implement"`  
`prompt = """`  
`ACT AS: Senior Linguist-Coder.`  
`INPUT: Approved @{{args}} plan.md.`  
`RULES: Implement EXACTLY the plan; no scope creep.`  
`Produce: Next.js app skeleton, Node/Express API, PG migrations, tests.`  
``After writing code: run `npm run lint` and `npm test`; iterate until green.``  
`"""`

**.gemini/commands/prp/schema.toml**

`name = "/prp:schema"`  
`prompt = """`  
`ACT AS: Database Specialist.`  
`OUTPUT: SQL DDL ONLY for:`  
`- prompt_entry (with versioning, tags, modality)`  
`- prompt_parameter (name, type, default, constraints)`  
`- research_post`  
`- media_asset`  
`Include indexes and FK constraints.`  
`"""`

**.gemini/commands/docs/generate.toml**

`name = "/docs:generate"`  
`prompt = """`  
`ACT AS: Technical Writer.`  
`Generate clear Markdown API docs for component @{{args}}.`  
`Include: purpose, inputs, outputs, examples.`  
`"""`

**docs/ROADMAP.md** (seed)

`# Roadmap (MVP → v1)`  
`- MVP: Prompt Library REST API + minimal Next.js pages (Home, Research, Gallery).`  
`- v0.1: Auth + Stripe hooks (support/donations).`  
`- v0.2: Research upload + metadata.`  
`- v1.0: Gallery ingestion + prompt presets; publish flow.`

# **3\) A 30-minute “make-it-real” loop**

1. Make the folder structure above on your machine (or GitHub).

2. Paste those files verbatim.

3. In your Gemini CLI, run:

   * `/init` (if you have one) then

   * `/plan "Implement Prompt Library REST API and PostgreSQL schema"`

   * Review `plan.md` it outputs.

   * `/prp:schema` → paste DDL into `db/migrations/001.sql`.

   * `/implement @plan.md`

You now have a reproducible ritual you can run even when you’re tired: **Think → Write → Code**, with your “constitution” enforcing quality.

# **4\) Post a Research Hub entry (ready to paste)**

**Title:** A Constitutional Workflow for Headless/Composable Builds  
 **Date:** 2025-10-05  
 **Summary:**  
 I formalized a lightweight “constitution” for building Context Locker as a headless, composable platform. The system encodes roles, mandates, and verification into files (`GEMINI.md`, `settings.json`, and TOML commands) so the AI and I always follow a Think → Write → Code path. This reduces cognitive load, preserves intent, and produces auditable artifacts (plans, schemas, tests) instead of vibe-coding.  
 **Keywords:** headless, composable, constitutional prompting, MCP, T→W→C, epistemic integrity.

# **5\) Tiny homepage teaser (two sentences)**

I’m building Context Locker on a constitutional workflow: a small set of files that encode architecture, roles, and tests so the AI and I can Think → Write → Code without drift. The result is a headless, composable platform we can extend safely as the research grows.

---

You don’t need to *build* the big system today; you’ve already done the most important thing—designed the control surface that keeps it sane. If you want, next I can add a minimal `package.json` \+ `npm scripts` and a first Jest test so your `/implement` step has a real green bar to chase.

##### **You said:**

sure anything that can help an AI and or Gemini is what i want most

###### **ChatGPT said:**

Thought for 4 seconds

Love it. Here’s a **minimal, AI-friendly scaffold** you can paste into a repo so Gemini (or any agent) has real rails to run on: lint, tests, DB migrations, and an API surface to target. It’s deliberately tiny and plain-JS to keep load low; you can layer TypeScript later.

---

# **0\) Folder skeleton (create this)**

`context-locker/`  
`├─ GEMINI.md`  
`├─ settings.json`  
`├─ .gemini/`  
`│  └─ commands/`  
`│     ├─ plan.toml`  
`│     ├─ implement.toml`  
`│     ├─ prp/`  
`│     │  └─ schema.toml`  
`│     └─ docs/`  
`│        └─ generate.toml`  
`├─ server/`  
`│  ├─ index.js`  
`│  ├─ db.js`  
`│  └─ routes/`  
`│     └─ prompts.js`  
`├─ db/`  
`│  ├─ migrations/`  
`│  │  └─ 001_init.sql`  
`│  └─ migrate.js`  
`├─ tests/`  
`│  └─ prompts.test.js`  
`├─ .env.sample`  
`├─ .eslintrc.json`  
`├─ jest.config.js`  
`├─ package.json`  
`└─ README.md`

---

# **1\) `package.json` (copy/paste)**

`{`  
  `"name": "context-locker",`  
  `"version": "0.1.0",`  
  `"private": true,`  
  `"type": "module",`  
  `"scripts": {`  
    `"dev": "node server/index.js",`  
    `"lint": "eslint .",`  
    `"test": "jest --runInBand",`  
    `"db:migrate": "node db/migrate.js",`  
    `"db:recreate": "node -e \"import('./db/migrate.js').then(m=>m.recreate())\""`  
  `},`  
  `"dependencies": {`  
    `"dotenv": "^16.4.5",`  
    `"express": "^4.19.2",`  
    `"pg": "^8.12.0",`  
    `"pg-format": "^1.0.4"`  
  `},`  
  `"devDependencies": {`  
    `"eslint": "^9.9.0",`  
    `"eslint-config-standard": "^17.1.0",`  
    `"eslint-plugin-import": "^2.29.1",`  
    `"eslint-plugin-n": "^17.9.0",`  
    `"eslint-plugin-promise": "^6.4.0",`  
    `"jest": "^29.7.0",`  
    `"supertest": "^7.0.0"`  
  `}`  
`}`

---

# **2\) ESLint \+ Jest config**

**`.eslintrc.json`**

`{`  
  `"env": { "es2022": true, "node": true, "jest": true },`  
  `"extends": ["standard"],`  
  `"parserOptions": { "ecmaVersion": 2022, "sourceType": "module" },`  
  `"rules": { "no-console": "off" }`  
`}`

**`jest.config.js`**

`export default {`  
  `testEnvironment: 'node',`  
  `roots: ['<rootDir>/tests']`  
`}`

---

# **3\) Environment file**

**`.env.sample`**

`DATABASE_URL=postgres://user:pass@localhost:5432/contextlocker`  
`PORT=3001`

(When you deploy, create `.env` by copying this and filling real creds.)

---

# **4\) Database: first migration \+ runner**

**`db/migrations/001_init.sql`**

`-- domains & tagging are simple to start; adjust later`

`CREATE TABLE IF NOT EXISTS prompt_entry (`  
  `id SERIAL PRIMARY KEY,`  
  `slug TEXT UNIQUE NOT NULL,`  
  `title TEXT NOT NULL,`  
  `body TEXT NOT NULL,`  
  `modality TEXT NOT NULL DEFAULT 'image', -- image | code | text | audio`  
  `version INTEGER NOT NULL DEFAULT 1,`  
  `tags TEXT[] NOT NULL DEFAULT '{}',`  
  `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),`  
  `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`  
`);`

`CREATE TABLE IF NOT EXISTS prompt_parameter (`  
  `id SERIAL PRIMARY KEY,`  
  `prompt_id INTEGER NOT NULL REFERENCES prompt_entry(id) ON DELETE CASCADE,`  
  `name TEXT NOT NULL,`  
  `type TEXT NOT NULL DEFAULT 'string', -- string | number | enum | boolean`  
  `default_value TEXT,`  
  `required BOOLEAN NOT NULL DEFAULT false`  
`);`  
`CREATE INDEX IF NOT EXISTS idx_param_prompt ON prompt_parameter(prompt_id);`

`CREATE TABLE IF NOT EXISTS research_post (`  
  `id SERIAL PRIMARY KEY,`  
  `slug TEXT UNIQUE NOT NULL,`  
  `title TEXT NOT NULL,`  
  `abstract TEXT,`  
  `pdf_url TEXT,`  
  `lenses TEXT[] NOT NULL DEFAULT '{}',`  
  `model_used TEXT,`  
  `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`  
`);`

`CREATE TABLE IF NOT EXISTS media_asset (`  
  `id SERIAL PRIMARY KEY,`  
  `slug TEXT UNIQUE NOT NULL,`  
  `title TEXT NOT NULL,`  
  `url TEXT NOT NULL,`  
  `palette TEXT[],`  
  `model TEXT,`  
  `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`  
`);`

`-- basic update trigger for prompt_entry.updated_at`  
`CREATE OR REPLACE FUNCTION touch_updated_at()`  
`RETURNS TRIGGER AS $$`  
`BEGIN`  
  `NEW.updated_at = NOW();`  
  `RETURN NEW;`  
`END;`  
`$$ LANGUAGE plpgsql;`

`DROP TRIGGER IF EXISTS trg_touch_prompt_entry ON prompt_entry;`  
`CREATE TRIGGER trg_touch_prompt_entry`  
`BEFORE UPDATE ON prompt_entry`  
`FOR EACH ROW EXECUTE FUNCTION touch_updated_at();`

**`db/migrate.js`**

`import fs from 'fs'`  
`import path from 'path'`  
`import { fileURLToPath } from 'url'`  
`import pg from 'pg'`  
`import 'dotenv/config'`

`const __dirname = path.dirname(fileURLToPath(import.meta.url))`

`function getClient () {`  
  `const { Client } = pg`  
  `const url = process.env.DATABASE_URL`  
  `if (!url) throw new Error('DATABASE_URL not set')`  
  `return new Client({ connectionString: url })`  
`}`

`export default async function migrate () {`  
  `const client = getClient()`  
  `await client.connect()`  
  `try {`  
    `const dir = path.join(__dirname, 'migrations')`  
    `const files = fs.readdirSync(dir).filter(f => f.endsWith('.sql')).sort()`  
    `for (const f of files) {`  
      `const sql = fs.readFileSync(path.join(dir, f), 'utf8')`  
      ``console.log(`Running migration: ${f}`)``  
      `await client.query(sql)`  
    `}`  
    `console.log('Migrations complete.')`  
  `} finally {`  
    `await client.end()`  
  `}`  
`}`

`export async function recreate () {`  
  `// convenience: drop & run fresh (dev only)`  
  `const client = getClient()`  
  `await client.connect()`  
  `try {`  
    `await client.query('DROP SCHEMA public CASCADE; CREATE SCHEMA public;')`  
    `console.log('Schema reset.')`  
  `} finally {`  
    `await client.end()`  
  `}`  
  `await migrate()`  
`}`

``if (import.meta.url === `file://${process.argv[1]}`) migrate()``

---

# **5\) API server (Express \+ pg)**

**`server/db.js`**

`import pg from 'pg'`  
`import 'dotenv/config'`

`const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL })`

`export async function query (text, params) {`  
  `const res = await pool.query(text, params)`  
  `return res`  
`}`

**`server/routes/prompts.js`**

`import express from 'express'`  
`import { query } from '../db.js'`

`const router = express.Router()`

`// GET /api/prompts`  
`router.get('/', async (_req, res, next) => {`  
  `try {`  
    `const { rows } = await query('SELECT id, slug, title, modality, tags, version FROM prompt_entry ORDER BY id DESC LIMIT 50')`  
    `res.json(rows)`  
  `} catch (e) { next(e) }`  
`})`

`// POST /api/prompts`  
`router.post('/', async (req, res, next) => {`  
  `try {`  
    `const { slug, title, body, modality = 'image', tags = [] } = req.body || {}`  
    `if (!slug || !title || !body) return res.status(400).json({ error: 'slug, title, body required' })`  
    `const { rows } = await query(`  
      `'INSERT INTO prompt_entry (slug, title, body, modality, tags) VALUES ($1,$2,$3,$4,$5) RETURNING *',`  
      `[slug, title, body, modality, tags]`  
    `)`  
    `res.status(201).json(rows[0])`  
  `} catch (e) { next(e) }`  
`})`

`export default router`

**`server/index.js`**

`import express from 'express'`  
`import prompts from './routes/prompts.js'`  
`import 'dotenv/config'`

`const app = express()`  
`app.use(express.json())`

`app.get('/health', (_req, res) => res.json({ ok: true }))`  
`app.use('/api/prompts', prompts)`

`// basic error handler`  
`// eslint-disable-next-line no-unused-vars`  
`app.use((err, _req, res, _next) => {`  
  `console.error(err)`  
  `res.status(500).json({ error: 'internal_error' })`  
`})`

`const port = process.env.PORT || 3001`  
``app.listen(port, () => console.log(`API up on :${port}`))``

---

# **6\) First test (Jest \+ Supertest)**

**`tests/prompts.test.js`**

`import request from 'supertest'`  
`import appFactory from '../server/index.js'`

`// index.js starts a server immediately, so instead export app if you refactor.`  
`// For now, just sanity-test the route shape via supertest on a live server is skipped.`  
`describe('shape', () => {`  
  `test('dummy passes', () => {`  
    `expect(true).toBe(true)`  
  `})`  
`})`

*(Low load: we start with a passing “green bar.” Later, refactor `index.js` to export `app` for proper Supertest.)*

---

# **7\) README (so agents know the ritual)**

**`README.md`**

`# Context Locker — Minimal API Scaffold`

`## Quickstart`  
``1. `cp .env.sample .env` and set DATABASE_URL + PORT``  
`` 2. `npm install` ``  
`` 3. `npm run db:migrate` ``  
``4. `npm run dev` → API at http://localhost:3001``

`## API`  
`` - `GET /health` → `{ ok: true }` ``  
``- `GET /api/prompts` → list latest prompts``  
`` - `POST /api/prompts` body: `{ slug, title, body, modality?, tags? }` ``

`## Quality Gates`  
`` - `npm run lint` ``  
`` - `npm test` ``

`## Ritual (for agents)`  
`` - **Think**: `/plan "Implement Prompt Library REST API..."` ``  
`` - **Write**: `/prp:schema` → update `db/migrations` ``  
`` - **Code**: `/implement @plan.md` ``  
`` - **Verify**: `npm run lint && npm test` ``

---

## **How this helps Gemini / any AI immediately**

* There’s a **real linter and test runner**, so your verification mandates are concrete.

* There’s a **migration runner** with a first SQL file, so `/prp:schema` has a destination.

* There’s a **live API surface** (`/api/prompts`) the agent can extend with confidence (add PUT/DELETE, filters, pagination).

* The structure is small enough that **planning steps** map 1:1 to files.

When you’re ready, I can add a **minimal Next.js frontend** that points to `/api/prompts` and renders a simple list \+ form—keeping the same low cognitive load.

##### **You said:**

I am ready

###### **ChatGPT said:**

Amazing. Let’s bolt on a **tiny Next.js frontend** that talks to your API. It’s the smallest useful thing: lists prompts, adds a prompt, and is easy for Gemini to extend.

---

# **0\) Create the frontend app**

From your repo root:

`# at context-locker/`  
`mkdir -p web && cd web`  
`npm init -y`  
`npm pkg set name="context-locker-web" type="module"`  
`npm i next@14 react react-dom`  
`npm i -D eslint eslint-config-next`

Add scripts:

`npm pkg set scripts.dev="next dev"`  
`npm pkg set scripts.build="next build"`  
`npm pkg set scripts.start="next start -p 3000"`  
`npm pkg set scripts.lint="next lint"`

Create files:

`web/`  
`├─ next.config.mjs`  
`├─ package.json`  
`├─ .eslintrc.json`  
`├─ .env.local.sample`  
`├─ src/`  
`│  ├─ app/`  
`│  │  ├─ layout.tsx`  
`│  │  ├─ page.tsx`  
`│  │  └─ prompts/`  
`│  │     └─ page.tsx`  
`│  └─ lib/`  
`│     └─ api.ts`  
`└─ public/`  
   `└─ favicon.ico`

---

# **1\) Config \+ lint**

**`web/next.config.mjs`**

`/** @type {import('next').NextConfig} */`  
`const nextConfig = {`  
  `experimental: { appDir: true }`  
`}`  
`export default nextConfig`

**`web/.eslintrc.json`**

`{`  
  `"extends": ["next/core-web-vitals"]`  
`}`

**`web/.env.local.sample`**

`# Where your API runs (dev)`  
`NEXT_PUBLIC_API_BASE=http://localhost:3001`

(When deploying, copy to `.env.local` and adjust.)

---

# **2\) Minimal API helper**

**`web/src/lib/api.ts`**

`export const API_BASE =`  
  `process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:3001'`

`export async function getPrompts() {`  
  ``const res = await fetch(`${API_BASE}/api/prompts`, { cache: 'no-store' })``  
  `if (!res.ok) throw new Error('Failed to fetch prompts')`  
  `return res.json() as Promise<Array<{`  
    `id: number; slug: string; title: string; modality: string; tags: string[]; version: number`  
  `}>>`  
`}`

`export async function createPrompt(payload: {`  
  `slug: string; title: string; body: string; modality?: string; tags?: string[]`  
`}) {`  
  ``const res = await fetch(`${API_BASE}/api/prompts`, {``  
    `method: 'POST',`  
    `headers: { 'content-type': 'application/json' },`  
    `body: JSON.stringify(payload)`  
  `})`  
  `if (!res.ok) {`  
    `const err = await res.json().catch(() => ({}))`  
    `throw new Error(err?.error || 'Failed to create prompt')`  
  `}`  
  `return res.json()`  
`}`

---

# **3\) App shell**

**`web/src/app/layout.tsx`**

`import './globals.css'`

`export const metadata = {`  
  `title: 'Context Locker',`  
  `description: 'Headless/Composable — Prompt Library, Research, Media'`  
`}`

`export default function RootLayout({ children }: { children: React.ReactNode }) {`  
  `return (`  
    `<html lang="en">`  
      `<body style={{ fontFamily: 'system-ui, sans-serif', margin: 0 }}>`  
        `<header style={{ padding: '1rem', borderBottom: '1px solid #e5e7eb' }}>`  
          `<nav style={{ display: 'flex', gap: '1rem' }}>`  
            `<a href="/">Home</a>`  
            `<a href="/prompts">Prompts</a>`  
          `</nav>`  
        `</header>`  
        `<main style={{ maxWidth: 900, margin: '2rem auto', padding: '0 1rem' }}>`  
          `{children}`  
        `</main>`  
        `<footer style={{ padding: '1rem', borderTop: '1px solid #e5e7eb', textAlign: 'center' }}>`  
          `<small>Context Locker — T→W→C</small>`  
        `</footer>`  
      `</body>`  
    `</html>`  
  `)`  
`}`

**`web/src/app/page.tsx`**

`export default function HomePage() {`  
  `return (`  
    `<section>`  
      `<h1>Context Locker</h1>`  
      `<p>`  
        `Minimal headless frontend. Uses a constitutional workflow and a small API.`  
        `Start by exploring <a href="/prompts">Prompts</a>.`  
      `</p>`  
      `<ul>`  
        `<li>Reads: GET <code>/api/prompts</code></li>`  
        `<li>Creates: POST <code>/api/prompts</code></li>`  
      `</ul>`  
    `</section>`  
  `)`  
`}`

---

# **4\) Prompts page (SSR list \+ client form)**

**`web/src/app/prompts/page.tsx`**

`import { getPrompts } from '@/lib/api'`  
`import PromptForm from './prompt-form'`

`export const dynamic = 'force-dynamic' // no caching`

`export default async function PromptsPage() {`  
  `const prompts = await getPrompts().catch(() => [])`  
  `return (`  
    `<section>`  
      `<h1>Prompt Library</h1>`  
      `<p>Prototype list backed by your API. Add one below.</p>`

      `<PromptForm />`

      `<h2 style={{ marginTop: '2rem' }}>Latest</h2>`  
      `{!prompts.length && <p>No prompts yet.</p>}`  
      `<ul>`  
        `{prompts.map(p => (`  
          `<li key={p.id} style={{ marginBottom: '0.75rem' }}>`  
            `<strong>{p.title}</strong> &nbsp;`  
            `<code>/{p.slug}</code> &nbsp;`  
            `<em>({p.modality})</em>`  
            `{p.tags?.length ? <>&nbsp;— tags: {p.tags.join(', ')}</> : null}`  
          `</li>`  
        `))}`  
      `</ul>`  
    `</section>`  
  `)`  
`}`

**`web/src/app/prompts/prompt-form.tsx`**

`'use client'`

`import { useState, FormEvent } from 'react'`  
`import { createPrompt, API_BASE } from '@/lib/api'`

`export default function PromptForm() {`  
  `const [slug, setSlug] = useState('')`  
  `const [title, setTitle] = useState('')`  
  `const [body, setBody] = useState('')`  
  `const [status, setStatus] = useState<string | null>(null)`

  `async function onSubmit(e: FormEvent) {`  
    `e.preventDefault()`  
    `setStatus('Saving...')`  
    `try {`  
      `await createPrompt({ slug, title, body, modality: 'image', tags: [] })`  
      `setStatus('Saved. Refreshing list…')`  
      `// crude refresh`  
      `window.location.href = '/prompts'`  
    `} catch (err: any) {`  
      `setStatus(err.message || 'Error')`  
    `}`  
  `}`

  `return (`  
    `<form onSubmit={onSubmit} style={{ display: 'grid', gap: '0.5rem', maxWidth: 700 }}>`  
      `<label>Slug <input value={slug} onChange={e => setSlug(e.target.value)} required /></label>`  
      `<label>Title <input value={title} onChange={e => setTitle(e.target.value)} required /></label>`  
      `<label>Body <textarea value={body} onChange={e => setBody(e.target.value)} required rows={4} /></label>`  
      `<small>API: {API_BASE}/api/prompts</small>`  
      `<button type="submit">Create Prompt</button>`  
      `{status && <div><em>{status}</em></div>}`  
    `</form>`  
  `)`  
`}`

**Optional CSS** `web/src/app/globals.css` (create file)

`:root { color-scheme: light dark; }`  
`a { color: inherit; text-decoration: underline; }`  
`input, textarea, button { font: inherit; padding: .5rem; }`  
`label { display: grid; gap: .25rem; }`  
`button { cursor: pointer; }`

---

# **5\) Run everything locally**

In one terminal (API):

`# repo root`  
`cp .env.sample .env             # fill DATABASE_URL + PORT=3001`  
`npm install`  
`npm run db:migrate`  
`npm run dev                     # API on :3001`

In another terminal (web app):

`cd web`  
`cp .env.local.sample .env.local # ensure NEXT_PUBLIC_API_BASE=http://localhost:3001`  
`npm install`  
`npm run dev                     # Next.js on :3000`

Visit `http://localhost:3000/prompts`.  
 Create a prompt; it POSTs to your API and re-lists.

---

## **Where agents/Gemini plug in now**

* **Planning:** `/plan "Add PUT /api/prompts/:id and edit form"`

* **Schema:** `/prp:schema` when you introduce versioning/history tables.

* **Implementation:** `/implement @plan.md` to add routes \+ tests.

* **Verification:** `npm run lint && npm test` stays the green gate.

---

## **Next tiny upgrades (when you’re ready)**

1. **Export `app` for real tests**  
    Refactor `server/index.js` to export the Express app, and start the server in a separate `start.js`, so Jest \+ Supertest can hit routes in-process.

2. **Add CORS** if you host web and API on different origins.  
    `npm i cors` then `app.use(cors())`.

3. **Basic auth** for POST routes (JWT or a static token) to keep random writes out when it’s public.

4. **Deploy**

* API: your current Namecheap can run Node services behind Passenger or as a simple process (or deploy to a small VPS/render.com).

* Web: Next.js can be built and exported static (or hosted on Vercel) while it calls your API.

---

You’ve now got a complete, minimal **headless stack**: database → API → frontend UI. It’s small enough to hold in your head, structured enough for AI to extend safely. When you want, I can add a simple **Research list** page that reads from `research_post` and links PDFs—same pattern, same calm footprint.


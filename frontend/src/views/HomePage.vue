<template>
  <div class="min-h-screen bg-slate-950 text-slate-50 flex flex-col">
    <!-- Nav -->
    <header class="border-b border-slate-800/80 bg-slate-950/80 backdrop-blur">
      <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div
            class="h-8 w-8 rounded-lg bg-indigo-500/20 border border-indigo-400/40 flex items-center justify-center text-xs font-semibold text-indigo-200"
          >
            CG
          </div>
          <div class="flex flex-col">
            <span class="text-sm font-semibold tracking-tight">
              Company Guideline Assistant
            </span>
            <span class="text-[11px] text-slate-400">
              A private AI layer over your policies, knowledge, and financial data
            </span>
          </div>
        </div>

        <div class="flex items-center gap-3 text-xs">
          <RouterLink
            to="/login"
            class="px-3 py-1.5 rounded-lg border border-slate-700 hover:border-slate-500 hover:bg-slate-900/70 transition"
          >
            Sign in
          </RouterLink>
        </div>
      </div>
    </header>

    <!-- Hero -->
    <main class="flex-1">
      <section
        class="max-w-6xl mx-auto px-4 py-10 md:py-16 grid md:grid-cols-2 gap-10 items-center"
      >
        <!-- Left: copy -->
        <div class="space-y-5">
          <p
            class="inline-flex items-center gap-2 rounded-full border border-indigo-400/40 bg-indigo-500/10 px-3 py-1 text-[11px] font-medium text-indigo-100"
          >
            Multi‑tenant AI copilot for modern organisations
            <span class="h-1 w-1 rounded-full bg-emerald-400 animate-pulse" />
            <span class="text-[10px] text-emerald-200/80">Your content. Your rules. Your data.</span>
          </p>

          <h1 class="text-3xl md:text-4xl font-semibold tracking-tight text-slate-50">
            Turn scattered company documents and data into one searchable, conversational brain.
          </h1>

          <p class="text-sm md:text-[15px] text-slate-300 leading-relaxed max-w-xl">
            Upload policies, playbooks, reports, and spreadsheets. Company Guideline Assistant
            becomes a private AI helpdesk that answers questions, explains procedures, and turns
            financial tables into clear comparisons and charts — without leaking data or inventing
            new rules.
          </p>

          <!-- Primary actions -->
          <div class="flex flex-wrap gap-3 pt-1">
            <RouterLink
              to="/login"
              class="inline-flex items-center justify-center px-4 py-2.5 rounded-lg bg-indigo-500 text-xs font-medium text-white shadow-sm hover:bg-indigo-400 transition"
            >
              Try it with your documents
            </RouterLink>
            <a
              href="#how-it-works"
              class="inline-flex items-center justify-center px-4 py-2.5 rounded-lg border border-slate-700 text-xs font-medium text-slate-200 hover:border-slate-500 hover:bg-slate-900/70 transition"
            >
              See how it works
            </a>
          </div>

          <!-- Key benefits / capabilities -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-4 text-[11px] text-slate-300">
            <div class="flex items-start gap-2">
              <span class="mt-1 h-1.5 w-1.5 rounded-full bg-emerald-400"></span>
              <div>
                <p class="font-semibold text-slate-100">Multi‑tenant by design</p>
                <p class="text-slate-400">
                  Serve multiple clients or business units from one stack while keeping workspaces,
                  indexes, and chat history fully isolated.
                </p>
              </div>
            </div>
            <div class="flex items-start gap-2">
              <span class="mt-1 h-1.5 w-1.5 rounded-full bg-emerald-400"></span>
              <div>
                <p class="font-semibold text-slate-100">Role‑aware answers</p>
                <p class="text-slate-400">
                  Shape responses for HR, managers, execs, vendors, or employees based on their
                  access and responsibilities.
                </p>
              </div>
            </div>
            <div class="flex items-start gap-2">
              <span class="mt-1 h-1.5 w-1.5 rounded-full bg-emerald-400"></span>
              <div>
                <p class="font-semibold text-slate-100">Data & financial analysis</p>
                <p class="text-slate-400">
                  Ask for quarterly revenue, expenses, and net‑profit tables and get side‑by‑side
                  comparisons with charts straight from your reports.
                </p>
              </div>
            </div>
          </div>

          <!-- Example questions strip -->
          <div class="pt-3">
            <p class="text-[11px] font-semibold text-slate-400 mb-1">
              Ask in plain language:
            </p>
            <div class="flex flex-wrap gap-2 text-[11px]">
              <span
                class="px-2.5 py-1 rounded-full bg-slate-900/80 border border-slate-700/60 text-slate-300"
              >
                “What is our travel reimbursement policy and who signs off?”
              </span>
              <span
                class="px-2.5 py-1 rounded-full bg-slate-900/80 border border-slate-700/60 text-slate-300"
              >
                “Compare Q1 2023 vs Q1 2024 financial performance with charts.”
              </span>
              <span
                class="px-2.5 py-1 rounded-full bg-slate-900/80 border border-slate-700/60 text-slate-300"
              >
                “Summarise the onboarding handbook for new engineers.”
              </span>
            </div>
          </div>
        </div>

        <!-- Right: stacked previews – finance + policy -->
        <div class="relative space-y-4">
          <div
            class="absolute -inset-6 bg-indigo-500/10 blur-3xl rounded-3xl pointer-events-none"
          ></div>

          <!-- Finance / charts card -->
          <div
            class="relative rounded-2xl border border-slate-800 bg-slate-950/80 shadow-xl shadow-slate-950/60 overflow-hidden"
          >
            <div
              class="border-b border-slate-800 px-4 py-2.5 flex items-center justify-between"
            >
              <span class="text-xs font-medium text-slate-200">
                Financial performance analysis
              </span>
              <span class="text-[11px] text-slate-500">
                Tables and charts from your reports
              </span>
            </div>

            <div class="p-4 space-y-3 text-[11px] text-slate-200">
              <!-- Chart sample explanation -->
              <div class="space-y-1.5">
                <p class="font-medium text-slate-100">
                  “Generate financial performance tables and charts for Q1 2023 and 2024.”
                </p>
                <p class="text-slate-400 leading-relaxed">
                  The assistant reads your quarterly statements, builds revenue, total‑expense, and
                  net‑profit tables, then renders comparison charts so leaders see trends in seconds
                  instead of digging through spreadsheets.
                </p>
              </div>

              <!-- Image samples -->
              <div class="space-y-2">
                <p class="text-[10px] uppercase tracking-wide text-slate-500 font-semibold">
                  What your managers see
                </p>

                <div class="grid grid-cols-1 gap-3">
                  <!-- Bar chart sample -->
                  <div
                    class="relative rounded-lg border border-indigo-500/40 bg-slate-900 overflow-hidden shadow-lg"
                  >
                    <img
                      src="/assets/bar.png"
                      alt="Revenue and expenses comparison charts Q1 2023 vs Q1 2024"
                      class="w-full h-32 md:h-36 object-cover"
                    />
                    <div
                      class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-slate-950/90 to-transparent px-3 pb-2 pt-6 text-[10px]"
                    >
                      <p class="text-slate-100 font-semibold">
                        Revenue & expenses comparison · Q1 2023 vs Q1 2024
                      </p>
                      <p class="text-slate-400">
                        Grouped bars call out shifts in spend and growth at a glance.
                      </p>
                    </div>
                  </div>

                  <!-- Line chart sample -->
                  <div
                    class="relative rounded-lg border border-indigo-500/40 bg-slate-900 overflow-hidden shadow-lg"
                  >
                    <img
                      src="/assets/line.png"
                      alt="Financial performance line chart Q1 2023 vs Q1 2024"
                      class="w-full h-32 md:h-36 object-cover"
                    />
                    <div
                      class="absolute inset-x-0 bottom-0 bg-gradient-to-t from-slate-950/90 to-transparent px-3 pb-2 pt-6 text-[10px]"
                    >
                      <p class="text-slate-100 font-semibold">
                        Financial performance line chart
                      </p>
                      <p class="text-slate-400">
                        Follow revenue, expenses, and net profit month by month.
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <div
                class="rounded-lg border border-dashed border-slate-800 bg-slate-900/60 px-3 py-2 text-[11px] text-slate-400"
              >
                The same engine powers HR answers and financial insights — one assistant, grounded
                entirely in your internal content.
              </div>
            </div>
          </div>

          <!-- Policy / knowledge card -->
          <div
            class="relative rounded-2xl border border-slate-800 bg-slate-950/90 shadow-lg shadow-slate-950/50 overflow-hidden"
          >
            <div
              class="border-b border-slate-800 px-4 py-2.5 flex items-center justify-between"
            >
              <span class="text-xs font-medium text-slate-200">Employee policy chat</span>
              <span class="text-[11px] text-slate-500">Answers from your company only</span>
            </div>
            <div class="p-4 space-y-3 text-[11px] text-slate-200">
              <div class="space-y-1.5">
                <p class="font-medium text-slate-100">
                  “What’s our remote work allowance?”
                </p>
                <p class="text-slate-400 leading-relaxed">
                  “According to your latest <span class='font-medium'>Remote Work Policy</span>,
                  full‑time employees can work remotely up to 3 days per week, subject to manager
                  approval and role eligibility. Security and equipment requirements are listed in
                  section 4.2…”
                </p>
              </div>
              <div
                class="rounded-lg border border-dashed border-slate-800 bg-slate-900/60 px-3 py-2 flex items-center"
              >
                <span class="text-slate-400">
                  Update a PDF once in the admin panel and every answer reflects the new version —
                  no retraining or redeploys.
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- How it works -->
      <section id="how-it-works" class="border-t border-slate-900 bg-slate-950">
        <div class="max-w-6xl mx-auto px-4 py-10 md:py-12 space-y-6">
          <div class="flex items-center justify-between gap-2">
            <h2 class="text-sm font-semibold text-slate-100">How it works</h2>
            <p class="text-[11px] text-slate-400">
              Built for consultancies, multi‑brand groups, and internal enablement teams who need AI
              that respects tenant boundaries.
            </p>
          </div>

          <div class="grid md:grid-cols-3 gap-6 text-sm text-slate-300">
            <div class="space-y-2">
              <p class="text-xs font-semibold text-indigo-300 uppercase tracking-wide">
                1. Onboard tenants in minutes
              </p>
              <p>
                Vendor and tenant admins create workspaces, configure collections, and invite HR,
                finance, Legal, and content owners from a simple web UI.
              </p>
            </div>
            <div class="space-y-2">
              <p class="text-xs font-semibold text-indigo-300 uppercase tracking-wide">
                2. Connect and upload knowledge
              </p>
              <p>
                Ingest handbooks, SOPs, contracts, wikis, and financial reports into secure,
                tenant‑scoped storage. Embeddings and chat history never cross tenants.
              </p>
            </div>
            <div class="space-y-2">
              <p class="text-xs font-semibold text-indigo-300 uppercase tracking-wide">
                3. Ask questions, get grounded answers
              </p>
              <p>
                Employees get clear, cited answers to policy questions. Managers get live‑from‑your‑
                data tables and charts — not generic internet AI.
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Footer CTA -->
    <footer class="border-t border-slate-900 bg-slate-950">
      <div
        class="max-w-6xl mx-auto px-4 py-6 flex flex-col md:flex-row items-center justify-between gap-3 text-[11px] text-slate-400"
      >
        <p class="max-w-xl">
          Stop forwarding PDFs and answering the same questions twice. Give every tenant a secure AI
          assistant that knows their policies and numbers — and can explain both.
        </p>
        <RouterLink
          to="/login"
          class="inline-flex items-center justify-center px-3 py-2 rounded-lg bg-indigo-500 text-xs font-medium text-white hover:bg-indigo-400 transition"
        >
          Open the app
        </RouterLink>
      </div>
    </footer>
  </div>
</template>

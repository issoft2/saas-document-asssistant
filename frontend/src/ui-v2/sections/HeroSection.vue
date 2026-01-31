<template>
  <section class="relative min-h-[90vh] flex items-center overflow-hidden bg-surface-neutral-50 px-6 lg:px-8">
    
    <div class="absolute inset-0 -z-10 opacity-[0.03]" aria-hidden="true">
      <svg class="h-full w-full" fill="none" viewBox="0 0 100 100" preserveAspectRatio="none">
        <defs>
          <pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse">
            <path d="M 10 0 L 0 0 0 10" stroke="currentColor" stroke-width="0.5"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#grid)" />
      </svg>
    </div>

    <div class="mx-auto max-w-7xl w-full grid lg:grid-cols-2 gap-12 items-center pt-20 pb-32">
      
      <div class="flex flex-col items-start space-y-8">
        
        <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-indigo-50 border border-indigo-100/50 transition-all hover:bg-indigo-100">
          <span class="material-symbols-rounded text-indigo-600 text-[18px]">verified_user</span>
          <span class="text-xs font-bold tracking-wider text-indigo-700 uppercase">
            Hard Isolation Enforced
          </span>
        </div>

        <h1 class="text-balance text-5xl font-semibold tracking-tight text-slate-900 sm:text-7xl">
          Institutional <br/>
          <span class="text-indigo-600">Sovereign Intelligence.</span>
        </h1>

        <p class="max-w-lg text-lg leading-relaxed text-slate-600">
          The trusted knowledge layer for multi-tenant organizations. 
          Ask questions, analyze reports, and generate insights exclusively from 
          your <span class="text-slate-900 font-medium underline decoration-indigo-300 underline-offset-4">grounded documents</span>.
        </p>

        <div class="flex flex-wrap gap-4 pt-4">
          <button class="relative group overflow-hidden bg-slate-900 px-8 py-4 rounded-full text-white font-medium transition-all hover:shadow-lg active:scale-95">
            <div class="absolute inset-0 bg-white opacity-0 group-hover:opacity-[0.12] transition-opacity"></div>
            <span class="relative flex items-center gap-2">
              Deploy Intelligence Layer
              <span class="material-symbols-rounded text-[20px]">arrow_forward</span>
            </span>
          </button>
          
          <button class="px-8 py-4 rounded-full border border-slate-300 text-slate-700 font-medium hover:bg-slate-50 transition-colors active:scale-95">
            Security Whitepaper
          </button>
        </div>
      </div>

      <div class="relative lg:ml-auto w-full max-w-[560px]">
        <div class="rounded-[28px] bg-white p-2 shadow-[0_20px_50px_rgba(0,0,0,0.1)] ring-1 ring-slate-200">
          <div class="rounded-[22px] bg-slate-50 overflow-hidden border border-slate-100">
            
            <div class="px-6 py-4 bg-white border-b border-slate-200 flex justify-between items-center">
              <div class="flex items-center gap-3">
                <div class="h-8 w-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white font-bold text-xs">AI</div>
                <div class="flex flex-col">
                  <span class="text-[11px] font-bold text-slate-900 leading-none">Global Ministry Hub</span>
                  <span class="text-[9px] text-emerald-600 font-medium flex items-center gap-1">
                    <span class="h-1 w-1 rounded-full bg-emerald-600 animate-pulse"></span>
                    Tenant: Subsidiary_Alpha
                  </span>
                </div>
              </div>
              <span class="material-symbols-rounded text-slate-400 text-[20px]">settings_input_component</span>
            </div>

            <div class="p-6 space-y-6">
              <div class="space-y-2">
                <div class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Query Retrieval Trace</div>
                <div class="p-4 rounded-xl bg-indigo-50/50 border border-indigo-100 text-[13px] text-slate-700 italic">
                  "Analyze our Q3 compliance risks across the EMEA region."
                </div>
              </div>

              <div class="space-y-4">
                <div class="flex items-center gap-2">
                  <span class="material-symbols-rounded text-emerald-600 text-[18px]">verified</span>
                  <span class="text-[11px] font-bold text-slate-500">Retrieval Sources (ACL Verified)</span>
                </div>
                <div class="grid grid-cols-2 gap-2">
                  <div class="p-2 rounded-lg bg-white border border-slate-200 text-[10px] font-medium flex items-center gap-2">
                    <span class="material-symbols-rounded text-[14px] text-red-500">description</span>
                    EMEA_Risk_SOP.pdf
                  </div>
                  <div class="p-2 rounded-lg bg-white border border-slate-200 text-[10px] font-medium flex items-center gap-2">
                    <span class="material-symbols-rounded text-[14px] text-blue-500">table_chart</span>
                    Q3_Audits.xlsx
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="absolute -top-12 -right-12 h-64 w-64 bg-indigo-200/30 blur-[100px] -z-10 rounded-full"></div>
      </div>

    </div>
  </section>
</template>

<script setup lang="ts">
// Logic for handling dynamic tenant names or roles could go here
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200');

/* M3 Transition Easing */
.ease-m3 {
  transition-timing-function: cubic-bezier(0.2, 0, 0, 1);
}
</style>
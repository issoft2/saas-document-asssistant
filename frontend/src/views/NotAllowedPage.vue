<template>
  <div class="min-h-screen flex items-center justify-center bg-slate-50">
    <div class="bg-white border border-slate-200 rounded-xl px-6 py-5 shadow-md max-w-sm text-center">
      <h1 class="text-sm font-semibold text-slate-800 mb-2">Access denied</h1>
      <p class="text-xs text-slate-500 mb-4">
        You do not have permission to view this page.
      </p>
      <RouterLink
        to="/"
        class="inline-flex items-center gap-1 rounded-md border border-slate-300 px-3 py-1.5
               text-xs font-medium text-slate-700 hover:bg-slate-100 hover:border-slate-400"
      >
        Go to home
      </RouterLink>
    </div>
  </div>
</template>

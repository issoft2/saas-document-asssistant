
<script setup>
import { computed } from 'vue'
import { authState, logout } from '../authStore'

// Same admin-capable roles as in admin layout
const adminRoles = [
  'group_admin',
  'group_exe',
  'group_hr',
  'group_finance',
  'group_operation',
  'group_production',
  'group_marketing',
  'group_legal',
  'sub_admin',
  'sub_md',
  'sub_hr',
  'sub_finance',
  'sub_operations',
  'vendor',
]

// Whether this user should see the configuration panel link
const canSeeAdmin = computed(() => {
  const role = authState.user?.role
  if (!role) return false
  return adminRoles.includes(String(role))
})

// Human-readable role label if you want to show it later
const roleLabel = computed(() => {
  const raw = authState.user?.role
  if (!raw) return 'Guest'
  const role = String(raw)

  if (role.startsWith('group_')) return 'Group ' + role.split('_')[1].toUpperCase()
  if (role.startsWith('sub_')) return 'Subsidiary ' + role.split('_')[1].toUpperCase()
  if (role === 'employee') return 'Employee'
  if (role === 'vendor') return 'Vendor'

  // Fallback for any legacy/custom roles
  return role
})
</script>


<template>
  <div class="min-h-screen flex flex-col bg-slate-50 text-slate-900">
    <header class="border-b bg-white h-14 flex items-center justify-between px-4 md:px-8">
      <div class="flex items-center gap-2 text-sm">
        <RouterLink
          v-if="canSeeAdmin"
          to="/admin/companies"
          class="inline-flex items-center gap-1 rounded-md border border-slate-300 px-3 py-1.5
                 text-xs font-medium text-slate-700 hover:bg-slate-100 hover:border-slate-400
                 hover:text-slate-900 transition-colors cursor-pointer"
        >
          <span class="h-1.5 w-1.5 rounded-full bg-emerald-500"></span>
          <span>Configuration panel</span>
        </RouterLink>
      </div>

      <div class="flex items-center gap-3 text-xs">
        <!-- Optional: show role -->
        <span class="text-slate-500">{{ roleLabel }}</span>

        <button
          v-if="authState.user"
          @click="logout"
          class="inline-flex items-center gap-1 rounded-md border border-slate-300 px-3 py-1.5
                 font-medium text-slate-700 hover:bg-slate-100 hover:border-slate-400
                 hover:text-slate-900 transition-colors cursor-pointer"
        >
          Logout
        </button>
      </div>
    </header>

    <main class="flex-1 flex px-0 md:px-0 py-0">
      <div class="w-full">
        <RouterView />
      </div>
    </main>
  </div>
</template>


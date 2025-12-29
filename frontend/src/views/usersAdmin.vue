<template>
  <div class="p-4">
    <div class="mb-3 flex items-center gap-2"> <!-- ✅ fixed items-centre -->
      <input 
        type="text"
        v-model="filter" 
        placeholder="Search by name or email"
        class="px-2 py-1 text-xs rounded bg-slate-900 border border-slate-700 text-slate-100 w-56"
      />
      <label class="flex items-center gap-1 text-[11px] text-slate-300"> <!-- ✅ fixed item-center -->
        <input type="checkbox" v-model="onlyActive" />
        Show only active
      </label>
      <span v-if="loading" class="text-[11px] text-slate-400">Loading...</span>
      <span v-if="error" class="text-[11px] text-red-400">{{ error }}</span>
    </div>

    <div
      class="grid gap-3"
      style="grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));"
    >
      <div
        v-for="u in filteredUsers"
        :key="u.id"
        class="border border-slate-800 rounded-lg p-3 bg-slate-950"
      >
        <div class="flex items-center justify-between mb-2">
          <div class="text-xs font-semibold text-slate-100">
            {{ `${u.first_name} ${u.last_name}`.trim() || 'No name' }} <!-- ✅ use first_name + last_name -->
          </div>
          <span
            class="text-[10px] px-2 py-0.5 rounded-full"
            :class="u.is_active
              ? 'bg-emerald-900 text-emerald-200'
              : 'bg-slate-800 text-slate-400'"
          >
            {{ u.is_active ? 'Active' : 'Inactive' }}
          </span>
        </div>

        <div class="text-[11px] text-slate-400 break-all mb-2">
          {{ u.email }}
        </div>

        <div class="mb-2">
          <label class="block text-[10px] text-slate-500">Role</label>
          <input
            v-model="u.role"
            class="mt-0.5 px-1 py-0.5 text-[11px] rounded bg-slate-900 border border-slate-700 text-slate-100 w-full"
          />
        </div>

        <div class="flex items-center justify-between mt-2 gap-2">
          <button
            class="flex-1 text-[11px] px-2 py-1 rounded bg-slate-800 text-slate-100 hover:bg-slate-700"
            @click="onSaveUser(u)"
          >
            Save
          </button>
          <button
            class="flex-1 text-[11px] px-2 py-1 rounded"
            :class="u.is_active
              ? 'bg-red-900 text-red-100 hover:bg-red-800'
              : 'bg-emerald-900 text-emerald-100 hover:bg-emerald-800'"
            @click="onToggleActive(u)"
          >
            {{ u.is_active ? 'Deactivate' : 'Activate' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { listUsers, updateUser } from '../composables/users'  // ✅ correct path for your structure
import type { User } from '../types/index'                  // ✅ correct path

const users = ref<User[]>([])
const loading = ref(false)
const error = ref('')
const filter = ref('')
const onlyActive = ref(true)

const filteredUsers = computed(() => 
  users.value.filter(user => {
    const fullName = `${user.first_name || ''} ${user.last_name || ''}`.toLowerCase()
    const matchText = !filter.value || 
      user.email.toLowerCase().includes(filter.value.toLowerCase()) ||  // ✅ fixed toLowerCase
      fullName.includes(filter.value.toLowerCase())
    const matchActive = !onlyActive.value || user.is_active
    return matchText && matchActive
  })
)

async function loadUsers() {
  console.log('🔄 Loading users...')  // ✅ debug
  loading.value = true
  error.value = ''
  try {
    const res = await listUsers()
    users.value = res.data || []
    console.log('✅ Users loaded:', users.value.length)  // ✅ debug
  } catch (e: any) {
    console.error('❌ Load users error:', e)  // ✅ debug
    error.value = e?.response?.data?.detail || 'Failed to load users.'
  } finally {
    loading.value = false
  }
}

async function onToggleActive(user: User) {
  const confirmMsg = user.is_active
    ? `Deactivate ${user.email}?`
    : `Activate ${user.email}?`
  if (!window.confirm(confirmMsg)) return

  try {
    const res = await updateUser(user.id, { is_active: !user.is_active })
    const updated = res.data
    const idx = users.value.findIndex(u => u.id === updated.id)  // ✅ fixed: u.id === updated.id
    if (idx !== -1) users.value[idx] = updated
  } catch (e: any) {
    error.value = e?.response?.data?.detail || 'Failed to update user.'
  }
}

async function onSaveUser(user: User) {
  try {
    const res = await updateUser(user.id, {
      first_name: user.first_name,
      last_name: user.last_name,  // ✅ added last_name
      role: user.role,
    })
    const updated = res.data
    const idx = users.value.findIndex(u => u.id === updated.id)  // ✅ fixed: u.id === updated.id
    if (idx !== -1) users.value[idx] = updated
  } catch (e: any) {
    error.value = e?.response?.data?.detail || 'Failed to save user.'
  }
}

onMounted(() => {
  console.log('📱 UsersAdmin mounted')  // ✅ debug
  loadUsers()
})
</script>

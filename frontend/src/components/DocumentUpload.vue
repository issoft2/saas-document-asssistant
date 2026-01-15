<template>
  <form @submit.prevent="handleUpload" class="space-y-3">
    <label class="block text-xs font-medium text-slate-600">
      Document title (optional)
      <input
        v-model="title"
        type="text"
        class="input"
        placeholder="e.g. Remote Work Policy v1"
        :disabled="loading || !canUpload"
      />
    </label>

    <label class="block text-xs font-medium text-slate-600">
      Select file
      <input
        type="file"
        class="mt-1 block w-full text-xs text-slate-600"
        @change="onFileChange"
        :disabled="loading || !canUpload"
        required
      />
    </label>

    <p
      v-if="!canUpload"
      class="text-[11px] text-red-600"
    >
      Your role is not allowed to upload documents. Contact your administrator.
    </p>

    <button
      type="submit"
      class="btn-primary"
      :disabled="loading || !file || !canUpload"
    >
      <span v-if="loading">Uploading &amp; indexing…</span>
      <span v-else>Upload document</span>
    </button>

    <p v-if="message" class="text-xs text-emerald-600">{{ message }}</p>
    <p v-if="error" class="text-xs text-red-600">{{ error }}</p>
  </form>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { authState } from '../authStore'
import { uploadDocument } from '../api'

const props = defineProps({
  // Backend now infers tenant from token; collection is still explicit
  collectionName: { type: String, required: true },
})

const title = ref('')
const file = ref<File | null>(null)
const loading = ref(false)
const message = ref('')
const error = ref('')

// ---- Role / tenant awareness ----
const currentUser = computed(() => authState.user)
const currentRole = computed(() => currentUser.value?.role || '')
const currentTenantId = computed(() => currentUser.value?.tenant_id || '')

const groupAdminRoles = [
  'group_admin',
  'group_exe',
  'group_hr',
  'group_finance',
  'group_operation',
  'group_production',
  'group_marketing',
  'group_legal',
]
const subAdminRoles = [
  'sub_admin',
  'sub_md',
  'sub_hr',
  'sub_finance',
  'sub_operations',
]

const isVendor = computed(() => currentRole.value === 'vendor')
const isGroupAdmin = computed(() => groupAdminRoles.includes(currentRole.value))
const isSubAdmin = computed(() => subAdminRoles.includes(currentRole.value))

// Employees cannot upload; only vendor/group/sub admins can
const canUpload = computed(
  () => isVendor.value || isGroupAdmin.value || isSubAdmin.value,
)

function onFileChange(e: Event) {
  const target = e.target as HTMLInputElement
  const files = target.files
  file.value = files && files[0] ? files[0] : null
}

async function handleUpload() {
  if (!file.value || loading.value) return

  error.value = ''
  message.value = ''

  if (!canUpload.value) {
    error.value = 'Your role is not allowed to upload documents.'
    return
  }
  if (!currentTenantId.value) {
    error.value = 'No tenant is associated with your account.'
    return
  }

  loading.value = true
  try {
    const res = await uploadDocument({
      tenantId: currentTenantId.value,        // from auth, not from props
      collectionName: props.collectionName,
      title: title.value,
      file: file.value,
      doc_id: '',                             // matches ingestion page backend
    })
    message.value = `Uploaded. Chunks indexed: ${res.data.chunks_indexed ?? 'n/a'}.`
    file.value = null
  } catch (e: any) {
    error.value =
      e?.response?.data?.detail || 'Failed to upload document.'
  } finally {
    loading.value = false
  }
}
</script>

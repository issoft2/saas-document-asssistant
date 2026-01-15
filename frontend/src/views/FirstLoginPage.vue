<template>
  <div class="min-h-screen flex items-center justify-center bg-slate-50 px-4">
    <div class="w-full max-w-md bg-white shadow-md rounded-lg p-6 space-y-4">
      <h1 class="text-lg font-semibold text-slate-900">Set your password</h1>

      <p class="text-xs text-slate-500">
        Choose a new password to complete your first-time sign in.
      </p>

      <p v-if="error" class="text-sm text-red-600">
        {{ error }}
      </p>

      <p v-if="loading" class="text-sm text-slate-500">
        Verifying your first-time login link…
      </p>

      <form
        v-if="!loading && !done"
        @submit.prevent="onSubmit"
        class="space-y-3"
      >
        <div>
          <label class="block text-xs font-medium text-slate-700 mb-1">
            New password
          </label>
          <input
            v-model="password"
            type="password"
            required
            class="w-full border rounded-md px-3 py-2 text-sm"
            :disabled="submitting"
          />
          <p class="mt-1 text-[11px] text-slate-400">
            At least 8 characters. Use a mix of letters, numbers, and symbols.
          </p>
        </div>

        <div>
          <label class="block text-xs font-medium text-slate-700 mb-1">
            Confirm password
          </label>
          <input
            v-model="confirmPassword"
            type="password"
            required
            class="w-full border rounded-md px-3 py-2 text-sm"
            :disabled="submitting"
          />
        </div>

        <button
          type="submit"
          class="w-full btn-primary text-sm py-2"
          :disabled="submitting"
        >
          {{ submitting ? 'Saving…' : 'Save password' }}
        </button>
      </form>

      <p v-if="done" class="text-sm text-emerald-700">
        Password set. Redirecting…
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { authState, firstLoginVerify, firstLoginSetPassword } from '../authStore'
import { me as apiMe, setAuthToken } from '../api'

const route = useRoute()
const router = useRouter()

const token = ref<string | null>(null)
const loading = ref(true)
const error = ref<string | null>(null)
const password = ref('')
const confirmPassword = ref('')
const submitting = ref(false)
const done = ref(false)

// Role groups aligned with backend
const adminRoles = [
  'vendor',
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
]

onMounted(async () => {
  token.value = (route.query.token as string) || null
  if (!token.value) {
    error.value = 'Invalid first-time login link.'
    loading.value = false
    return
  }

  try {
    await firstLoginVerify({ token: token.value })
  } catch {
    error.value = 'This first-time login link is invalid or has expired.'
  } finally {
    loading.value = false
  }
})

const onSubmit = async () => {
  if (!token.value || submitting.value) return

  if (password.value !== confirmPassword.value) {
    error.value = 'Passwords do not match.'
    return
  }
  if (password.value.length < 8) {
    error.value = 'Password must be at least 8 characters long.'
    return
  }

  submitting.value = true
  error.value = null

  try {
    const { data } = await firstLoginSetPassword({
      token: token.value,
      new_password: password.value,
    })

    setAuthToken(data.access_token)
    const meResp = await apiMe()
    authState.user = meResp.data
    done.value = true

    const role = authState.user?.role || ''
    if (adminRoles.includes(role)) {
      router.push('/admin/companies')
    } else {
      router.push('/chat')
    }
  } catch (e: any) {
    error.value =
      e?.response?.data?.detail ||
      'Could not set password. Please try again or contact support.'
  } finally {
    submitting.value = false
  }
}
</script>

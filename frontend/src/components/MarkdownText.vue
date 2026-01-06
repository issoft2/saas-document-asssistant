<!-- src/components/MarkdownText.vue -->
<template>
  <div :class="wrapperClass" v-html="compiled"></div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import MarkdownIt from 'markdown-it'

const props = defineProps<{
  content: string
  class?: string
}>()

const md = new MarkdownIt({
  html: false,
  linkify: true,
  breaks: true,
})

const compiled = computed(() => md.render(props.content || ''))
const wrapperClass = computed(() => props.class)
</script>

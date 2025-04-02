<template>
  <nav v-if="totalPages > 1" class="mt-4">
    <ul class="pagination justify-content-center">
      <li class="page-item" :class="{ disabled: currentPage === 1 }">
        <button class="page-link" @click="$emit('page-change', currentPage - 1)" :disabled="currentPage === 1">
          Anterior
        </button>
      </li>

      <li 
        v-for="page in visiblePages" 
        :key="page" 
        class="page-item" 
        :class="{ active: page === currentPage, disabled: page === '...' }"
      >
        <button 
          class="page-link" 
          @click="page !== '...' && $emit('page-change', page)" 
          :disabled="page === '...'"
        >
          {{ page }}
        </button>
      </li>

      <li class="page-item" :class="{ disabled: currentPage === totalPages }">
        <button class="page-link" @click="$emit('page-change', currentPage + 1)" :disabled="currentPage === totalPages">
          Próximo
        </button>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Pagination',
  props: {
    currentPage: {
      type: Number,
      required: true
    },
    totalPages: {
      type: Number,
      required: true
    }
  },
  computed: {
    visiblePages(): (number | string)[] {
      const pages: (number | string)[] = [];
      const maxVisible = 5;
      const halfVisible = Math.floor(maxVisible / 2);

      if (this.totalPages <= maxVisible) {
        for (let i = 1; i <= this.totalPages; i++) {
          pages.push(i);
        }
      } else {
        pages.push(1);

        if (this.currentPage > halfVisible + 2) {
          pages.push('...');
        }

        const start = Math.max(2, this.currentPage - halfVisible);
        const end = Math.min(this.totalPages - 1, this.currentPage + halfVisible);
        for (let i = start; i <= end; i++) {
          pages.push(i);
        }

        if (this.currentPage < this.totalPages - halfVisible - 1) {
          pages.push('...');
        }

        pages.push(this.totalPages);
      }

      return pages;
    }
  }
});
</script>

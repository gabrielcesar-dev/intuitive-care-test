<template>
  <div class="card mb-4">
    <div class="card-body">
      <h5 class="card-title">Pesquisar Operadoras</h5>
      <div class="input-group mb-3">
        <input 
          type="text" 
          class="form-control" 
          placeholder="Digite nome, CNPJ, registro ANS, cidade..." 
          v-model="searchQuery"
          @keyup.enter="search"
        >
        <button class="btn btn-primary" type="button" @click="search">
          <i class="bi bi-search"></i> Buscar
        </button>
      </div>
      <div class="d-flex align-items-center small">
        <span class="text-muted me-2">Sugestões de busca:</span>
        <button 
          v-for="suggestion in suggestions" 
          :key="suggestion"
          class="btn btn-sm btn-outline-secondary me-1 mb-1"
          @click="searchFor(suggestion)"
        >
          {{ suggestion }}
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OperatorSearch',
  data() {
    return {
      searchQuery: '',
      suggestions: ['UNIMED', 'São Paulo', 'Cooperativa', 'Amil', 'Bradesco']
    };
  },
  methods: {
    search() {
      if (this.searchQuery.trim()) {
        this.$emit('search', this.searchQuery);
      }
    },
    searchFor(term) {
      this.searchQuery = term;
      this.search();
    }
  }
}
</script>
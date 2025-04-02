<template>
  <div class="container mt-4">
    <h1 class="mb-4">Busca de Operadoras de Saúde</h1>
    <div class="alert alert-info" v-if="connectionStatus === 'checking'">
      Verificando conexão com o servidor...
    </div>
    <div class="alert alert-danger" v-if="connectionStatus === 'error'">
      <strong>Erro!</strong> Não foi possível conectar ao servidor. Verifique se o backend está rodando em http://localhost:8000
    </div>
    <template v-if="connectionStatus !== 'error'">
      <OperatorSearch 
        @search="performSearch" 
      />
      <OperatorList 
        :operators="paginatedOperators" 
        :loading="loading" 
        :current-page="currentPage"
        :total-pages="totalPages"
        @page-change="handlePageChange"
      />
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import OperatorSearch from './components/OperatorSearch.vue';
import OperatorList from './components/OperatorList.vue';

interface Operator {
  registro_ans: string;
  cnpj: string;
  razao_social: string;
  nome_fantasia?: string;
  modalidade: string;
  cidade?: string;
  uf?: string;
  endereco_eletronico?: string;
  telefone?: string;
  regiao_de_comercializacao?: string;
}

export default defineComponent({
  name: 'App',
  components: {
    OperatorSearch,
    OperatorList
  },
  data() {
    return {
      operators: [] as Operator[],
      loading: false,
      apiUrl: 'http://localhost:8000/api/operators/search/',
      connectionStatus: 'checking' as 'checking' | 'connected' | 'error',
      currentPage: 1,
      totalPages: 1,
      itemsPerPage: 10
    };
  },
  computed: {
    paginatedOperators() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.operators.slice(start, end);
    }
  },
  mounted() {
    this.checkBackendConnection();
  },
  methods: {
    checkBackendConnection() {
      axios.get('http://localhost:8000/api/operators/search/?q=test')
        .then(() => {
          this.connectionStatus = 'connected';
        })
        .catch(error => {
          if (error.code === 'ERR_NETWORK') {
            this.connectionStatus = 'error';
          } else {
            this.connectionStatus = 'connected';
          }
        });
    },
    async performSearch(query: string) {
      if (!query) return;

      this.loading = true;
      try {
        const response = await axios.get(this.apiUrl, {
          params: { q: query }
        });
        this.operators = response.data.results;
        this.totalPages = Math.ceil(this.operators.length / this.itemsPerPage);
        this.currentPage = 1;
      } catch (error) {
        console.error('Error fetching data:', error);
        alert('Erro ao buscar operadoras. Por favor, tente novamente.');
      } finally {
        this.loading = false;
      }
    },
    handlePageChange(newPage: number) {
      this.currentPage = newPage;
    }
  }
});
</script>
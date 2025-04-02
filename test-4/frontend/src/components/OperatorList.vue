<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Resultados da Busca</h5>
      
      <div v-if="loading" class="text-center my-4">
        <div class="spinner-border text-primary" role="status">
          <span class="visually-hidden">Carregando...</span>
        </div>
        <p class="mt-2">Carregando resultados...</p>
      </div>
      
      <div v-else-if="operators.length === 0" class="alert alert-info">
        Nenhum resultado encontrado. Tente uma nova busca.
      </div>
      
      <div v-else>
        <div class="table-responsive">
          <table class="table table-striped table-hover">
            <thead>
              <tr>
                <th>Registro ANS</th>
                <th>CNPJ</th>
                <th>Razão Social</th>
                <th>Nome Fantasia</th>
                <th>Modalidade</th>
                <th>Cidade/UF</th>
                <th>Contato</th>
                <th>Região</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="operator in operators" :key="operator.registro_ans">
                <td>{{ operator.registro_ans }}</td>
                <td>{{ formatCnpj(operator.cnpj) }}</td>
                <td>{{ operator.razao_social }}</td>
                <td>{{ operator.nome_fantasia || '-' }}</td>
                <td>{{ operator.modalidade }}</td>
                <td>{{ operator.cidade && operator.uf ? `${operator.cidade}/${operator.uf}` : '-' }}</td>
                <td>
                  <div v-if="operator.endereco_eletronico || operator.telefone">
                    <div v-if="operator.telefone">Tel: {{ operator.telefone }}</div>
                    <div v-if="operator.endereco_eletronico">{{ operator.endereco_eletronico }}</div>
                  </div>
                  <span v-else>-</span>
                </td>
                <td>{{ operator.regiao_de_comercializacao || '-' }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <Pagination 
          :current-page="currentPage" 
          :total-pages="totalPages" 
          @page-change="$emit('page-change', $event)" 
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Pagination from './Pagination.vue';

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
  name: 'OperatorList',
  components: {
    Pagination
  },
  props: {
    operators: {
      type: Array as () => Operator[],
      required: true
    },
    loading: {
      type: Boolean,
      default: false
    },
    currentPage: {
      type: Number,
      required: true
    },
    totalPages: {
      type: Number,
      required: true
    }
  },
  methods: {
    formatCnpj(cnpj: string): string {
      if (!cnpj) return '-';
      if (/^\d{14}$/.test(cnpj)) {
        return cnpj.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/, '$1.$2.$3/$4-$5');
      }
      return cnpj;
    }
  }
});
</script>
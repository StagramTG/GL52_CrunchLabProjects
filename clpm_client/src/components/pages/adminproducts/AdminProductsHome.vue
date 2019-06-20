<template>
    <div class="admin-products">
        <div class="box">
            <div class="space-between">
                <h3>Produits</h3>
                <div>
                    <router-link to="/app/admin/products/create" class="button success">+ Créer</router-link> &nbsp;
                    <router-link to="/app/admin" class="button primary">Retour</router-link>
                </div>
            </div>
            <table class="data-table">
                <tbody>
                    <tr v-for="product in products" :key="product.id">
                        <td>{{product.name}} : {{product.price}} €</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            products: {}
        }
    },
    mounted() {
        let self = this;
        axios.get('api/products/list').then(function(response){
            self.products = response.data;
        })
    }
}
</script>

<style scoped>
    .admin-products {
        padding: 20px;
        overflow-y: auto;
    }
</style>
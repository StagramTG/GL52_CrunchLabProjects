<template>
    <div class="shop">
        <div class="box">
            <h3>Boutique</h3>
            <table class="data-table">
                <tbody>
                    <tr v-for="product in products" :key="product.id">
                        <div class="space-between">
                            <td>{{product.name}} : {{product.price}} €</td>
                            <td><a href="" class="button success" @click.prevent="add_cart(product.id)">Ajouter au panier</a></td>
                        </div>
                    </tr>
                </tbody>
            </table>
            <a href="" class="button success right" @click.prevent="">Consulter le panier</a>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            products: {},
            cart: [],
        }
    },
    mounted() {
        let self = this;
        axios.get('api/products/list').then(function(response){
            self.products = response.data;
        })
    },
    methods: {
        add_cart(id) {
            this.cart.push(id);
        }
    }
}
</script>

<style lang="scss">
    .shop {
        padding: 20px;
        overflow-y: auto;
    }
</style>
<template>
    <div class="shop">
        <div class="box">
            <h3>Boutique</h3>
            <table class="data-table">
                <tbody>
                    <tr v-for="product in products" :key="product.id">
                        <div class="space-between">
                            <td>{{product.name}} : {{product.price}} €</td>
                            <td><router-link :to="{name: 'app.shop.checkout', params: {id: product.id}}"><a href="" class="button success">Acheter</a></router-link></td>
                        </div>
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
            products: {},
            cart: [],
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

<style lang="scss">
    .shop {
        padding: 20px;
        overflow-y: auto;
    }
</style>
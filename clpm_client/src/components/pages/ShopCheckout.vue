<template>
    <div class="shop-checkout">
        <div class="box">
            <h3>Acheter le produit :</h3><br>

            <div class="message danger invisible" id="insufficient-amount-msg">
                <span>Solde portemonnaie insuffisant. Veuillez réaprovisionner le compte</span>
            </div>

            <h4>Nom du produit : {{this.name}}</h4>
            <h4>Prix : {{this.price}} €</h4>
            <h4>Description :</h4>
            <div>{{this.description}}</div><br>
            <div class="right">
                <router-link to="/app/shop" class="button primary">Retour</router-link>
                <a href="" class="button success" @click.prevent="checkout()">Confirmer l'achat</a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            name: '',
            price: '',
            description: '',
            user: {},
        }
    },
    mounted() {
        let self = this;
        let productId = this.$route.params.id;
        axios.get('api/products/' + productId + '/details').then(function(response){
            self.name = response.data.name
            self.price = response.data.price
            self.description = response.data.description
        })
    },
    methods: {
        checkout() {
            let self = this;
            axios.get('api/user/details').then(function(response){
                let userId = response.data.id;
                axios.get('api/account/' + userId + '/details').then(function(response) {
                    let amount = response.data.balance;
                    let enough = true;
                    if (self.price > amount) {
                        document.querySelector('#insufficient-amount-msg').classList.remove('invisible');
                        enough = false;
                    }
                    else {
                        document.querySelector('#insufficient-amount-msg').classList.add('invisible');
                    }

                    if (enough) {

                        axios.post('api/account/' + userId + '/update', {
                            amount: self.price
                        }).then(function(response){
                            if (response.status == 200) {
                                axios.post('api/account/transaction', {
                                    amount: -self.price,
                                    id: userId,
                                }).then(function(response) {
                                    if (response.status == 200) {
                                        self.$router.push('/app/shop');
                                    }
                                });
                            }
                        });
                    }
                })
            })
        }
    }
}
</script>

<style lang="scss">
    .shop-checkout {
        padding: 20px;
        overflow-y: auto;
    }
</style>
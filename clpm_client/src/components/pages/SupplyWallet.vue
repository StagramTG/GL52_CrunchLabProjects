<template>
    <div class="supply-wallet">
        <div class="box">
            <h3>Ajouter des fonds</h3><br>
            <div>Veuillez rentrer vos informations de paiement :</div>

            <div class="form-field">
                <span class="label">Numéro de carte :</span>
                <input type="text" id="card-number">
            </div>

            <div class="form-field">
                <span class="label">Propriétaire de la carte :</span>
                <input type="text" id="card-owner">
            </div>

            <div class="form-field">
                <span class="label">Date d'expiration :</span>
                <input type="date" id="card-expiration">
            </div>

            <div class="form-field">
                <span class="label">CCV :</span>
                <input type="text" id="card-ccv">
            </div>

            <div class="form-field">
                <span class="label">Montant à créditer :</span>
                <input type="number" v-model="amount" id="card-amount">
            </div>
            <a href="" class="button success" @click.prevent="supply_wallet()">Confirmer</a>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {}
    },
    methods: {
        supply_wallet() {
            let self = this;
            axios.post('api/account/supply', {
                amount: self.amount,
                id: self.$route.params.id,
            }).then(function(response){
                if (response.status == 200) {
                        self.$router.push('/app/wallet');
                }
            })
        }
    }
}
</script>

<style lang="scss">
    .supply-wallet {
        padding: 20px;
        overflow-y: auto;
    }
</style>
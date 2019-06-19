<template>
    <div class="supply-wallet">
        <div class="box">
            <h3>Ajouter des fonds</h3><br>
            <div>Veuillez rentrer vos informations de paiement :</div><br>

            <div class="message danger invisible" id="invalid-empty-msg">
                <span>Veuillez renseigner tous les champs.</span>
            </div>

            <div class="message danger invisible" id="invalid-card-msg">
                <span>Veuillez entrer un numéro de carte bancaire valide :</span>
            </div>

            <div class="message danger invisible" id="invalid-ccv-msg">
                <span>Veuillez entrer un CCV valide :</span>
            </div>

            <div class="form-field">
                <span class="label">Numéro de carte :</span>
                <input type="text" v-model="number" id="card-number">
            </div>

            <div class="form-field">
                <span class="label">Propriétaire de la carte :</span>
                <input type="text" v-model="owner" id="card-owner">
            </div>

            <div class="form-field">
                <span class="label">Date d'expiration :</span>
                <input type="date" v-model="date" id="card-expiration">
            </div>

            <div class="form-field">
                <span class="label">CCV :</span>
                <input type="text" v-model="ccv" id="card-ccv">
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
        return {
            number: '',
            owner: '',
            date: '',
            ccv: '',
            amount: '',
        }
    },
    methods: {
        supply_wallet() {

            let dataAreValide = true;

            //(\d{6}[-\s]?\d{12})|(\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}/)
            if(!(/^\d{16}$/.test(this.number))) {
                document.querySelector('#invalid-card-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-card-msg').classList.add('invisible');
            }

            if(!(/^\d{3}$/.test(this.ccv))) {
                document.querySelector('#invalid-ccv-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-ccv-msg').classList.add('invisible');
            }

            if (this.owner === "" || this.date === "") {
                document.querySelector('#invalid-empty-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-empty-msg').classList.add('invisible');
            }

            if (dataAreValide) {
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
}
</script>

<style lang="scss">
    .supply-wallet {
        padding: 20px;
        overflow-y: auto;
    }
</style>
<template>
    <div class="admin-create-products">
        <div class="box">
            <h3>Créer un produit</h3>

            <div class="message danger invisible" id="invalid-price-msg">
                <span>Veuillez entrer un prix valide</span>
            </div>

            <div class="message danger invisible" id="invalid-empty-msg">
                <span>Veuillez renseigner tous les champs.</span>
            </div>

            <div class="form-field">
                <span class="label">Nom du produit</span>
                <input type="text" v-model="name">
            </div>

            <div class="form-field">
                <span class="label">Prix</span>
                <input type="number" v-model="price">
            </div>

            <div class="form-field">
                <span class="label">Description</span>
                <textarea type="text" rows="4" v-model="description"></textarea>
            </div>
            <div class="right">
                <router-link to="/app/admin/products" class="button primary">Retour</router-link>
                <a href="" class="button success" @click.prevent="create()">Confirmer</a>
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
        }
    },
    methods: {
        create() {
            let dataAreValide = true;

            if(!(/^[0-9]+(\.[0-9]{1,2})?$/.test(this.price))) {
                document.querySelector('#invalid-price-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-price-msg').classList.add('invisible');
            }

            if (this.name === "" || this.description === "") {
                document.querySelector('#invalid-empty-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-empty-msg').classList.add('invisible');
            }

            if (dataAreValide) {
                let self = this;
                axios.post('api/products/create', {
                    name: self.name,
                    price: self.price,
                    description: self.description,
                }).then(function(response){
                    if (response.status == 200) {
                        self.$router.push('/app/admin/products');
                    }
                })
            }
        }
    }
}
</script>

<style scoped>
    .admin-create-products {
        padding: 20px;
        overflow-y: auto;
    }
</style>
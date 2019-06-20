<template>
    <div class="admin-product-modification">
        <div class="box">
            <h3>Modification du produit : {{name}}</h3>

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
                <a href="" class="button success" @click.prevent="update_product()">Modifier</a>
                <a href="" class="button danger" @click.prevent="delete_product()">Supprimer</a>
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
    mounted() {
        let self = this;
        let productId = this.$route.params.id;
        axios.get('api/products/' + productId + '/details').then(function(response){
            self.name = response.data.name
            self.price = response.data.price
            self.description = response.data.description
        })
    },
    methods : {
        update_product() {
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
                let productId = this.$route.params.id;
                axios.post('api/products/' + productId + '/update', {
                    name: self.name,
                    price: self.price,
                    description: self.description,
                }).then(function(response){
                    if (response.status == 200) {
                        self.$router.push('/app/admin/products');
                    }
                })
            }
        },

        delete_product() {
            let self = this;
            let productId = this.$route.params.id;
            axios.post('api/products/' + productId + '/delete').then(function(response){
                if (response.status == 200) {
                    self.$router.push('/app/admin/products');
                }
            })
        }
    }
}
</script>

<style scoped>
    .admin-product-modification {
        padding: 20px;
        overflow-y: auto;
    }
</style>
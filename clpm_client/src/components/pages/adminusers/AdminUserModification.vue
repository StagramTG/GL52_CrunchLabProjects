<template>
    <div class="admin-user-modification">
            <div class="box">
                <h3>Modification du compte de {{userInfo.first_name}} {{userInfo.last_name}}</h3>

                <div class="message danger invisible" id="invalid-empty-msg">
                    <span>Veuillez renseigner tous les champs.</span>
                </div>

                <div class="message danger invisible" id="invalid-mail-msg">
                    <span>Veuillez saisir une adresse mail valide.</span>
                </div>

                <div class="form-field">
                    <span class="label">Prénom</span>
                    <input type="text" v-model="first_name" id="new-user-fn">
                </div>

                <div class="form-field">
                    <span class="label">Nom</span>
                    <input type="text" v-model="last_name" id="new-user-ln">
                </div>

                <div class="form-field">
                    <span class="label">Nom d'utilisateur</span>
                    <input type="text" v-model="username" id="new-user-un">
                </div>

                <div class="form-field">
                    <span class="label">Email</span>
                    <input type="email" v-model="email" id="new-user-email">
                </div>

                <div class="form-field">
                    <span class="label">Téléphone</span>
                    <input type="text" v-model="phone" id="new-user-phone">
                </div>

                <div class="form-field">
                    <span class="label">Adresse</span>
                    <input type="text" v-model="location" id="new-user-location">
                </div>

                <div class="right">
                    <router-link to="/app/admin/users" class="button primary">Retour</router-link> &nbsp;&nbsp;
                    <a href="" class="button success" @click.prevent="update()">Modifier</a>
                    <a href="" class="button danger" @click.prevent="delete_user()">Supprimer</a>
                </div>
            </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            userInfo: []
        }
    },
    mounted() {
        let self = this;
        let userId = this.$route.params.id;
        axios.get('api/user/'+ userId + '/info').then(function(response){

            self.userInfo = response.data;
            self.username = self.userInfo.username;
            self.last_name = self.userInfo.last_name;
            self.first_name = self.userInfo.first_name;
            self.email = self.userInfo.email;
            self.phone = self.userInfo.phone;
            self.location = self.userInfo.location;

        });

    },
    methods: {
        update() {
            let dataAreValide = true;
            let userId = this.$route.params.id;
            // Check email validity
            if(!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email))) {
                document.querySelector('#invalid-mail-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-mail-msg').classList.add('invisible');
            }

            if(this.first_name === "" || this.last_name === "" || this.phone === "" || this.location === "")
            {
                document.querySelector('#invalid-empty-msg').classList.remove('invisible');
                dataAreValide = false;
            }
            else {
                document.querySelector('#invalid-empty-msg').classList.add('invisible');
            }

            if(dataAreValide) {
                // Perform request to create new user
                let self = this;
                axios.post('api/user/' + userId + '/update', {
                    email: self.email,
                    first_name: self.first_name,
                    last_name: self.last_name,
                    phone: self.phone,
                    location: self.location,
                    username: self.username
                }).then(function (response) {
                    if (response.status == 200) {
                        self.$router.push('/app/admin/users');
                    }
                });
            }
        },

        delete_user() {
            let self = this;
            let userId = this.$route.params.id;
            axios.post('api/user/' + userId + '/delete').then(function(response) {
                if (response.status == 200) {
                    self.$router.push('/app/admin/users');
                }
            });
        }
    }
}
</script>

<style lang="scss">
    .admin-user-modification {
        padding: 20px;
        overflow-y: auto;
    }
</style>
<template>
    <div class="admin-roles-create">
        <div class="box">
            <h3>Création d'un nouveau rôle</h3>

            <div class="form-field">
                <span class="label">Nom du rôle</span>
                <input type="text" v-model="name">
            </div>

            <div class="right">
                <router-link to="/app/admin/roles" class="button primary">Retour</router-link> &nbsp;&nbsp;
                <a href="" class="button success" @click.prevent="create()">Créer</a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            name: ''
        }
    },
    methods: {
        create() {
            if(this.name === "")
            {
                return;
            }

            let self = this;
            axios.post('api/project/role/create', { name: self.name })
                .then(function(response) {
                    self.$router.push('/app/admin/roles');
                });
        }
    }
}
</script>

<style lang="scss">
    .admin-roles-create {
        padding: 20px;
        overflow-y: auto;
    }
</style>

<template>
    <div class="project-creation">
        <div class="box">
            <h3>Créer un projet</h3>
            <p>Vous êtes les propriétaires des projets que vous créez.</p>

            <div class="form-field">
                <span class="label">Nom</span>
                <input type="text" v-model="name">
            </div>

            <div class="form-field">
                <span class="label">Description</span>
                <textarea id="" rows="4" v-model="description"></textarea>
            </div>

            <div class="right">
                <router-link to="/app/projects" class="button primary">Retour</router-link> &nbsp;
                <a href="" class="button success" @click.prevent="create()">Enregistrer</a>
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
            description: ''
        }
    },

    methods: {
        create() {
            let self = this;
            axios.post('api/project/create', {
                name: self.name,
                description: self.description
            }).then(function(response) {
                self.$router.push({name: 'app.projects'});
            });
        }
    }
}
</script>


<style lang="scss">
    .project-creation {
        padding: 20px;
        overflow-y: auto;
    }
</style>

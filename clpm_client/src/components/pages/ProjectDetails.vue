<template>
    <div class="project-details">
        <div class="box">
            <div class="space-between">
                <h3>Projet : {{ projectDetails.name }}</h3>
                <router-link :to="{name: 'app.projects'}" class="button primary">Retour</router-link>
            </div>

            <p>{{ projectDetails.description }}</p>


        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            projectDetails: {},
            projectMembers: {}
        }
    },

    mounted() {
        let self = this;
        axios.get('api/project/' + self.$route.params.id + '/details')
            .then(function(response) {
                self.projectDetails = response.data;
                return axios.get('api/project/' + response.data.id + '/users');
            })
            .then(function(response) {
                self.projectMembers = response.data;
            });
    }
}
</script>

<style lang="scss">
    .project-details {
        padding: 20px;
        overflow-y: auto;
    }
</style>

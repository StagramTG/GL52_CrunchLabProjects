<template>
    <div class="project-details">
        <div class="box">
            Détails du projet
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            projectDetails: {}
        }
    },

    mounted() {
        let self = this;
        axios.get('api/project/' + self.$route.params.id + '/details')
            .then(function(response) {
                self.projectDetails = response.data;
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

<template>
    <div class="projects">
        <div class="box">
            <h3>Projets</h3>
            <p>Tous vos projets sont listés ci-dessous</p>

            <table class="data-table">
                <tbody>

                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from '@/services/api'

export default {
    data() {
        return {
            userProjects: {}
        }
    },

    mounted() {
        /* axios.get('').then(function(response) {

        }); */
    }
}
</script>

<style lang="scss">
    .projects {
        padding: 20px;
        overflow-y: auto;
    }
</style>

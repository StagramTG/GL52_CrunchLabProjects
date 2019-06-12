<template>
    <h1>Lol t'es connecté !</h1>
</template>

<script>
/* eslint-disable */
import axios from '@/services/api'

export default {
    mounted: function()
    {
        axios.get('api/').then(function(response) {
            console.log(response);
        })
    }
}
</script>

<style lang="scss">

</style>

<template>
    <div class="content">
        <Navbar/>
        <SideNav/>
    </div>
</template>

<script>
import SideNav from './elements/SideNav.vue'
import Navbar from './elements/Navbar.vue'

export default {
    data: function() {
        return {
            received: {}
        }
    },
    components: {
        SideNav,
        Navbar
    },
}
</script>

<style lang="scss">
    .content {
        height: 100%;
        display: grid;
        grid-template-areas: 
            "nav nav"
            "sidenav content";
        grid-template-columns: 200px 1fr;
        grid-template-rows: 50px 1fr;
    }
</style>

<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'app',
    components: {
        
    }
}
</script>

<style lang="scss">
    html, body
    {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #app {
        position: absolute;
        top: 0; left: 0;
        bottom: 0; right: 0;

        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;

        background-color: #EEEEEE;
    }
</style>

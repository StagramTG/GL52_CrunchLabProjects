<template>
    <div class="top-nav">
        <p class="brand">Crunch Lab</p>
    </div>
</template>

<script>
export default {
    
}
</script>

<style lang="scss">
    $darker: #223843;
    $dark: #41436A;
    $lighter: #EFF1F3;
    $light: #DBD3D8;
    $pink: #D8B4A0;
    $terra: #D77A61;

    .top-nav {
        z-index: 20;
        color: $light;
        background-color: $dark;
        grid-area: top;
        height: 50px;

        .brand {
            padding: 0 0 0 20px;
            margin: 0;

            line-height: 50px;
            font-size: 20px;
        }
    }
</style>

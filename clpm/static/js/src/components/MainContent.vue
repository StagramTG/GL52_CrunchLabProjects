<template>
    <div class="main-content">
        <div class="box">
            <h1>Main content</h1>
            <p>Lorem, ipsum</p>
            <p>Lorem, ipsum</p>
        </div>
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

    .main-content {
        color: $darker;
        background-color: $light;
        grid-area: c;
        overflow-y: auto;
        padding: 20px;
    }
</style>

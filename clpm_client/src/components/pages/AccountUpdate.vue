<template>
    <div class="account-update">
        <div class="box">
            <h3>Modifier vos informations</h3>

            <div class="form-field">
                <span class="label">Nom</span>
                <input type="text" v-model="last_name">
            </div>

            <div class="form-field">
                <span class="label">Prénom</span>
                <input type="text" v-model="first_name">
            </div>

            <div class="form-field">
                <span class="label">Email</span>
                <input type="email" v-model="email">
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            last_name: '',
            first_name: '',
            email: '',
            password: ''
        }
    }
}
</script>

<style lang="scss">
    .account-update {
        padding: 20px;
        overflow-y: auto;
    }
</style>

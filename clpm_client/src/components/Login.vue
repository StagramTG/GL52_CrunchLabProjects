<template>
    <div class="login">
        <div class="login-form">
            <p class="title">Connexion</p>

            <div class="form">
                <div class="form-field">
                    <span>Email</span>
                    <input type="email" name="username" placeholder="ex: example@example.fr">
                </div>

                <div class="form-field">
                    <span>Mot de passe</span>
                    <input type="password" name="password" placeholder="************">
                </div>

                <br>
                <input type="button" value="Se connecter">
            </div>

        </div>
    </div>
</template>

<script>
export default {
    
}
</script>

<style lang="scss">
    .login
    {
        padding: 100px 0 0 0;

        .login-form 
        {
            width: 50%;
            margin: auto;

            background-color: #fff;
            border-radius: 5px;
            box-shadow: rgba(0,0,0,0.1) 0px 5px 10px;
            padding: 20px;

            .title
            {
                text-align: center;
                font-size: 42px;

                margin: 20px 0;
            }

            .form
            {
                display: flex;
                flex-direction: column;

                .form-field
                {
                    display: flex;
                    flex-direction: column;
                    margin: 0 0 20px 0;

                    span
                    {
                        margin: 0 0 5px 0;
                    }

                    input
                    {
                        height: 33px;
                        padding: 0 10px 0 10px;

                        border: none;
                        border-radius: 5px;

                        background-color: #EEEEEE;
                        outline: none;
                    }
                }

                input[type=button]
                {
                    display: block;
                    margin: auto;
                    width: 50%;
                    height: 33px;

                    border: none;
                    border-radius: 5px;
                    outline: none;
                    cursor: pointer;

                    &:hover
                    {
                        background-color: #CCCCCC;
                    }
                }
            }
        }
    }
</style>

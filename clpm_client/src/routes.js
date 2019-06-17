/* eslint-disable */

import Vue from 'vue'
import VueRouter from 'vue-router'

import store from './store/index'

import Login from '@/components/Login.vue'
import Site from '@/components/Site.vue'

import Home from '@/components/pages/Home.vue'
import Account from '@/components/pages/Account.vue'
import Wallet from '@/components/pages/Wallet.vue'
import Projects from '@/components/pages/Projects.vue'

import AccountUpdate from '@/components/pages/AccountUpdate.vue'

Vue.use(VueRouter);

const router = new VueRouter({
    routes: [
        { 
            path: '/', 
            name: 'root', 
            redirect: 'app'
        },
        { 
            path: '/login', 
            component: Login, 
            name: 'login' 
        },
        { 
            path: '/app', 
            component: Site,
            meta: {authenticationNeeded: true},
            children: [
                {
                    path: '',
                    name: 'app',
                    redirect: 'home'
                },
                {
                    path: 'home',
                    component: Home,
                    name: 'app.home',
                    meta: {authenticationNeeded: true},
                },
                {
                    path: 'account',
                    component: Account,
                    name: 'app.account',
                    meta: {authenticationNeeded: true},
                },
                {
                    path: 'account/update',
                    component: AccountUpdate,
                    name: 'app.account.update',
                    meta: {authenticationNeeded: true},
                },
                {
                    path: 'wallet',
                    component: Wallet,
                    name: 'app.wallet',
                    meta: {authenticationNeeded: true},
                },
                {
                    path: 'projects',
                    component: Projects,
                    name: 'app.projects',
                    meta: {authenticationNeeded: true},
                }
            ]
        }
    ]
});

// A DECOMMENTER EN PROD !!!!
/* router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.authenticationNeeded && !store.state.isAuthenticated)) {
        // You can use store variable here to access globalError or commit mutation 
        next("/Login");
    } else {
        next();
    }
}); */

export default router;
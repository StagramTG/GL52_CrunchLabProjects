/* eslint-disable */

import Vue from 'vue'
import VueRouter from 'vue-router'

import Cookies from 'js-cookie'

import Login from '@/components/Login.vue'
import Site from '@/components/Site.vue'

import Home from '@/components/pages/Home.vue'
import Account from '@/components/pages/Account.vue'
import Wallet from '@/components/pages/Wallet.vue'
import Projects from '@/components/pages/Projects.vue'

Vue.use(VueRouter);

export const router = new VueRouter({
    routes: [
        { 
            path: '/', 
            name: 'root', 
            redirect: to => { 
                if(Cookies.get('sessionid')) {
                    console.log(to);
                    return;
                }
            } 
        },
        { path: '/login', component: Login, name: 'login' },
        { 
            path: '/app', 
            component: Site, 
            name: 'app',
            children: [
                {
                    path: '',
                    redirect: '/app/home'
                },
                {
                    path: 'home',
                    component: Home,
                    name: 'home'
                },
                {
                    path: 'account',
                    component: Account,
                    name: 'account'
                },
                {
                    path: 'wallet',
                    component: Wallet,
                    name: 'wallet'
                },
                {
                    path: 'projects',
                    component: Projects,
                    name: 'projects'
                }
            ]
        }
    ]
});
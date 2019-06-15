/* eslint-disable */

import Vue from 'vue'
import VueRouter from 'vue-router'

import Cookies from 'js-cookie'

import Login from '@/components/Login.vue'
import Site from '@/components/Site.vue'

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
        { path: '/app', component: Site, name: 'app' }
    ]
});
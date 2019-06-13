import axios from 'axios'
import Cookies from 'js-cookie'

export default axios.create({
    baseURL: '/',
    timeout: 5000,
    xsrfCookieName: 'csrftoken',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': Cookies.get('csrftoken')
    }
})
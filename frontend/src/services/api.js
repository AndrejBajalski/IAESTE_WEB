import axios from 'axios';

class ApiService {
    constructor(baseURL="/backend/api"){
        this.baseURL = baseURL
    }
    
    async get(endpoint, params = {}) {
        return axios.get(`${this.baseURL}${endpoint}`)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
    async getInternships(params = {}) {
        return axios.get(`${this.baseURL}/internships/`)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
}

export { ApiService };
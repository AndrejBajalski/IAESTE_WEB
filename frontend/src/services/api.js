import axios from 'axios';

class ApiService {
    constructor(baseURL=import.meta.env.VITE_API_BASE_URL){
        this.baseURL = baseURL
        console.log("API BASE URL SET TO: ", this.baseURL)
    }
    
    async get(endpoint, params = {}) {
        const url = this.baseURL + endpoint
        console.log('SENDING API REQUEST TO URL PATH: ', url)
        return axios.get(url)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
    async getInternships(params = {}) {
        const url = this.baseURL + "/api/internships"
        console.log('SENDING API REQUEST TO URL PATH: ', url)
        return axios.get(url)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
}

export { ApiService };
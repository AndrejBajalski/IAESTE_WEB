import axios from 'axios';

class ApiService {
    constructor(baseURL="http://backend-service.default.svc.cluster.local:8000/backend/api"){
        this.baseURL = baseURL
    }
    
    async get(endpoint, params = {}) {
        const url = this.baseURL + endpoint
        console.log('SENDING API REQUEST TO URL PATH: ', url)
        return axios.get(url)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
    async getInternships(params = {}) {
        const url = this.baseURL + "/internships"
        console.log('SENDING API REQUEST TO URL PATH: ', url)
        return axios.get(url)
                    .then(response => response.data)
                    .catch(error => console.log('Error fetching data from API:', error ))
    }
}

export { ApiService };
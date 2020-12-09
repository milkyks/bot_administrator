import axios from 'axios'

export const getCommands = () => {
    return axios.get('https://5fb057bb7edddb0016468450.mockapi.io/commands')
}

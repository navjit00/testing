import { defineStore} from 'pinia'

export const useNotifications = defineStore('notifications', {
    state() {
        return {
            lists: [
                {
                title: 'Received 50 euros',
                timestamp: '20/03/2022'
                },
                {
                title: 'Received 50 euros',
                timestamp: '20/03/2022'
                },
                {
                title: 'Received 50 euros',
                timestamp: '20/03/2022'
                }
            ]
        }
    }
})
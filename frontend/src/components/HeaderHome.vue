<script setup>

import { computed, ref } from 'vue'
import { useUser } from '@/stores/user'
import { useNotifications} from '@/stores/notifications'
import { useRouter } from 'vue-router'

const showFloatingBtn = ref(false)
const user = useUser()
const router = useRouter()
const notifications = useNotifications()

const navigate = path => {
	setTimeout(() => {
		router.push({ name: path })
	}, 300)
}

//Getter
const fullname = computed(() => user.fullname)
const amountNotif = computed(() => notifications.lists)

</script>
